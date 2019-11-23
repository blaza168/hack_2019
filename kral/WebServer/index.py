from flask import Flask, request, render_template, jsonify
import os

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
        upload.save('./static/blaza2.jpeg')
    else:
        upload.save('./static/blaza2.jpeg')
    return "dfs"

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

@app.route('/cams', methods=['GET'])
def cams():
    return render_template("livecams.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0')
