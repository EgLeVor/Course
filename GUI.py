import sys

import psycopg2

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QDialog,QWidget,QPushButton,QLineEdit,QInputDialog,QFormLayout,QMessageBox, QDialogButtonBox)

import LoginWindow, ClientRegistrationWindow

connection = None
cur = None
role = None
login = None

def patrick_pavviaz_protection(goverment: str):
    FACE = ("--", ";", "\\", "/", "||", "chr(")
    if any(el in goverment for el in FACE):
        return ""
    return goverment

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
        any()
        connection = psycopg2.connect(
            host="localhost", 
            database="CarsharingDB",
            user="postgres",
            password="QSXFtrew16912"
            )
        connection.set_client_encoding("WIN1251")
        cur = connection.cursor()
        try:
            cur.execute(patrick_pavviaz_protection(f"INSERT INTO clients (lgn, pwd, drv_lic, passport, full_name, phone) VALUES ('{lgn}', '{pwd}', '{drv_lic}', '{passport}', '{full_name}', '{phone}')"))
            cur.execute(patrick_pavviaz_protection(f"CREATE USER \"{lgn}\" WITH ENCRYPTED PASSWORD '{pwd}' IN GROUP \"Client\""))
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
            user=lgn,
            password=pwd
            )
            connection.set_client_encoding("WIN1251")
            cur = connection.cursor()
            self.role()
            if role=="Client":
                connection.commit()
                cur.execute(f"select available from clients")
                available = str(cur.fetchall())
                if available == "true":
                    print("Успешно!")
                else:
                    print("Вы заблокированы!")
                print("Роль установлена!")
            elif role == "TechUser":
                connection.commit()
                print("Роль установлена!")
            elif role == "postgres":
                connection.commit()
                print("Роль установлена!")
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