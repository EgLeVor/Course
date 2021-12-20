import sys, random

import psycopg2

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow,QWidget,QPushButton,QLineEdit,QInputDialog,QFormLayout,QMessageBox, QDialogButtonBox)

import LoginWindow, ClientRegistrationWindow, ClientWindow, TripWindow, ClientOrderWindow

connection = None
cur = None
role = None
login = None

def patrick_pavviaz_protection(goverment: str):
    FACE = ("--", "'", ";", "\\", "/", "||", "chr(")
    if any(el in goverment for el in FACE):
        return ''
    return goverment

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

class Client(QDialog, ClientWindow.Ui_Dialog):
    def __init__(self):
        global cur, connection, login
        super().__init__()
        self.setupUi(self)
        cur.execute("SELECT code, car_id, date_time, description FROM orders")
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

    def refresh_table(self, table):
        global cur, connection, login
        if table == "Машины":
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
            item.setText("Пробег к километрах")
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
        elif table == "Заказы":
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
        connection = psycopg2.connect(
        host="localhost", 
        database="CarsharingDB",
        user="Qwardley",
        password="SHH389ZCA4"
        )
        connection.set_client_encoding("WIN1251")
        cur = connection.cursor()
        self.role()
        if role=="Client":
            connection.commit()
            cur.execute(f"select available from clients")
            available = str(cur.fetchall())
            if available == "[(True,)]":
                print("Успешно!")
                main_window = Client()
                connection.commit()
                main_window.exec()
            else:
                print("Вы заблокированы!")
                reject = QMessageBox()
                reject.setWindowTitle("Ошибка")
                reject.setText("Вы заблокированы!")
                reject.setStandardButtons(QMessageBox.Ok)
                reject.exec_()
                print("Роль установлена!")
        elif role == "TechUser":
            connection.commit()
            print("Роль установлена!")
        elif role == "postgres":
            connection.commit()
            print("Роль установлена!")
        # try:
        #     connection = psycopg2.connect(
        #     host="localhost", 
        #     database="CarsharingDB",
        #     user="Qwardley",
        #     password="SHH389ZCA4"
        #     )
        #     connection.set_client_encoding("WIN1251")
        #     cur = connection.cursor()
        #     self.role()
        #     if role=="Client":
        #         connection.commit()
        #         cur.execute(f"select available from clients")
        #         available = str(cur.fetchall())
        #         if available == "[(True,)]":
        #             print("Успешно!")
        #             main_window = Client()
        #             main_window.exec()
        #         else:
        #             print("Вы заблокированы!")
        #             reject = QMessageBox()
        #             reject.setWindowTitle("Ошибка")
        #             reject.setText("Вы заблокированы!")
        #             reject.setStandardButtons(QMessageBox.Ok)
        #             reject.exec_()
        #         print("Роль установлена!")
        #     elif role == "TechUser":
        #         connection.commit()
        #         print("Роль установлена!")
        #     elif role == "postgres":
        #         connection.commit()
        #         print("Роль установлена!")
        # except Exception as ex:
        #     reject = QMessageBox()
        #     reject.setWindowTitle("Ошибка")
        #     reject.setText("Неправильный логин или пароль!")
        #     reject.setStandardButtons(QMessageBox.Ok)
        #     reject.exec_()

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