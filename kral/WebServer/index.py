from flask import Flask, request, render_template, jsonify
global spz
global counter

app = Flask(__name__)

spz = False
counter = 0

@app.route('/save', methods=['POST'])
def save():
    global counter
    upload = request.files['img']
    counter += 1
    if counter % 2 == 0:
        upload.save('blaza2.jpeg')
    else:
        upload.save('blaza1.jpeg')

@app.route('/spz', methods=['POST'])
def update():
    global spz
    spz = True
    data = request.data
    return "True"

@app.route('/isSPZ')
def check():
    if spz:
        return jsonify('true')
    else:
        return jsonify('false')

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0')
