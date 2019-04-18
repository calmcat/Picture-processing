import os
from PIL import Image

global width,height       ##可以修改图片的尺寸
width=550
height=550

ori_path=r'C:\Users\BY\Desktop\socks'  ##读取图片地址
dst_path=r'C:\Users\BY\Desktop\1111111'  ##存储图片地址

def changesize(path,object):
    s = os.listdir(path)
    count = 1
    for i in s:
        document = os.path.join(path,i)
        img = Image.open(document)
        out = img.resize((width,height))
        fileName = ''.join([str(count)])
        out.save(object+os.sep+'%s.jpg' % fileName)
        count = count + 1

changesize(ori_path,dst_path)

##os.sep 根据你所处的平台，自动地采用相应的分割符号
