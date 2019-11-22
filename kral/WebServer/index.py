from flask import Flask, request

app = Flask(__name__)

spz = False

@app.route('/save', methods=['POST'])
def save():
    upload = request.files['img']
    upload.save('blaza.jpeg')

@app.route('/spz', methods=['POST'])
def update():
    spz = True
    data = request.data
    print(data)

@app.route('/isSPZ', methods = ['POST'])
def check():
    if spz:
        return 'ok'
    else:
        return 'none'
@app.route('/')
def index():
    print("hello world");
