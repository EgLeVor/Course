# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\EGOR\Desktop\cursach\Course\ReceiptWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1141, 288)
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
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1121, 192))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(44, 44, 64))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(44, 44, 64))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(44, 44, 64))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(44, 44, 64))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(44, 44, 64))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(44, 44, 64))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(44, 44, 64))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(44, 44, 64))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.false_btn = QtWidgets.QPushButton(Dialog)
        self.false_btn.setGeometry(QtCore.QRect(10, 230, 231, 41))
        self.false_btn.setObjectName("false_btn")
        self.all_btn = QtWidgets.QPushButton(Dialog)
        self.all_btn.setGeometry(QtCore.QRect(900, 230, 231, 41))
        self.all_btn.setObjectName("all_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Информация о заказах"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Код поездки"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Логин"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Номер машины"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Описание цели заказа"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Начало поездки"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Конец поездки"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Стоимость"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Статус"))
        self.false_btn.setText(_translate("Dialog", "Неоплаченные поездки"))
        self.all_btn.setText(_translate("Dialog", "Все поездки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
