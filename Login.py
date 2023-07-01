from PyQt5 import QtWidgets, uic,QtCore
import sys

class ExitSignal(QtCore.QObject):
    exit_program = QtCore.pyqtSignal()

# Iniciar la aplicación
app = QtWidgets.QApplication([])

# Cargar archivos .ui
login = uic.loadUi("window1.ui")
entrar = uic.loadUi("window2.ui")
error = uic.loadUi("window3.ui")

# Variable global para indicar si el programa debe seguir ejecutándose
seguir_ejecutando = True

# Crear la señal y conectarla a la ranura en Main.py
exit_signal = ExitSignal()

def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()
    if len(name) == 0 or len(password) == 0:
        login.label_5.setText("Ingrese todos los datos")
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
    login.label_5.setText("")
    login.show()

def regresar_error():
    error.hide()
    login.label_5.setText("")
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
login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(salir)

entrar.pushButton.clicked.connect(continuar)
entrar.pushButton_2.clicked.connect(salir)

error.pushButton.clicked.connect(regresar_error)
error.pushButton_2.clicked.connect(salir)

# Ejecutable
if seguir_ejecutando:
    login.show()
    app.exec()
