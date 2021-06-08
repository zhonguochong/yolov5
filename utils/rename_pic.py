'''
Author: your name
Date: 2021-06-07 16:29:53
LastEditTime: 2021-06-08 13:53:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /yolov5/utils/rename_pic.py
'''
import os
path = "/home/zgc/test/zhonguochong/皓吉达马达线圈缺陷检测项目/VCM不良图片/tmp/"
# 获取该目录下所有文件，存入列表中
f = os.listdir(path)
print(len(f))

print(f[0])

n = 0
i = 0
for i in f:
    # 设置旧文件名（就是路径+文件名）
    oldname = f[n]

    # 设置新文件名
    # newname = 'overlapping-' + str(n+1) + '.jpg'  # 理线重叠
    # newname = 'beyond-' + str(n+1) + '.jpg'  # 理线超出
    # newname = 'stripTin-' + str(n+7) + '.jpg'  # 剥锡不良
    # newname = 'deformed-' + str(n+1) + '.jpg'  # 线形变
    newname = 'bracket-' + str(n+10) + '.jpg'  # 支架伤
    # newname = 'smallCylinder-' + str(n+1) + '.jpg'  # 小圆柱
    # newname = 'extra-'+ str(n+1) + '.jpg'  # 多余
    # 用os模块中的rename方法对文件改名
    os.rename(path+oldname, path+newname)
    print(oldname, '======>', newname)

    n += 1
