#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QObject, pyqtSignal

from utils.toyolo import get_xml


class xmlThread(QObject):
    #  通过类成员对象定义信号对象
    signal = pyqtSignal(str)

    def __init__(self, img_no_xml):
        super(xmlThread, self).__init__()
        self.img_no_xml = img_no_xml
        self.flag = False

    def __del__(self):
        print(">>> __del__")

    def run(self):
        while self.flag and self.img_no_xml:
            name = self.img_no_xml.pop()
            print(get_xml("./res/JPEGImages/" + name))
            self.signal.emit(str(name))
