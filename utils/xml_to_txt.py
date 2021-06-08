'''
@Author: your name
@Date: 2020-06-02 14:02:59
LastEditTime: 2021-03-12 18:00:52
LastEditors: Guochong Zhong
@Description: In User Settings Edit
@FilePath: /object_detection/utils/xml_to_txt.py
'''
import glob
import xml.etree.ElementTree as ET

annotations_path = '/home/zgc/test/zhonguochong/jp/annotations/' 

class_name_path = '/home/zgc/test/zhonguochong/jp/jp.names'
with open(class_name_path) as f:
    class_names = f.readlines()
    class_names = [item.strip('\n') for item in class_names]


def single_xml_to_txt(xml_file, flags):
    tree = ET.parse(xml_file)
    root = tree.getroot()
   
    # txt_file = '/home/zgc/zhonguochong/jp/labels/' + flags +'0121/'+ xml_file.split('/')[-1].split('.')[0]+'.txt'
    # txt_file = '/home/zgc/zhonguochong/jp/labels/' + flags +'0311/'+ xml_file.split('/')[-1].split('.')[0]+'.txt'
    
    txt_file = '/home/zgc/test/zhonguochong/jp/labels/' + flags +'0512/'+ xml_file.split('/')[-1].split('.')[0]+'.txt'
    with open(txt_file, 'w') as txt_file:
        for member in root.findall('object'):
            # filename = root.find('filename').text
            picture_width = int(root.find('size')[0].text)
            picture_height = int(root.find('size')[1].text)
            class_name = member[0].text
            
            class_num = class_names.index(class_name)
            box_x_min = int(member[4][0].text)  # 左上角横坐标
            box_y_min = int(member[4][1].text)  # 左上角纵坐标
            box_x_max = int(member[4][2].text)  # 右下角横坐标
            box_y_max = int(member[4][3].text)  # 右下角纵坐标
           
            x_center = (box_x_min + box_x_max) / (2 * picture_width)
            y_center = (box_y_min + box_y_max) / (2 * picture_height)
            width = (box_x_max - box_x_min) / picture_width
            height = (box_y_max - box_y_min) / picture_height
            print(class_num, x_center, y_center, width, height)
            txt_file.write(str(class_num) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(width) + ' ' + str(height) + '\n')


def dir_xml_to_txt(path, flags):
    for xml_file in glob.glob(path + '*.xml'):
        single_xml_to_txt(xml_file, flags)

dir_xml_to_txt(annotations_path + 'train0512/', 'train')
dir_xml_to_txt(annotations_path + 'val0512/', 'val')
