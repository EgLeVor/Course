# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\EGOR\Desktop\cursach\Course\CarWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(311, 481)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.brand_line = QtWidgets.QLineEdit(Dialog)
        self.brand_line.setGeometry(QtCore.QRect(20, 40, 271, 22))
        self.brand_line.setObjectName("brand_line")
        self.mileage_line = QtWidgets.QLineEdit(Dialog)
        self.mileage_line.setGeometry(QtCore.QRect(20, 100, 271, 22))
        self.mileage_line.setObjectName("mileage_line")
        self.loc_line = QtWidgets.QLineEdit(Dialog)
        self.loc_line.setGeometry(QtCore.QRect(20, 160, 271, 22))
        self.loc_line.setObjectName("loc_line")
        self.cost_line = QtWidgets.QLineEdit(Dialog)
        self.cost_line.setGeometry(QtCore.QRect(20, 220, 271, 22))
        self.cost_line.setObjectName("cost_line")
        self.buy_date_line = QtWidgets.QLineEdit(Dialog)
        self.buy_date_line.setGeometry(QtCore.QRect(20, 280, 271, 22))
        self.buy_date_line.setObjectName("buy_date_line")
        self.supplier_box = QtWidgets.QComboBox(Dialog)
        self.supplier_box.setGeometry(QtCore.QRect(40, 340, 73, 31))
        self.supplier_box.setObjectName("supplier_box")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.add_btn = QtWidgets.QPushButton(Dialog)
        self.add_btn.setGeometry(QtCore.QRect(160, 317, 111, 41))
        self.add_btn.setObjectName("add_btn")
        self.delete_btn = QtWidgets.QPushButton(Dialog)
        self.delete_btn.setGeometry(QtCore.QRect(60, 390, 171, 41))
        self.delete_btn.setObjectName("delete_btn")
        self.car_box = QtWidgets.QComboBox(Dialog)
        self.car_box.setGeometry(QtCore.QRect(100, 440, 91, 31))
        self.car_box.setObjectName("car_box")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новая машина"))
        self.label.setText(_translate("Dialog", "Марка машины"))
        self.label_2.setText(_translate("Dialog", "Пробег (в километрах)"))
        self.label_3.setText(_translate("Dialog", "Местонахождение"))
        self.label_4.setText(_translate("Dialog", "Цена (в рублях)"))
        self.label_5.setText(_translate("Dialog", "Дата покупки (формат гггг-мм-дд)"))
        self.label_6.setText(_translate("Dialog", "ИД поставщика"))
        self.add_btn.setText(_translate("Dialog", "Добавить"))
        self.delete_btn.setText(_translate("Dialog", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())