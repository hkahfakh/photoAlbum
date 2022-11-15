from PyQt5.QtWidgets import QLabel, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor


class MyLabel(QLabel):
    global NOP_value, NOP_dict

    def __init__(self, pixmap=None, image_id=None, info=""):
        ye = self.parent
        QLabel.__init__(self)
        self.pixmap = pixmap
        self.image_id = image_id
        self.setPixmap(pixmap)

        self.info = info

        self.setAlignment(Qt.AlignCenter)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)  # 开放右键策略

    def leftMenuShow(self):
        pass

    def rightMenuShow(self, point):
        # 添加右键菜单
        self.popMenu = QMenu()
        im = QAction(u'信息', self)
        ch = QAction(u'撤回', self)
        sc = QAction(u'删除', self)
        xs = QAction(u'显示相似频率', self)
        self.popMenu.addAction(im)
        self.popMenu.addAction(ch)
        self.popMenu.addAction(sc)
        self.popMenu.addAction(xs)
        # 绑定事件
        im.triggered.connect(self.show_info)
        ch.triggered.connect(self.reback)
        sc.triggered.connect(self.delete)
        xs.triggered.connect(self.rshow)
        self.showContextMenu(QCursor.pos())

    def show_info(self):
        print(self.info)

    def rshow(self):
        '''
        do something
        '''

    def delete(self):
        '''
        do something
        '''

    def reback(self):
        '''
        do something
        '''

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
