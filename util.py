# -*- coding: utf-8 -*-
import os
import time
import uuid

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'JPG', 'JPEG', 'PNG'])
LOG_DIR = os.getcwd() + '/log.txt'

def get_cur_time():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))

def get_uuid():
    return str(uuid.uuid4().hex)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def get_all_dirs(path):
    return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

def get_all_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def __run__():
    # print(get_cur_time())
    # print(get_uuid())
    # print(allowed_file('a.jpg'))
    # log('hello')
    # log('world')
    
    # print(get_all_dirs('./uploads'))
    # print(get_all_files('./uploads/train'))
    get_all_usernames()

def log(message):
    with open(LOG_DIR, 'a+') as f:
        f.write(message + '\n')


def get_all_usernames():
    file_list = os.listdir('classifiers')
    res =  [f.split('_')[0] for f in file_list if f.endswith('.pkl')]
    return res

if __name__ == '__main__':
    __run__()