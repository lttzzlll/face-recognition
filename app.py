# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from werkzeug import secure_filename

import util

import os

app = Flask(__name__)

MAX_CONTENT_LENGTH = 1 * 1024 * 1024
UPLOAD_FOLDER = './uploads'

# set the max upload file size 1MB
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['upload_file']
        if file and util.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', img_path=app.config['UPLOAD_FOLDER'] + '/' + filename)


if __name__ == '__main__':
    app.run(debug=True)
