# -*- coding: utf-8 -*-

import facenet.src.classifier as classifier

class FaceRec(object):
    def __init__(self):
        pass

    def train(self):
        pass

    def classify(self, 
                use_split_dataset,
                mode,
                data_dir, 
                min_nrof_images_per_class, 
                nrof_train_images_per_class,
                model,
                classifier_filename,
                batch_size,
                image_size):

        res = classifier.classify(use_split_dataset,
                mode,
                data_dir, 
                min_nrof_images_per_class, 
                nrof_train_images_per_class,
                model,
                classifier_filename,
                batch_size,
                image_size)

        return res


def classify(use_split_dataset,
            mode,
            data_dir, 
            min_nrof_images_per_class, 
            nrof_train_images_per_class,
            model,
            classifier_filename,
            batch_size,
            image_size):
    
    facerec = FaceRec()
    
    res = facerec.classify(use_split_dataset,
                    mode,
                    data_dir, 
                    min_nrof_images_per_class, 
                    nrof_train_images_per_class,
                    model,
                    classifier_filename,
                    batch_size,
                    image_size)

    return res

def main():
    res = classify(False,
                    'CLASSIFY',
                    'tmp/temp',
                    20,
                    10,
                    '20170512-110547/20170512-110547.pb',
                    'classifiers/jay_classifier.pkl',
                    1000,
                    160)

    print(res)
    
if __name__ == '__main__':
    main()
