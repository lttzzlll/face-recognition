# -*- coding: utf-8 -*-
import os
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG'])
LOG_DIR = os.getcwd() + '/log.txt'

def get_cur_time():
    import time
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))

def get_uuid():
    import uuid
    return str(uuid.uuid4().hex)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def __run__():
    print(get_cur_time())
    print(get_uuid())
    print(allowed_file('a.jpg'))
    log('hello')
    log('world')
    
def log(message):
    with open(LOG_DIR, 'a+') as f:
        f.write(message + '\n')


if __name__ == '__main__':
    __run__()