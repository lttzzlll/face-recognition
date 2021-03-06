# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from werkzeug import secure_filename
from flask import jsonify

import util
import net

import shutil
import os

app = Flask(__name__)

MAX_CONTENT_LENGTH = 1 * 1024 * 1024
UPLOAD_FOLDER = 'uploads'
TRAIN_DIR = UPLOAD_FOLDER + '/train'
TRAIN_ALIGN_DIR = UPLOAD_FOLDER + '/train_align'
TEST_DIR = UPLOAD_FOLDER + '/test'
TEST_ALIGN_DIR = UPLOAD_FOLDER + '/test_align'
TEMP_DIR = '/tmp'
CUR_PATH = os.getcwd()

# set the max upload file size 1MB
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = TRAIN_DIR
app.config['UPLOAD_TRAIN_ALIGN_FOLDER'] = TRAIN_ALIGN_DIR
app.config['UPLOAD_TEST_FOLDER'] = TEST_DIR
app.config['UPLOAD_TEST_ALIGN_FOLDER'] = TEST_ALIGN_DIR
app.config['TMP_DIR'] = TEMP_DIR
app.config['CUR_PATH'] = CUR_PATH

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/uploads/train/<path:filename>')
def uploaded_train_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/uploads/train_align/<path:filename>')
def uploaded_train_align_file(filename):
    print(filename)
    return send_from_directory(app.config['UPLOAD_TRAIN_ALIGN_FOLDER'], filename)

@app.route('/uploads/test/<path:filename>')
def uploaded_test_file(filename):
    return send_from_directory(app.config['UPLOAD_TEST_FOLDER'], filename)

@app.route('/uploads/test_align/<path:filename>')    
def uploaded_test_align_file(filename):
    return send_from_directory(app.config['UPLOAD_TEST_ALIGN_FOLDER'], filename)

@app.route('/validateusername', methods=['POST'])
def validate_username():
    if request.method == 'POST':
        name = request.form["name"]
        if name is not None and len(name) > 0 and name in util.get_all_usernames():
            return jsonify(res=True)
    return jsonify(res=False)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        username = request.form["username"]
        if username is None or len(username) == 0:
            return render_template("index.html")
        
        file = request.files['upload_file']
        if file and util.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            dirpath = os.path.join(app.config['UPLOAD_TEST_FOLDER'], username)
            align_dirpath = os.path.join(app.config['UPLOAD_TEST_ALIGN_FOLDER'], username)
            align_filepath = os.path.join(align_dirpath, filename)
            
            shutil.rmtree(app.config['UPLOAD_TEST_FOLDER'])
            shutil.rmtree(app.config['UPLOAD_TEST_ALIGN_FOLDER'])
            os.mkdir(app.config['UPLOAD_TEST_FOLDER'])
            os.mkdir(app.config['UPLOAD_TEST_ALIGN_FOLDER'])
            os.mkdir(dirpath)

            filepath = os.path.join(dirpath, filename)
            file.save(filepath)
            
            des = 'tmp/%s' % util.get_uuid()
            src = 'tmp/%s' % util.get_uuid()
        
            shutil.copytree(dirpath, os.path.join(src, username))
            net.align_dataset(des, src, 0.25, True, 32, 160)
            shutil.copytree(os.path.join(des, username), os.path.join('uploads/test_align', username))
            shutil.rmtree(src)
            shutil.rmtree(des)

            res = net.classify(False,
                            'CLASSIFY',
                            app.config['UPLOAD_TEST_ALIGN_FOLDER'],
                            20,
                            10,
                            '20170512-110547/20170512-110547.pb',
                            'classifiers/%s_classifier.pkl' % username,
                            1000,
                        160)

            
            if res[0][1] == username and res[0][2] >= 0.90:
                # generate a random filename 
                pic_name = util.get_uuid() + '.png'
                pic_align_name = util.get_uuid() + '.png'
                des_path = os.path.join(os.path.join(app.config['UPLOAD_FOLDER'], username), pic_name)
                align_des_path = os.path.join(os.path.join(app.config['UPLOAD_TRAIN_ALIGN_FOLDER'], username), pic_align_name)
                shutil.move(filepath, des_path)            
                shutil.move(align_filepath.split('.')[0] + '.png', align_des_path)

                return render_template('index.html', 
                                        # img_path='uploads/train/%s/%s' % (username, pic_name), 
                                        img_align_path=align_des_path,
                                        username=username,
                                        prob=res[0][2])
            else:
                return render_template('index.html', 
                                        img_path=filepath, 
                                        # img_align_path='uploads/test_align/%s/%s' %(username, filename),
                                        err_msg='not the {} picture'.format(username))
        else:
            return render_template('index.html')


@app.route('/uploads', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('files[]')
        name = request.form['name']
        path = os.path.join(app.config['UPLOAD_FOLDER'], name)
        if not os.path.exists(path):
            os.makedirs(path)
        for f in uploaded_files:
            f.save(os.path.join(path, f.filename))
        
        des = 'tmp/%s' % util.get_uuid()
        src = 'tmp/%s' % util.get_uuid()

        dirpath = os.path.join(app.config['UPLOAD_FOLDER'], name)
        shutil.copytree(dirpath, os.path.join(src, name))
        net.align_dataset(des, src, 0.25, True, 32, 160)
        shutil.copytree(os.path.join(des, name), os.path.join(app.config['UPLOAD_TRAIN_ALIGN_FOLDER'], name))
        shutil.rmtree(src)
        shutil.rmtree(des)
        shutil.copytree(os.path.join(app.config['UPLOAD_TRAIN_ALIGN_FOLDER'], name), os.path.join('tmp', name))

        res = net.train(False,
                        'TRAIN',
                        'tmp',
                        20,
                        10,
                        '20170512-110547/20170512-110547.pb',
                        'classifiers/%s_classifier.pkl' % name,
                        1000,
                        160)

        shutil.rmtree(os.path.join('tmp', name))

        img_list = [os.path.join(path, f.filename) for f in uploaded_files]
        img_align_path = os.path.join(app.config['UPLOAD_TRAIN_ALIGN_FOLDER'], name) 
        img_align_list = [os.path.join(os.path.join(img_align_path, f.filename.split('.')[0] + '.png')) for f in uploaded_files]
        
        return render_template('index.html', img_align_list=img_align_list, name=name)

@app.route('/*')
def notfound404():
   return render_template('404notfound.html')


if __name__ == '__main__':
    app.run(debug=True)
