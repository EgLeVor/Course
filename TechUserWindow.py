# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\EGOR\Desktop\cursach\Course\TechUserWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1191, 818)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cars_tbl = QtWidgets.QTableWidget(self.centralwidget)
        self.cars_tbl.setGeometry(QtCore.QRect(10, 50, 911, 211))
        self.cars_tbl.setObjectName("cars_tbl")
        self.cars_tbl.setColumnCount(6)
        self.cars_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cars_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cars_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cars_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.cars_tbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.cars_tbl.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.cars_tbl.setHorizontalHeaderItem(5, item)
        self.supp_contr_tbl = QtWidgets.QTableWidget(self.centralwidget)
        self.supp_contr_tbl.setGeometry(QtCore.QRect(10, 315, 911, 211))
        self.supp_contr_tbl.setObjectName("supp_contr_tbl")
        self.supp_contr_tbl.setColumnCount(4)
        self.supp_contr_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.supp_contr_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.supp_contr_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.supp_contr_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.supp_contr_tbl.setHorizontalHeaderItem(3, item)
        self.supp_contr_box = QtWidgets.QComboBox(self.centralwidget)
        self.supp_contr_box.setGeometry(QtCore.QRect(820, 275, 101, 31))
        self.supp_contr_box.setObjectName("supp_contr_box")
        self.supp_contr_box.addItem("")
        self.supp_contr_box.addItem("")
        self.work_serv_tbl = QtWidgets.QTableWidget(self.centralwidget)
        self.work_serv_tbl.setGeometry(QtCore.QRect(10, 580, 911, 211))
        self.work_serv_tbl.setObjectName("work_serv_tbl")
        self.work_serv_tbl.setColumnCount(4)
        self.work_serv_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.work_serv_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.work_serv_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.work_serv_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.work_serv_tbl.setHorizontalHeaderItem(3, item)
        self.work_serv_box = QtWidgets.QComboBox(self.centralwidget)
        self.work_serv_box.setGeometry(QtCore.QRect(770, 540, 151, 31))
        self.work_serv_box.setObjectName("work_serv_box")
        self.work_serv_box.addItem("")
        self.work_serv_box.addItem("")
        self.cars_update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cars_update_btn.setGeometry(QtCore.QRect(820, 10, 101, 31))
        self.cars_update_btn.setObjectName("cars_update_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 540, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.phone_line = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_line.setGeometry(QtCore.QRect(940, 120, 241, 22))
        self.phone_line.setObjectName("phone_line")
        self.name_lbl = QtWidgets.QLabel(self.centralwidget)
        self.name_lbl.setGeometry(QtCore.QRect(940, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_lbl.setFont(font)
        self.name_lbl.setObjectName("name_lbl")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(940, 210, 241, 41))
        self.update_btn.setObjectName("update_btn")
        self.inf_lbl = QtWidgets.QLabel(self.centralwidget)
        self.inf_lbl.setGeometry(QtCore.QRect(940, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inf_lbl.setFont(font)
        self.inf_lbl.setObjectName("inf_lbl")
        self.email_lbl = QtWidgets.QLabel(self.centralwidget)
        self.email_lbl.setGeometry(QtCore.QRect(940, 150, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_lbl.setFont(font)
        self.email_lbl.setObjectName("email_lbl")
        self.phone_lbl = QtWidgets.QLabel(self.centralwidget)
        self.phone_lbl.setGeometry(QtCore.QRect(940, 100, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phone_lbl.setFont(font)
        self.phone_lbl.setObjectName("phone_lbl")
        self.email_line = QtWidgets.QLineEdit(self.centralwidget)
        self.email_line.setGeometry(QtCore.QRect(940, 170, 241, 22))
        self.email_line.setObjectName("email_line")
        self.name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line.setGeometry(QtCore.QRect(940, 70, 241, 22))
        self.name_line.setObjectName("name_line")
        self.clients_viol_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clients_viol_btn.setGeometry(QtCore.QRect(940, 330, 241, 41))
        self.clients_viol_btn.setObjectName("clients_viol_btn")
        self.orders_trips_btn = QtWidgets.QPushButton(self.centralwidget)
        self.orders_trips_btn.setGeometry(QtCore.QRect(940, 380, 241, 41))
        self.orders_trips_btn.setObjectName("orders_trips_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тех. поддержка"))
        item = self.cars_tbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер машины"))
        item = self.cars_tbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ИД поставщика"))
        item = self.cars_tbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Доступность"))
        item = self.cars_tbl.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Местонахождение"))
        item = self.cars_tbl.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Марка"))
        item = self.cars_tbl.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Пробег"))
        item = self.supp_contr_tbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ИД поставщика"))
        item = self.supp_contr_tbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.supp_contr_tbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Телефон"))
        item = self.supp_contr_tbl.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Факс"))
        self.supp_contr_box.setItemText(0, _translate("MainWindow", "Поставщики"))
        self.supp_contr_box.setItemText(1, _translate("MainWindow", "Контракты"))
        item = self.work_serv_tbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ИД автомастерской"))
        item = self.work_serv_tbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.work_serv_tbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Телефон"))
        item = self.work_serv_tbl.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Факс"))
        self.work_serv_box.setItemText(0, _translate("MainWindow", "Мастерские"))
        self.work_serv_box.setItemText(1, _translate("MainWindow", "Тех. обслуживание"))
        self.cars_update_btn.setText(_translate("MainWindow", "Обновить"))
        self.label.setText(_translate("MainWindow", "Машины"))
        self.label_2.setText(_translate("MainWindow", "Поставщики и контракты"))
        self.label_3.setText(_translate("MainWindow", "Мастерские и тех. обслуживание"))
        self.name_lbl.setText(_translate("MainWindow", "ФИО"))
        self.update_btn.setText(_translate("MainWindow", "Обновить информацию"))
        self.inf_lbl.setText(_translate("MainWindow", "Информация о пользователе:"))
        self.email_lbl.setText(_translate("MainWindow", "Email"))
        self.phone_lbl.setText(_translate("MainWindow", "Телефон"))
        self.clients_viol_btn.setText(_translate("MainWindow", "Информация о клиентах"))
        self.orders_trips_btn.setText(_translate("MainWindow", "Информация о заказах"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
