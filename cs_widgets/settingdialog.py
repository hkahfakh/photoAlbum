#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from ui.setting import Ui_SettingDialog


class SettingDialog(QDialog, Ui_SettingDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
