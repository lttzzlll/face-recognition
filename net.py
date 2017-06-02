# -*- coding: utf-8 -*-

import facenet.src.classifier as classifier
import facenet.src.align.align_dataset_mtcnn as align_dataset_mtcnn

class FaceRec(object):
    def __init__(self):
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

    def train(self,
                use_split_dataset,
                mode,
                data_dir, 
                min_nrof_images_per_class, 
                nrof_train_images_per_class,
                model,
                classifier_filename,
                batch_size,
                image_size):
        
        classifier.train(use_split_dataset,
                mode,
                data_dir, 
                min_nrof_images_per_class, 
                nrof_train_images_per_class,
                model,
                classifier_filename,
                batch_size,
                image_size)

    def align_dataset(self, 
            output_dir,
            input_dir,
            gpu_memory_fraction,
            random_order,
            margin,
            image_size):
        align_dataset_mtcnn.align_dataset(output_dir,
                                    input_dir,
                                    gpu_memory_fraction,
                                    random_order,
                                    margin,
                                    image_size)

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

def train(use_split_dataset,
            mode,
            data_dir, 
            min_nrof_images_per_class, 
            nrof_train_images_per_class,
            model,
            classifier_filename,
            batch_size,
            image_size):
    
    facerec = FaceRec()    
    
    facerec.train(use_split_dataset,
                    mode,
                    data_dir, 
                    min_nrof_images_per_class, 
                    nrof_train_images_per_class,
                    model,
                    classifier_filename,
                    batch_size,
                    image_size)

def align_dataset(output_dir,
            input_dir,
            gpu_memory_fraction,
            random_order,
            margin,
            image_size):
    facerec = FaceRec()
    facerec.align_dataset(output_dir, 
                    input_dir, 
                    gpu_memory_fraction, 
                    random_order,
                    margin, 
                    image_size)

def main():
    
    align_dataset('rec/train_align', 'rec/train', 0.25, True, 32, 160)
    # res = classify(False,
    #                 'CLASSIFY',
    #                 'tmp/temp',
    #                 20,
    #                 10,
    #                 '20170512-110547/20170512-110547.pb',
    #                 'classifiers/jay_classifier.pkl',
    #                 1000,
    #                 160)

    # print(res)

    # train(False,
    #         'TRAIN',
    #         'tmp',
    #         20,
    #         10,
    #         '20170512-110547/20170512-110547.pb',
    #         'classifiers/luo_classifier.pkl',
    #         1000,
    #         160)


if __name__ == '__main__':
    main()
