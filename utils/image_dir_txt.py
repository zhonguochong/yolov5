'''
@Author: your name
@Date: 2020-06-02 15:00:51
@LastEditTime: 2020-06-16 10:32:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /yolov3/utils/img_dir_txt.py
'''
import glob

path = 'jp/datasets/'

def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:
        for jpg_file in glob.glob(image_path + '*.BMP'):
            tf.write(jpg_file + '\n')

generate_train_and_val(path + 'train_images/', 'jp/train.txt')
generate_train_and_val(path + 'val_images/', 'jp/val.txt')
