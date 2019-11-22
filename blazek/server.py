from flask import Flask, request, Response, jsonify
import time
import cv2
import numpy as np
import tensorflow as tf
from yolov3_tf2.models import (
    YoloV3, YoloV3Tiny
)
from yolov3_tf2.dataset import transform_images
from yolov3_tf2.utils import draw_outputs


app = Flask(__name__)


physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_visible_devices(physical_devices[0], 'GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

yolo = YoloV3(classes=80)
yolo.load_weights('./checkpoints/yolov3.tf')
class_names = [c.strip() for c in open('./data/coco.names').readlines()]
print("Yolo model is OK")


def process(path):
    print("b")
    img = tf.image.decode_image(open(path, 'rb').read(), channels=3)
    print("a")
    img = tf.expand_dims(img, 0)
    img = transform_images(img, 416)

    print("b")
    t1 = time.time()
    boxes, scores, classes, nums = yolo(img)
    t2 = time.time()
    print('time: {}'.format(t2 - t1))

    print('detections:')
    for i in range(nums[0]):
        print('\t{}, {}, {}'.format(class_names[int(classes[0][i])],
                                           np.array(scores[0][i]),
                                           np.array(boxes[0][i])))

    img = cv2.imread('input.jpg')
    img = draw_outputs(img, (boxes, scores, classes, nums), class_names)
    cv2.imwrite('output.jpg', img)
    print('output saved to: {}'.format('output.jpg'))

    return nums, boxes, scores, classes


def get_num_cars(nums, boxes, scores, classes):
    count = 0
    for i in range(nums[0]):
        class_name = class_names[int(classes[0][i])]
        if class_name == "car" or class_name == "truck":
            count += 1
    print("COUNT: {}".format(count))
    return count

@app.route("/test", methods=["GET"])
def test():
    return Response("OK")

@app.route('/process', methods=['POST'])
def process_img():
    print("accessing image")
    if 'img' not in request.files:
        print("not img")
        return Response('Please provide image with "img" key'), 400
    upload = request.files['img']
    print("upload")
    upload.save('input.jpg')
    nums, boxes, scores, classes = process('input.jpg')
    return Response(str(get_num_cars(nums, boxes, scores, classes)))


app.run(host="0.0.0.0", port=5555)
