# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\EGOR\Desktop\cursach\Course\SupplierWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(251, 396)
        Dialog.setStyleSheet("QWidget{\n"
"    background-color: rgb(44, 44, 64);\n"
"}\n"
"QPushButton{\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(170, 170, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    font-weight: bold\n"
"}\n"
"QPushButton#delete_btn{\n"
"    background-color: rgb(211, 47, 47);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    font-weight: bold\n"
"\n"
"}\n"
"QLabel{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit{\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-right-color: rgba(255, 255, 255, 0);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    background-color: rgb(50, 50, 64);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLabel#inf_lbl{\n"
"    font-weight: bold\n"
"}\n"
"QComboBox{\n"
"    background-color: rgb(50, 50, 64);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget{\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.mail_line = QtWidgets.QLineEdit(Dialog)
        self.mail_line.setGeometry(QtCore.QRect(10, 40, 231, 21))
        self.mail_line.setObjectName("mail_line")
        self.phone_line = QtWidgets.QLineEdit(Dialog)
        self.phone_line.setGeometry(QtCore.QRect(10, 120, 231, 21))
        self.phone_line.setObjectName("phone_line")
        self.fax_line = QtWidgets.QLineEdit(Dialog)
        self.fax_line.setGeometry(QtCore.QRect(10, 200, 231, 21))
        self.fax_line.setObjectName("fax_line")
        self.add_button = QtWidgets.QPushButton(Dialog)
        self.add_button.setGeometry(QtCore.QRect(140, 310, 101, 41))
        self.add_button.setObjectName("add_button")
        self.supplier_box = QtWidgets.QComboBox(Dialog)
        self.supplier_box.setGeometry(QtCore.QRect(10, 250, 231, 31))
        self.supplier_box.setObjectName("supplier_box")
        self.delete_btn = QtWidgets.QPushButton(Dialog)
        self.delete_btn.setGeometry(QtCore.QRect(10, 310, 111, 41))
        self.delete_btn.setObjectName("delete_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "?????????? ??????????????????"))
        self.label.setText(_translate("Dialog", "?????????????????????? ??????????"))
        self.label_2.setText(_translate("Dialog", "??????????????"))
        self.label_3.setText(_translate("Dialog", "????????"))
        self.add_button.setText(_translate("Dialog", "????????????????"))
        self.delete_btn.setText(_translate("Dialog", "??????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
