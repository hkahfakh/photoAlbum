#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from ui.about import Ui_AboutDialog


class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)