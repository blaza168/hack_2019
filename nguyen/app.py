from flask import *
import base64
import os
app = Flask(__name__)

@app.route('/')
def takePhoto():
	os.system('raspistill -w 1280 -h 720 -t 1 -o image.jpg')
	return send_file('image.jpg')
#base64.b64encode(open('image.jpg', 'r').read())

if __name__ == '__main__':
	app.run(host='0.0.0.0')
