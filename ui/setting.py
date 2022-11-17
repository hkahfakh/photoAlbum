# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        SettingDialog.setObjectName("SettingDialog")
        SettingDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(SettingDialog)
        self.buttonBox.accepted.connect(SettingDialog.accept)
        self.buttonBox.rejected.connect(SettingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingDialog)

    def retranslateUi(self, SettingDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingDialog.setWindowTitle(_translate("SettingDialog", "Dialog"))

