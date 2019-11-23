from flask import Flask, request, render_template, jsonify

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

@app.route('/isSPZ')
def check():
    if spz:
        return jsonify('ok')
    else:
        return jsonify('none')

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0')
