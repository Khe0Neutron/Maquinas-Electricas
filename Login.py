from PyQt5 import QtWidgets, uic,QtCore
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from window1 import Ui_MainWindow, Ui_MainWindow2, Ui_MainWindow3
from img import imagenes 
class ExitSignal(QtCore.QObject):
    exit_program = QtCore.pyqtSignal()

# Iniciar la aplicación
app = QtWidgets.QApplication([])

# Crear instancias de las ventanas definidas en window1.py
login = QtWidgets.QMainWindow()
login_ui = Ui_MainWindow()
login_ui.setupUi(login)

# Cargar archivos .ui para las otras ventanas
entrar = QtWidgets.QMainWindow()
entrar_ui = Ui_MainWindow2()
entrar_ui.setupUi(entrar)

error = QtWidgets.QMainWindow()
error_ui = Ui_MainWindow3()
error_ui.setupUi(error)

# Variable global para indicar si el programa debe seguir ejecutándose
seguir_ejecutando = True

# Crear la señal y conectarla a la ranura en Main.py
exit_signal = ExitSignal()

def gui_login():
    name = login_ui.lineEdit.text()
    password = login_ui.lineEdit_2.text()
    if len(name) == 0 or len(password) == 0:
        login_ui.label_5.setText("Ingrese todos los datos")
    elif name == "admin" and password == "1234":
        gui_entrar()
    else:
        gui_error()

def gui_entrar():
    login.hide()
    entrar.show()

def gui_error():
    login.hide()
    error.show()

def regresar_entrar():
    entrar.hide()
    login_ui.label_5.setText("")
    login.show()

def regresar_error():
    error.hide()
    login_ui.label_5.setText("")
    login.show()

def continuar():
    entrar.hide()
    global seguir_ejecutando
    seguir_ejecutando = False
    app.exit()

def salir():
    exit_signal.exit_program.emit()
    sys.exit()
    app.exit()

# Botones
login_ui.pushButton.clicked.connect(gui_login)
login_ui.pushButton_2.clicked.connect(salir)

entrar_ui.pushButton.clicked.connect(continuar)
entrar_ui.pushButton_2.clicked.connect(salir)

error_ui.pushButton.clicked.connect(regresar_error)
error_ui.pushButton_2.clicked.connect(salir)

# Ejecutable
if seguir_ejecutando:
    login.show()
    app.exec()