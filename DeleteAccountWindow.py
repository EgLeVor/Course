# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\EGOR\Desktop\cursach\Course\DeleteAccountWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(344, 114)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.yes_btn = QtWidgets.QPushButton(Dialog)
        self.yes_btn.setGeometry(QtCore.QRect(40, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yes_btn.setFont(font)
        self.yes_btn.setObjectName("yes_btn")
        self.no_btn = QtWidgets.QPushButton(Dialog)
        self.no_btn.setGeometry(QtCore.QRect(180, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.no_btn.setFont(font)
        self.no_btn.setObjectName("no_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Удаление аккаунта"))
        self.label.setText(_translate("Dialog", "Вы уверены, что хотите удалить аккаунт?"))
        self.yes_btn.setText(_translate("Dialog", "Да"))
        self.no_btn.setText(_translate("Dialog", "Нет"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
