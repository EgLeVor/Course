# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\EGOR\Desktop\cursach\Course\ClientInformationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1191, 543)
        self.clients_tbl = QtWidgets.QTableWidget(Dialog)
        self.clients_tbl.setGeometry(QtCore.QRect(20, 45, 911, 211))
        self.clients_tbl.setObjectName("clients_tbl")
        self.clients_tbl.setColumnCount(6)
        self.clients_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.clients_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.clients_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.clients_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.clients_tbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.clients_tbl.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.clients_tbl.setHorizontalHeaderItem(5, item)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 15, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.violations_tbl = QtWidgets.QTableWidget(Dialog)
        self.violations_tbl.setGeometry(QtCore.QRect(20, 295, 911, 211))
        self.violations_tbl.setObjectName("violations_tbl")
        self.violations_tbl.setColumnCount(2)
        self.violations_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.violations_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.violations_tbl.setHorizontalHeaderItem(1, item)
        self.update_tbl_btn = QtWidgets.QPushButton(Dialog)
        self.update_tbl_btn.setGeometry(QtCore.QRect(950, 50, 221, 41))
        self.update_tbl_btn.setObjectName("update_tbl_btn")
        self.update_viol_btn = QtWidgets.QPushButton(Dialog)
        self.update_viol_btn.setGeometry(QtCore.QRect(950, 360, 211, 41))
        self.update_viol_btn.setObjectName("update_viol_btn")
        self.lgn_box = QtWidgets.QComboBox(Dialog)
        self.lgn_box.setGeometry(QtCore.QRect(1080, 300, 81, 21))
        self.lgn_box.setObjectName("lgn_box")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(950, 300, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cnt_line = QtWidgets.QLineEdit(Dialog)
        self.cnt_line.setGeometry(QtCore.QRect(1110, 330, 51, 22))
        self.cnt_line.setObjectName("cnt_line")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(950, 330, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Информация о клиентах"))
        item = self.clients_tbl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ФИО"))
        item = self.clients_tbl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Логин"))
        item = self.clients_tbl.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Имеет ли доступ"))
        item = self.clients_tbl.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Номер водительских прав"))
        item = self.clients_tbl.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Паспорт"))
        item = self.clients_tbl.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Телефон"))
        self.label.setText(_translate("Dialog", "Клиенты"))
        self.label_2.setText(_translate("Dialog", "Нарушения клиентов"))
        item = self.violations_tbl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Номер водительских прав"))
        item = self.violations_tbl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Количество нарушений"))
        self.update_tbl_btn.setText(_translate("Dialog", "Обновить таблицы"))
        self.update_viol_btn.setText(_translate("Dialog", "Изменить кол-во нарушений"))
        self.label_3.setText(_translate("Dialog", "Логин клиента"))
        self.label_4.setText(_translate("Dialog", "Кол-во нарушений"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())