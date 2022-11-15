#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from ui.img_info import Ui_Dialog


class InfoDialog(QDialog, Ui_Dialog):
    def __init__(self, pixmap, image_path, img_label, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.pixmap = pixmap
        self.image_path = image_path
        self.img_label = img_label

        self.lineEdit.setText(image_path)
        self.label_3.setPixmap(pixmap)
        self.label_3.setStyleSheet('background-color: rgb(255, 255, 0)')
        self.lineEdit_2.setText(str(img_label))
