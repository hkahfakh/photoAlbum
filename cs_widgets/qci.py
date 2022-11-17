import os

from PyQt5.QtCore import pyqtSignal, Qt, QSize, QRect, QStringListModel
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QMenu, QAction, QDialog
from cs_widgets.ml import MyLabel
from cs_widgets.ifdlg import InfoDialog
from PyQt5.QtGui import QCursor, QPixmap
from utils.util import parse_xml_object


class QClickableImage(QWidget):
    def __init__(self, width=0, height=0, initial_path=None, img_id=''):
        QWidget.__init__(self)
        self.initial_path = initial_path
        self.image_path = os.path.join(initial_path, "JPEGImages", img_id)
        self.annotation_path = os.path.join(initial_path, "Annotations", img_id.split('.')[0] + ".xml")
        self.layout = QVBoxLayout(self)
        self.width = width
        self.height = height
        self.pixmap = QPixmap(self.image_path)
        self.img_id = img_id

        self.init_ui()

        self.info = parse_xml_object(self.annotation_path)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)  # 开放右键策略

    def init_ui(self):
        if self.width and self.height:
            self.resize(self.width, self.height)
        if self.pixmap:
            pixmap = self.pixmap.scaled(QSize(self.width, self.height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label1 = QLabel()
            self.label1.setObjectName('label1')
            self.label1.setPixmap(pixmap)
            self.label1.setAlignment(Qt.AlignCenter)
            self.label1.setStyleSheet('background-color: rgb(255, 255, 0)')
            self.layout.addWidget(self.label1)
        if self.img_id:
            self.label2 = QLabel()
            self.label2.setObjectName('label2')
            self.label2.setText(self.img_id)
            self.label2.setAlignment(Qt.AlignCenter)
            self.label2.setWordWrap(True)
            self.label2.setStyleSheet('background-color: rgb(255, 0, 0)')
            self.layout.addWidget(self.label2)
        self.setLayout(self.layout)

    def imageId(self):
        return self.img_id

    def leftMenuShow(self):
        pass

    def rightMenuShow(self, point):
        # 添加右键菜单
        self.popMenu = QMenu()
        im = QAction(u'信息', self)
        ch = QAction(u'隐藏', self)
        sc = QAction(u'删除', self)
        self.popMenu.addAction(im)
        self.popMenu.addAction(ch)
        self.popMenu.addAction(sc)
        # 绑定事件
        im.triggered.connect(self.show_info)
        ch.triggered.connect(self.reback)
        sc.triggered.connect(self.delete)
        self.showContextMenu(QCursor.pos())

    def show_info(self):
        self.idlg = InfoDialog(self.pixmap, self.image_path, self.info)
        self.idlg.show()


    def delete(self):
        '''
        do something
        '''

    def reback(self):
        '''
        do something
        '''
        self.hide()

    def showContextMenu(self, pos):
        # 调整位置
        '''''
        右键点击时调用的函数
        '''
        # 菜单显示前，将它移动到鼠标点击的位置

        self.popMenu.move(pos)
        self.popMenu.show()

    def menuSlot(self, act):
        print(act.text())

    def get_label(self):
        return self.info


