#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import requests
import os


def get_xml(file_path):
    # API地址
    url = "http://[2409:8a3c:7d15:b3d0:c8b1:5a5d:8d9d:1e89]:5000/photo"
    # 图片名
    file_name = file_path.split('/')[-1]
    # xml名
    xml_name = file_name.split('.')[0] + ".xml"
    # xml 路径
    xml_dir = "./res/Annotations/"
    # 二进制打开图片
    file = open(file_path, 'rb')
    # 拼接参数
    files = {'file': (file_name, file, 'image/jpg')}
    # 发送post请求到服务器端
    r = requests.post(url, files=files)
    # 获取服务器返回的图片，字节流返回
    result = r.content
    # 字节转换成xml
    xml_str = base64.b64decode(result)

    file = open(os.path.join(xml_dir, xml_name), 'wb')
    file.write(xml_str)
    file.close()
    return xml_str


if __name__ == '__main__':
    get_xml('../res/JPEGImages/street.jpg')
