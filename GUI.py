import sys, random

import psycopg2

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow,QWidget,QPushButton,QLineEdit,QInputDialog,QFormLayout,QMessageBox, QDialogButtonBox)

import LoginWindow, ClientRegistrationWindow, ClientWindow, TripWindow, ClientOrderWindow, TechUserWindow, ClientInformationWindow, ReceiptWindow, WorkshopWindow, SupplierWindow, CarWindow, TechnicalServiceWindow

connection = None
cur = None
role = None
login = None

def patrick_pavviaz_protection(goverment: str):
    FACE = ("--", "'", ";", "\\", "/", "||", "chr(")
    if any(el in goverment for el in FACE):
        return ''
    return goverment

class TechnicalService(QDialog, TechnicalServiceWindow.Ui_Dialog):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)

class Car(QDialog, CarWindow.Ui_Dialog):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)

class Supplier(QDialog, SupplierWindow.Ui_Dialog):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)

class Workshop(QDialog, WorkshopWindow.Ui_Dialog):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)

class Receipt(QDialog, ReceiptWindow.Ui_Dialog):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)

class ClientInformation(QDialog, ClientInformationWindow.Ui_Dialog):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)

class TechUser(QMainWindow, TechUserWindow.Ui_MainWindow):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)
        self.cars()
        self.suppliers()
        self.workshops()
        cur.execute("SELECT full_name FROM tech_users")
        for el in cur.fetchall():
            self.name_line.setText(str(el[0]))
        cur.execute("SELECT phone FROM tech_users")
        for el in cur.fetchall():
            self.phone_line.setText(str(el[0]))
        cur.execute("SELECT email FROM tech_users")
        for el in cur.fetchall():
            self.email_line.setText(str(el[0]))
        self.update_btn.clicked.connect(lambda:self.update_techuser(self.name_line.text(), self.phone_line.text(), self.email_line.text()))
        self.supp_contr_box.currentTextChanged.connect(self.refresh_table)
        self.work_serv_box.currentTextChanged.connect(self.refresh_table)
        self.cars_update_btn.clicked.connect(self.refresh_car_table)
        self.clients_viol_btn.clicked.connect(self.create_client_information_window)
        self.orders_trips_btn.clicked.connect(self.create_receipt_window)
        self.workshop_btn.clicked.connect(self.create_workshop_window)
        self.supplier_btn.clicked.connect(self.create_supplier_window)
        self.car_contract_btn.clicked.connect(self.create_car_window)
        self.tech_service_btn.clicked.connect(self.create_technical_service_window)
        cur.execute("SELECT car_id FROM technical_service WHERE status=false")
        for el in cur.fetchall():
            self.tech_car_box.addItem(str(el[0]))
        self.finish_btn.clicked.connect(lambda:self.finish(self.tech_car_box.currentText()))
        connection.commit()

    def finish(self, car_id):
        global cur, connection, login
        cur.execute(f"UPDATE technical_service SET status=true WHERE car_id={car_id}")
        connection.commit()

    def create_technical_service_window(self):
        global cur, connection, login
        window = TechnicalService()
        cur.execute("SELECT workshop_id FROM workshops ORDER BY workshop_id ASC")
        for el in cur.fetchall():
            window.workshop_box.addItem(str(el[0]))
        connection.commit()
        cur.execute("SELECT car_id FROM cars WHERE available=true ORDER BY car_id ASC")
        for el in cur.fetchall():
            window.car_box.addItem(str(el[0]))
        connection.commit()
        window.add_btn.clicked.connect(lambda:self.add_technical_service(window.car_box.currentText(), window.workshop_box.currentText(), window.desc_line.text(), window.cost_line.text(), window.date_line.text(), window))
        window.exec()

    def add_technical_service(self, car_id, workshop_id, objective, cost, start_task, window):
        global cur, connection, login
        if patrick_pavviaz_protection(objective) == '' or patrick_pavviaz_protection(cost) == '' or patrick_pavviaz_protection(start_task) == '':
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Проверьте введённые данные!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            try:
                cur.execute(f"INSERT INTO technical_service (workshop_id, car_id, objective, \"cost\", start_task) VALUES ({workshop_id}, {car_id}, '{objective}', {cost}, '{start_task}')")
                reject = QMessageBox()
                reject.setWindowTitle("Сообщение")
                reject.setText("Успешно!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
                connection.commit()
                window.close()
            except Exception as ex:
                reject = QMessageBox()
                reject.setWindowTitle("Ошибка")
                reject.setText("Проверьте введённые данные!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
            finally:
                connection.commit()

    def create_car_window(self):
        global cur, connection, login
        window = Car()
        cur.execute("SELECT supplier_id FROM suppliers ORDER BY supplier_id ASC")
        for el in cur.fetchall():
            window.supplier_box.addItem(str(el[0]))
        window.add_btn.clicked.connect(lambda:self.create_car(window.brand_line.text(), window.mileage_line.text(), window.loc_line.text(), window.cost_line.text(), window.buy_date_line.text(), window.supplier_box.currentText(), window))
        window.exec()

    def create_car(self, brand, mileage, loc, cost, buy_date, supplier_id, window):
        global cur, connection, login
        if patrick_pavviaz_protection(brand) == '' or patrick_pavviaz_protection(mileage) == '' or patrick_pavviaz_protection(loc) == '' or patrick_pavviaz_protection(cost) == '' or patrick_pavviaz_protection(buy_date) == '':
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Проверьте введённые данные!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            try:
                cur.execute(f"INSERT INTO cars (supplier_id, loc, brand, mileage) values ({supplier_id}, '{loc}', '{brand}', {mileage}) returning car_id")
                for el in cur.fetchall():
                    car_id = el[0]
                connection.commit()
                cur.execute(f"INSERT INTO contracts (car_id, supplier_id, \"cost\", buy_date) VALUES ({car_id}, {supplier_id}, {cost}, '{buy_date}')")
                reject = QMessageBox()
                reject.setWindowTitle("Сообщение")
                reject.setText("Успешно!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
                connection.commit()
                window.close()
            except Exception as ex:
                reject = QMessageBox()
                reject.setWindowTitle("Ошибка")
                reject.setText("Проверьте введённые данные!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
            finally:
                connection.commit()


    def create_supplier(self, email, phone, fax, window):
        global cur, connection, login
        if patrick_pavviaz_protection(email) == '' or patrick_pavviaz_protection(phone) == '' or patrick_pavviaz_protection(fax) == '':
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Проверьте введённые данные!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            try:
                cur.execute(f"INSERT INTO suppliers (email, phone, fax) VALUES ('{email}', {phone}, {fax})")
                reject = QMessageBox()
                reject.setWindowTitle("Сообщение")
                reject.setText("Успешно!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
                connection.commit()
                window.close()
            except Exception as ex:
                reject = QMessageBox()
                reject.setWindowTitle("Ошибка")
                reject.setText("Проверьте введённые данные!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
            finally:
                connection.commit()

    def create_workshop(self, email, phone, fax, window):
        global cur, connection, login
        if patrick_pavviaz_protection(email) == '' or patrick_pavviaz_protection(phone) == '' or patrick_pavviaz_protection(fax) == '':
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Проверьте введённые данные!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            try:
                cur.execute(f"INSERT INTO workshops (email, phone, fax) VALUES ('{email}', {phone}, {fax})")
                reject = QMessageBox()
                reject.setWindowTitle("Сообщение")
                reject.setText("Успешно!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
                connection.commit()
                window.close()
            except Exception as ex:
                reject = QMessageBox()
                reject.setWindowTitle("Ошибка")
                reject.setText("Проверьте введённые данные!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
            finally:
                connection.commit()

    def create_supplier_window(self):
        window = Supplier()
        window.add_button.clicked.connect(lambda:self.create_supplier(window.mail_line.text(), window.phone_line.text(), window.fax_line.text(), window))
        window.exec()

    def create_workshop_window(self):
        window = Workshop()
        window.add_button.clicked.connect(lambda:self.create_workshop(window.mail_line.text(), window.phone_line.text(), window.fax_line.text(), window))
        window.exec()

    def create_receipt_window(self):
        self.receipt_window = Receipt()
        self.receipt()
        self.receipt_window.exec()

    def receipt(self):
        global cur, connection, login
        self.receipt_window.tableWidget.setColumnCount(8)
        self.receipt_window.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.receipt_window.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.receipt_window.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.receipt_window.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.receipt_window.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.receipt_window.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.receipt_window.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.receipt_window.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.receipt_window.tableWidget.setHorizontalHeaderItem(7, item)
        item = self.receipt_window.tableWidget.horizontalHeaderItem(0)
        item.setText("Код")
        item = self.receipt_window.tableWidget.horizontalHeaderItem(1)
        item.setText("Логин")
        item = self.receipt_window.tableWidget.horizontalHeaderItem(2)
        item.setText("Номер машины")
        item = self.receipt_window.tableWidget.horizontalHeaderItem(3)
        item.setText("Описание")
        item = self.receipt_window.tableWidget.horizontalHeaderItem(4)
        item.setText("Начало поездки")
        item = self.receipt_window.tableWidget.horizontalHeaderItem(5)
        item.setText("Конец поездки")
        item = self.receipt_window.tableWidget.horizontalHeaderItem(6)
        item.setText("Стоимость")
        item = self.receipt_window.tableWidget.horizontalHeaderItem(7)
        item.setText("Статус")
        cur.execute("select code1, lgn, car_id, description, start_trip, end_trip, \"cost\", status from receipt")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.receipt_window.tableWidget.rowCount()
            self.receipt_window.tableWidget.insertRow(rowPosition)
            for i in range(self.receipt_window.tableWidget.columnCount()):
                self.receipt_window.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.receipt_window.tableWidget.resizeColumnToContents(0)
        self.receipt_window.tableWidget.resizeColumnToContents(1)
        self.receipt_window.tableWidget.resizeColumnToContents(2)
        self.receipt_window.tableWidget.resizeColumnToContents(3)
        self.receipt_window.tableWidget.resizeColumnToContents(4)
        self.receipt_window.tableWidget.resizeColumnToContents(5)
        self.receipt_window.tableWidget.resizeColumnToContents(6)
        self.receipt_window.tableWidget.resizeColumnToContents(7)

    def create_client_information_window(self):
        global cur, connection, login
        self.client_window = ClientInformation()
        self.clients()
        self.violations()
        self.client_window.update_tbl_btn.clicked.connect(self.refresh_clients_violations_table)
        cur.execute("SELECT lgn FROM clients ORDER BY lgn DESC")
        for el in cur.fetchall():
            self.client_window.lgn_box.addItem(str(el[0]))
        self.client_window.update_viol_btn.clicked.connect(lambda:self.update_violations(self.client_window.lgn_box.currentText(), self.client_window.cnt_line.text()))
        self.client_window.exec()

    def update_violations(self, lgn, cnt):
        global cur, connection, login
        cur.execute(f"SELECT drv_lic FROM clients WHERE lgn='{lgn}'")
        for el in cur.fetchall():
            drv_lic = el[0]
        cur.execute(f"SELECT cnt FROM violations WHERE drv_lic={drv_lic}")
        for el in cur.fetchall():
            check_cnt = el[0]
        if patrick_pavviaz_protection(cnt) == '' or int(check_cnt) >= int(cnt):
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Проверьте введённые данные!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            cur.execute(f"UPDATE violations SET cnt={cnt} WHERE drv_lic={drv_lic}")
            connection.commit()
            reject = QMessageBox()
            reject.setWindowTitle("Сообщение")
            reject.setText("Успешно!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()

    def refresh_clients_violations_table(self):
        self.violations()
        self.clients()

    def refresh_car_table(self):
        self.cars()

    def refresh_table(self, table):
        if table == "Поставщики":
            self.suppliers()
        elif table == "Контракты":
            self.contracts()
        elif table == "Мастерские":
            self.workshops()
        elif table == "Тех. обслуживание":
            self.technical_service()

    def violations(self):
        global cur, connection, login
        self.client_window.violations_tbl.setColumnCount(2)
        self.client_window.violations_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.client_window.violations_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.client_window.violations_tbl.setHorizontalHeaderItem(1, item)
        item = self.client_window.violations_tbl.horizontalHeaderItem(0)
        item.setText("Номер водительских прав")
        item = self.client_window.violations_tbl.horizontalHeaderItem(1)
        item.setText("Количество нарушений")
        cur.execute("SELECT * FROM violations ORDER BY cnt ASC")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.client_window.violations_tbl.rowCount()
            self.client_window.violations_tbl.insertRow(rowPosition)
            for i in range(self.client_window.violations_tbl.columnCount()):
                self.client_window.violations_tbl.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.client_window.violations_tbl.resizeColumnToContents(0)
        self.client_window.violations_tbl.resizeColumnToContents(1)

    def clients(self):
        global cur, connection, login
        self.client_window.clients_tbl.setColumnCount(6)
        self.client_window.clients_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.client_window.clients_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.client_window.clients_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.client_window.clients_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.client_window.clients_tbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.client_window.clients_tbl.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.client_window.clients_tbl.setHorizontalHeaderItem(5, item)
        item = self.client_window.clients_tbl.horizontalHeaderItem(0)
        item.setText("ФИО")
        item = self.client_window.clients_tbl.horizontalHeaderItem(1)
        item.setText("Логин")
        item = self.client_window.clients_tbl.horizontalHeaderItem(2)
        item.setText("Имеет ли доступ")
        item = self.client_window.clients_tbl.horizontalHeaderItem(3)
        item.setText("Номер водительских прав")
        item = self.client_window.clients_tbl.horizontalHeaderItem(4)
        item.setText("Паспорт")
        item = self.client_window.clients_tbl.horizontalHeaderItem(5)
        item.setText("Телефон")
        cur.execute("SELECT full_name, lgn, available, drv_lic, passport, phone FROM clients ORDER BY lgn ASC")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.client_window.clients_tbl.rowCount()
            self.client_window.clients_tbl.insertRow(rowPosition)
            for i in range(self.client_window.clients_tbl.columnCount()):
                self.client_window.clients_tbl.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.client_window.clients_tbl.resizeColumnToContents(0)
        self.client_window.clients_tbl.resizeColumnToContents(1)
        self.client_window.clients_tbl.resizeColumnToContents(2)
        self.client_window.clients_tbl.resizeColumnToContents(3)
        self.client_window.clients_tbl.resizeColumnToContents(4)
        self.client_window.clients_tbl.resizeColumnToContents(5)

    def technical_service(self):
        global cur, connection, login
        self.work_serv_tbl.setColumnCount(8)
        self.work_serv_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(7, item)
        item = self.work_serv_tbl.horizontalHeaderItem(0)
        item.setText("ИД задания")
        item = self.work_serv_tbl.horizontalHeaderItem(1)
        item.setText("ИД автомастерской")
        item = self.work_serv_tbl.horizontalHeaderItem(2)
        item.setText("Номер машины")
        item = self.work_serv_tbl.horizontalHeaderItem(3)
        item.setText("Задание")
        item = self.work_serv_tbl.horizontalHeaderItem(4)
        item.setText("Стоимость")
        item = self.work_serv_tbl.horizontalHeaderItem(5)
        item.setText("Дата начала")
        item = self.work_serv_tbl.horizontalHeaderItem(6)
        item.setText("Дата конца")
        item = self.work_serv_tbl.horizontalHeaderItem(7)
        item.setText("Статус")
        cur.execute("SELECT * FROM technical_service ORDER BY task_id ASC")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.work_serv_tbl.rowCount()
            self.work_serv_tbl.insertRow(rowPosition)
            for i in range(self.work_serv_tbl.columnCount()):
                self.work_serv_tbl.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.work_serv_tbl.resizeColumnToContents(0)
        self.work_serv_tbl.resizeColumnToContents(1)
        self.work_serv_tbl.resizeColumnToContents(2)
        self.work_serv_tbl.resizeColumnToContents(3)
        self.work_serv_tbl.resizeColumnToContents(4)
        self.work_serv_tbl.resizeColumnToContents(5)
        self.work_serv_tbl.resizeColumnToContents(6)
        self.work_serv_tbl.resizeColumnToContents(7)

    def contracts(self):
        global cur, connection, login
        self.supp_contr_tbl.setColumnCount(5)
        self.supp_contr_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.supp_contr_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.supp_contr_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.supp_contr_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.supp_contr_tbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.supp_contr_tbl.setHorizontalHeaderItem(4, item)
        item = self.supp_contr_tbl.horizontalHeaderItem(0)
        item.setText("ИД контракта")
        item = self.supp_contr_tbl.horizontalHeaderItem(1)
        item.setText("Номер машины")
        item = self.supp_contr_tbl.horizontalHeaderItem(2)
        item.setText("ИД поставщика")
        item = self.supp_contr_tbl.horizontalHeaderItem(3)
        item.setText("Стоимость")
        item = self.supp_contr_tbl.horizontalHeaderItem(4)
        item.setText("Дата покупки")
        cur.execute("SELECT * FROM contracts ORDER BY contract_id ASC")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.supp_contr_tbl.rowCount()
            self.supp_contr_tbl.insertRow(rowPosition)
            for i in range(self.supp_contr_tbl.columnCount()):
                self.supp_contr_tbl.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.supp_contr_tbl.resizeColumnToContents(0)
        self.supp_contr_tbl.resizeColumnToContents(1)
        self.supp_contr_tbl.resizeColumnToContents(2)
        self.supp_contr_tbl.resizeColumnToContents(3)
        self.supp_contr_tbl.resizeColumnToContents(4)

    def workshops(self):
        global cur, connection, login
        self.work_serv_tbl.setColumnCount(4)
        self.work_serv_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.work_serv_tbl.setHorizontalHeaderItem(3, item)
        item = self.work_serv_tbl.horizontalHeaderItem(0)
        item.setText("ИД автомастерской")
        item = self.work_serv_tbl.horizontalHeaderItem(1)
        item.setText("Email")
        item = self.work_serv_tbl.horizontalHeaderItem(2)
        item.setText("Телефон")
        item = self.work_serv_tbl.horizontalHeaderItem(3)
        item.setText("Факс")
        cur.execute("SELECT * FROM workshops ORDER BY workshop_id ASC")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.work_serv_tbl.rowCount()
            self.work_serv_tbl.insertRow(rowPosition)
            for i in range(self.work_serv_tbl.columnCount()):
                self.work_serv_tbl.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.work_serv_tbl.resizeColumnToContents(0)
        self.work_serv_tbl.resizeColumnToContents(1)
        self.work_serv_tbl.resizeColumnToContents(2)
        self.work_serv_tbl.resizeColumnToContents(3)

    def suppliers(self):
        global cur, connection, login
        self.supp_contr_tbl.setColumnCount(4)
        self.supp_contr_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.supp_contr_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.supp_contr_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.supp_contr_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.supp_contr_tbl.setHorizontalHeaderItem(3, item)
        item = self.supp_contr_tbl.horizontalHeaderItem(0)
        item.setText("ИД поставщика")
        item = self.supp_contr_tbl.horizontalHeaderItem(1)
        item.setText("Email")
        item = self.supp_contr_tbl.horizontalHeaderItem(2)
        item.setText("Телефон")
        item = self.supp_contr_tbl.horizontalHeaderItem(3)
        item.setText("Факс")
        cur.execute("SELECT * FROM suppliers ORDER BY supplier_id ASC")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.supp_contr_tbl.rowCount()
            self.supp_contr_tbl.insertRow(rowPosition)
            for i in range(self.supp_contr_tbl.columnCount()):
                self.supp_contr_tbl.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.supp_contr_tbl.resizeColumnToContents(0)
        self.supp_contr_tbl.resizeColumnToContents(1)
        self.supp_contr_tbl.resizeColumnToContents(2)
        self.supp_contr_tbl.resizeColumnToContents(3)

    def cars(self):
        global cur, connection, login
        self.cars_tbl.setColumnCount(6)
        self.cars_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.cars_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.cars_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.cars_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.cars_tbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.cars_tbl.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.cars_tbl.setHorizontalHeaderItem(5, item)
        item = self.cars_tbl.horizontalHeaderItem(0)
        item.setText("Номер машины")
        item = self.cars_tbl.horizontalHeaderItem(1)
        item.setText("ИД поставщиков")
        item = self.cars_tbl.horizontalHeaderItem(2)
        item.setText("Доступность")
        item = self.cars_tbl.horizontalHeaderItem(3)
        item.setText("Местонахождение")
        item = self.cars_tbl.horizontalHeaderItem(4)
        item.setText("Марка")
        item = self.cars_tbl.horizontalHeaderItem(5)
        item.setText("Пробег (в километрах)")
        cur.execute("SELECT * FROM cars ORDER BY car_id ASC")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.cars_tbl.rowCount()
            self.cars_tbl.insertRow(rowPosition)
            for i in range(self.cars_tbl.columnCount()):
                self.cars_tbl.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.cars_tbl.resizeColumnToContents(0)
        self.cars_tbl.resizeColumnToContents(1)
        self.cars_tbl.resizeColumnToContents(2)
        self.cars_tbl.resizeColumnToContents(3)
        self.cars_tbl.resizeColumnToContents(4)
        self.cars_tbl.resizeColumnToContents(5)

    def update_techuser(self, full_name, phone, email):
        global cur, connection, login
        if patrick_pavviaz_protection(full_name) == '' or patrick_pavviaz_protection(phone) == '' or patrick_pavviaz_protection(email) == '':
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Проверьте введённые данные!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            try:
                cur.execute(f"UPDATE tech_users SET full_name = '{full_name}';")
                cur.execute(f"UPDATE tech_users SET phone = '{phone}';")
                cur.execute(f"UPDATE tech_users SET email = '{email}';")
                connection.commit()
                reject = QMessageBox()
                reject.setWindowTitle("Сообщение")
                reject.setText("Данные успешно обновлены!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
            except Exception as ex:
                reject = QMessageBox()
                reject.setWindowTitle("Ошибка")
                reject.setText("Проверьте введённые данные!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
            finally:
                connection.commit()

class ClientOrder(QDialog, ClientOrderWindow.Ui_ClientOrderWindow):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)

class Trip(QDialog, TripWindow.Ui_Dialog):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)

class Client(QMainWindow, ClientWindow.Ui_MainWindow):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)
        cur.execute("SELECT code, car_id, date_time, description FROM orders")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.tableWidget.resizeColumnToContents(0)
        self.tableWidget.resizeColumnToContents(1)
        self.tableWidget.resizeColumnToContents(2)
        self.tableWidget.resizeColumnToContents(3)
        cur.execute("SELECT full_name FROM clients")
        for el in cur.fetchall():
            self.name_line.setText(str(el[0]))
        cur.execute("SELECT phone FROM clients")
        for el in cur.fetchall():
            self.phone_line.setText(str(el[0]))
        cur.execute("SELECT passport FROM clients")
        for el in cur.fetchall():
            self.passport_line.setText(str(el[0]))
        self.comboBox.currentTextChanged.connect(self.refresh_table)
        self.trip_info_btn.clicked.connect(self.create_trip_window)
        self.insert_btn.clicked.connect(self.create_order_window)
        self.update_btn.clicked.connect(lambda:self.update_client(self.name_line.text(), self.phone_line.text(), self.passport_line.text()))
        self.find_btn.clicked.connect(lambda:self.find_brand(self.brand_line.text()))

    def find_brand(self, part_brand):
        global cur, connection, login
        if patrick_pavviaz_protection(part_brand) == '':
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Проверьте введённые данные!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(10)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(10)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(10)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(10)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(3, item)
            item = self.tableWidget.horizontalHeaderItem(0)
            item.setText("Номер машины")
            item = self.tableWidget.horizontalHeaderItem(1)
            item.setText("Местонахождение машины")
            item = self.tableWidget.horizontalHeaderItem(2)
            item.setText("Марка машины")
            item = self.tableWidget.horizontalHeaderItem(3)
            item.setText("Пробег (в километрах)")
            data = cur.execute(f"select * from get_car_by_part_brand('{part_brand}')")
            tablerow = 0
            self.tableWidget.resizeColumnToContents(0)
            self.tableWidget.resizeColumnToContents(1)
            self.tableWidget.resizeColumnToContents(2)
            self.tableWidget.resizeColumnToContents(3)
            for row in cur.fetchall():
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                for i in range(self.tableWidget.columnCount()):
                    self.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
                tablerow += 1

    def refresh_trip_table(self, table):
        global cur, connection, login
        self.trip_window.tableWidget.setColumnCount(5)
        self.trip_window.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.trip_window.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.trip_window.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.trip_window.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.trip_window.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.trip_window.tableWidget.setHorizontalHeaderItem(4, item)
        item = self.trip_window.tableWidget.horizontalHeaderItem(0)
        item.setText("Номер поездки")
        item = self.trip_window.tableWidget.horizontalHeaderItem(1)
        item.setText("Начало поездки")
        item = self.trip_window.tableWidget.horizontalHeaderItem(2)
        item.setText("Конец поездки")
        item = self.trip_window.tableWidget.horizontalHeaderItem(3)
        item.setText("Стоимость поездки")
        item = self.trip_window.tableWidget.horizontalHeaderItem(4)
        item.setText("Статус оплаты")
        cur.execute(f"SELECT trip_id, start_trip, end_trip, cost, status FROM trips WHERE code='{int(table)}'")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.trip_window.tableWidget.rowCount()
            self.trip_window.tableWidget.insertRow(rowPosition)
            for i in range(self.trip_window.tableWidget.columnCount()):
                self.trip_window.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.trip_window.tableWidget.resizeColumnToContents(0)
        self.trip_window.tableWidget.resizeColumnToContents(1)
        self.trip_window.tableWidget.resizeColumnToContents(2)
        self.trip_window.tableWidget.resizeColumnToContents(3)
        self.trip_window.tableWidget.resizeColumnToContents(4)

    def update_client(self, full_name, phone, passport):
        global cur, connection, login
        if patrick_pavviaz_protection(full_name) == '' or patrick_pavviaz_protection(phone) == '' or patrick_pavviaz_protection(passport) == '':
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Проверьте введённые данные!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            try:
                cur.execute(f"UPDATE clients SET full_name = '{full_name}';")
                cur.execute(f"UPDATE clients SET phone = '{phone}';")
                cur.execute(f"UPDATE clients SET passport = '{passport}';")
                connection.commit()
                reject = QMessageBox()
                reject.setWindowTitle("Сообщение")
                reject.setText("Данные успешно обновлены!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
            except Exception as ex:
                reject = QMessageBox()
                reject.setWindowTitle("Ошибка")
                reject.setText("Проверьте введённые данные!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
            finally:
                connection.commit()

    def create_order_window(self):
        global cur, connection, login
        window = ClientOrder()
        cur.execute("SELECT car_id FROM cars WHERE available=true ORDER BY car_id ASC")
        for el in cur.fetchall():
            window.car_box.addItem(str(el[0]))
        window.confirm_btn.clicked.connect(lambda:self.create_order(window.car_box.currentText(), window.descr_line.text(), window))
        window.exec()

    def create_order(self, car_id, descripion, window):
        global cur, connection, login
        if patrick_pavviaz_protection(descripion) == '':
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Проверьте введённые данные!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            check = False
            code = random.randint(100000, 999999)
            while not check:
                try:
                    cur.execute("rollback")
                    cur.execute(f"begin; insert into orders (code, car_id, description) values ({code}, {car_id}, '{descripion}'); insert into trips (code) values ({code}); commit;")
                    check = True
                    connection.commit()
                except Exception as ex:
                    print("Double!")
                finally:
                    connection.commit()
            reject = QMessageBox()
            reject.setWindowTitle("Сообщение")
            reject.setText("Заказ успешно создан")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
            window.close()

    def create_trip_window(self):
        global cur, connection, login
        self.trip_window = Trip()
        cur.execute("SELECT code FROM orders ORDER BY date_time DESC")
        for el in cur.fetchall():
            self.trip_window.comboBox.addItem(str(el[0]))
        self.trip_window.tableWidget.setColumnCount(5)
        self.trip_window.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.trip_window.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.trip_window.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.trip_window.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.trip_window.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.trip_window.tableWidget.setHorizontalHeaderItem(4, item)
        item = self.trip_window.tableWidget.horizontalHeaderItem(0)
        item.setText("Номер поездки")
        item = self.trip_window.tableWidget.horizontalHeaderItem(1)
        item.setText("Начало поездки")
        item = self.trip_window.tableWidget.horizontalHeaderItem(2)
        item.setText("Конец поездки")
        item = self.trip_window.tableWidget.horizontalHeaderItem(3)
        item.setText("Стоимость поездки")
        item = self.trip_window.tableWidget.horizontalHeaderItem(4)
        item.setText("Статус оплаты")
        cur.execute(f"SELECT trip_id, start_trip, end_trip, cost, status FROM trips WHERE code='{self.trip_window.comboBox.currentText()}'")
        tablerow = 0
        for row in cur.fetchall():
            rowPosition = self.trip_window.tableWidget.rowCount()
            self.trip_window.tableWidget.insertRow(rowPosition)
            for i in range(self.trip_window.tableWidget.columnCount()):
                self.trip_window.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1
        self.trip_window.tableWidget.resizeColumnToContents(0)
        self.trip_window.tableWidget.resizeColumnToContents(1)
        self.trip_window.tableWidget.resizeColumnToContents(2)
        self.trip_window.tableWidget.resizeColumnToContents(3)
        self.trip_window.tableWidget.resizeColumnToContents(4)
        self.trip_window.comboBox.currentTextChanged.connect(self.refresh_trip_table)
        self.trip_window.end_btn.clicked.connect(lambda:self.end_trip(self.trip_window.comboBox.currentText()))
        self.trip_window.pay_btn.clicked.connect(lambda:self.pay_trip(self.trip_window.comboBox.currentText()))
        self.trip_window.load_btn.clicked.connect(lambda:self.load_data(self.trip_window.comboBox.currentText()))
        self.trip_window.exec()

    def load_data(self, code):
        global cur, connection, login
        cur.execute(f"SELECT status FROM trips WHERE code={code}")
        for el in cur.fetchall():
            status = el[0]
        if status == True:
            cur.execute(f"call statistics_upload({code})")
            connection.commit()
            reject = QMessageBox()
            reject.setWindowTitle("Сообщение")
            reject.setText("Квитанция выгружена на ваше устройство!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            reject = QMessageBox()
            reject.setWindowTitle("Сообщение")
            reject.setText("Поездка не оплачена!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()

    def pay_trip(self, code):
        global cur, connection, login
        cur.execute(F"UPDATE trips SET status=true WHERE code={code} AND end_trip IS NOT NULL")
        connection.commit()
        self.refresh_trip_table(code)

    def end_trip(self, code):
        global cur, connection, login
        cur.execute(F"UPDATE trips SET end_trip=now() WHERE code={code} AND end_trip IS NULL")
        connection.commit()
        self.refresh_trip_table(code)

    def cars(self):
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Номер машины")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Местонахождение машины")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Марка машины")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Пробег (в километрах)")
        cur.execute("SELECT car_id, loc, brand, mileage FROM cars WHERE available=true ORDER BY car_id ASC")
        tablerow = 0
        self.tableWidget.resizeColumnToContents(0)
        self.tableWidget.resizeColumnToContents(1)
        self.tableWidget.resizeColumnToContents(2)
        self.tableWidget.resizeColumnToContents(3)
        for row in cur.fetchall():
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1

    def orders(self):
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Код поездки")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Номер машины")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Дата и время создания заказа")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Описание цели заказа")
        cur.execute("SELECT code, car_id, date_time, description FROM orders ORDER BY date_time ASC")
        tablerow = 0
        self.tableWidget.resizeColumnToContents(0)
        self.tableWidget.resizeColumnToContents(1)
        self.tableWidget.resizeColumnToContents(2)
        self.tableWidget.resizeColumnToContents(3)
        for row in cur.fetchall():
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow += 1

    def refresh_table(self, table):
        global cur, connection, login
        if table == "Машины":
            self.cars()
        elif table == "Заказы":
            self.orders()

class ClientRegistration(QDialog, ClientRegistrationWindow.Ui_RegistrationWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pwd_line.setEchoMode(QLineEdit.Password)

class Login(QDialog, LoginWindow.Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pwd_line.setEchoMode(QLineEdit.Password)
        self.lgn_btn.clicked.connect(lambda:self.login(self.lgn_line.text(), self.pwd_line.text()))
        self.reg_btn.clicked.connect(self.create_registration_window)
        self.exit_btn.clicked.connect(self.close)
    
    def create_registration_window(self):
        window = ClientRegistration()
        window.reg_btn.clicked.connect(lambda:self.registration(window.lgn_line.text(),
                                                                window.pwd_line.text(),
                                                                window.phone_line.text(),
                                                                window.name_line.text(),
                                                                window.passport_line.text(),
                                                                window.drv_line.text(),
                                                                window))
        window.exit_btn.clicked.connect(window.close)
        window.exec()

    def registration(self, lgn, pwd, phone, full_name, passport, drv_lic, old_window):
        if patrick_pavviaz_protection(lgn) == '' or patrick_pavviaz_protection(pwd) == '' or patrick_pavviaz_protection(phone) == '' or patrick_pavviaz_protection(full_name) == '' or patrick_pavviaz_protection(passport) == '' or patrick_pavviaz_protection(drv_lic) == '':
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Проверьте введённые данные!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()
        else:
            connection = psycopg2.connect(
                host="localhost", 
                database="CarsharingDB",
                user="postgres",
                password="QSXFtrew16912"
                )
            connection.set_client_encoding("WIN1251")
            cur = connection.cursor()
            try:
                cur.execute(f"INSERT INTO clients (lgn, pwd, drv_lic, passport, full_name, phone) VALUES ('{lgn}', '{pwd}', '{drv_lic}', '{passport}', '{full_name}', '{phone}')")
                cur.execute(f"CREATE USER \"{lgn}\" WITH ENCRYPTED PASSWORD '{pwd}' IN GROUP \"Client\"")
                reject = QMessageBox()
                reject.setWindowTitle("Сообщение")
                reject.setText("Пользователь успешно зарегистрирован!")
                reject.setStandardButtons(QMessageBox.Ok)
                connection.commit()
                reject.exec_()
                old_window.close()
            except Exception as ex:
                    reject = QMessageBox()
                    reject.setWindowTitle("Ошибка")
                    reject.setText("Проверьте введённые данные!")
                    reject.setStandardButtons(QMessageBox.Ok)
                    reject.exec_()
            finally:
                    connection.commit()
            del(cur, connection)

    def login(self, lgn, pwd):
        global cur, connection, login
        try:
            connection = psycopg2.connect(
            host="localhost", 
            database="CarsharingDB",
            # user = lgn,
            # password = pwd
            user="Johand",
            password="5T7BRYYMSO"
            # user="Qwardley",
            # password="SHH389ZCA4"
            )
            connection.set_client_encoding("WIN1251")
            cur = connection.cursor()
            connection.commit()
            self.close()
        except Exception as ex:
            reject = QMessageBox()
            reject.setWindowTitle("Ошибка")
            reject.setText("Неправильный логин или пароль!")
            reject.setStandardButtons(QMessageBox.Ok)
            reject.exec_()

    def role(self):
        global role, cur, connection
        resolver = ["Client", "TechUser", "postgres"]
        for el in resolver:
            cur.execute(f"select * from pg_has_role('{el}', 'member')")
            for eli in cur.fetchall():
                for inner_el in eli:
                    if inner_el:
                        role = el
                        print(role)

app = QtWidgets.QApplication(sys.argv)
window = Login()
window.show()    
app.exec_()
window.role()
if role=="Client":
    connection.commit()
    cur.execute(f"select available from clients")
    available = str(cur.fetchall())
    if available == "[(True,)]":
        print("Успешно!")
        main_window = Client()
        main_window.show()
        app.exec_()
    else:
        print("Вы заблокированы!")
        reject = QMessageBox()
        reject.setWindowTitle("Ошибка")
        reject.setText("Вы заблокированы!")
        reject.setStandardButtons(QMessageBox.Ok)
        reject.exec_()
        print("Роль установлена!")
elif role == "TechUser":
    main_window = TechUser()
    main_window.show()
    app.exec_()
    print("Роль установлена!")
elif role == "postgres":
    connection.commit()
    print("Роль установлена!")