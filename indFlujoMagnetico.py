# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'indFlujoMagnetico.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 181, 31))
        self.label.setObjectName("label")
        self.label_u = QtWidgets.QLabel(self.centralwidget)
        self.label_u.setGeometry(QtCore.QRect(30, 70, 311, 17))
        self.label_u.setObjectName("label_u")
        self.label_N = QtWidgets.QLabel(self.centralwidget)
        self.label_N.setGeometry(QtCore.QRect(30, 110, 291, 17))
        self.label_N.setObjectName("label_N")
        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(30, 150, 291, 17))
        self.label_A.setObjectName("label_A")
        self.label_L = QtWidgets.QLabel(self.centralwidget)
        self.label_L.setGeometry(QtCore.QRect(30, 190, 291, 17))
        self.label_L.setObjectName("label_L")
        self.label_E = QtWidgets.QLabel(self.centralwidget)
        self.label_E.setGeometry(QtCore.QRect(30, 230, 281, 17))
        self.label_E.setObjectName("label_E")
        self.label_F = QtWidgets.QLabel(self.centralwidget)
        self.label_F.setGeometry(QtCore.QRect(30, 310, 291, 17))
        self.label_F.setObjectName("label_F")
        self.label_Kd = QtWidgets.QLabel(self.centralwidget)
        self.label_Kd.setGeometry(QtCore.QRect(30, 350, 291, 17))
        self.label_Kd.setObjectName("label_Kd")
        self.text_u = QtWidgets.QTextEdit(self.centralwidget)
        self.text_u.setGeometry(QtCore.QRect(340, 64, 131, 31))
        self.text_u.setObjectName("text_u")
        self.text_N = QtWidgets.QTextEdit(self.centralwidget)
        self.text_N.setGeometry(QtCore.QRect(340, 104, 131, 31))
        self.text_N.setObjectName("text_N")
        self.text_A = QtWidgets.QTextEdit(self.centralwidget)
        self.text_A.setGeometry(QtCore.QRect(340, 144, 131, 31))
        self.text_A.setObjectName("text_A")
        self.text_E = QtWidgets.QTextEdit(self.centralwidget)
        self.text_E.setGeometry(QtCore.QRect(340, 224, 131, 31))
        self.text_E.setObjectName("text_E")
        self.text_L = QtWidgets.QTextEdit(self.centralwidget)
        self.text_L.setGeometry(QtCore.QRect(340, 184, 131, 31))
        self.text_L.setObjectName("text_L")
        self.text_F = QtWidgets.QTextEdit(self.centralwidget)
        self.text_F.setGeometry(QtCore.QRect(340, 304, 131, 31))
        self.text_F.setObjectName("text_F")
        self.text_Kd = QtWidgets.QTextEdit(self.centralwidget)
        self.text_Kd.setGeometry(QtCore.QRect(340, 344, 131, 31))
        self.text_Kd.setObjectName("text_Kd")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 164, 71, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 64, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButtonAtras = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAtras.setGeometry(QtCore.QRect(0, 520, 89, 25))
        self.pushButtonAtras.setMouseTracking(True)
        self.pushButtonAtras.setStyleSheet("#pushButtonAtras{\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"#pushButtonAtras:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.pushButtonAtras.setCheckable(False)
        self.pushButtonAtras.setAutoRepeat(False)
        self.pushButtonAtras.setAutoExclusive(False)
        self.pushButtonAtras.setObjectName("pushButtonAtras")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 390, 231, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 440, 231, 17))
        self.label_3.setObjectName("label_3")
        self.label_Induccion = QtWidgets.QLabel(self.centralwidget)
        self.label_Induccion.setGeometry(QtCore.QRect(290, 390, 111, 17))
        self.label_Induccion.setStyleSheet("<html><head/><body><p align=\"right\">-</p></body></html>")
        self.label_Induccion.setObjectName("label_Induccion")
        self.label_EspirasF = QtWidgets.QLabel(self.centralwidget)
        self.label_EspirasF.setGeometry(QtCore.QRect(290, 440, 111, 17))
        self.label_EspirasF.setObjectName("label_EspirasF")
        self.text_I = QtWidgets.QTextEdit(self.centralwidget)
        self.text_I.setGeometry(QtCore.QRect(340, 264, 131, 31))
        self.text_I.setObjectName("text_I")
        self.label_F_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_F_2.setGeometry(QtCore.QRect(30, 270, 291, 17))
        self.label_F_2.setObjectName("label_F_2")
        self.label_mensaje = QtWidgets.QLabel(self.centralwidget)
        self.label_mensaje.setGeometry(QtCore.QRect(490, 130, 171, 21))
        self.label_mensaje.setText("")
        self.label_mensaje.setObjectName("label_mensaje")
        self.label_gauss = QtWidgets.QLabel(self.centralwidget)
        self.label_gauss.setGeometry(QtCore.QRect(410, 390, 91, 17))
        self.label_gauss.setText("")
        self.label_gauss.setObjectName("label_gauss")
        self.label_espiras = QtWidgets.QLabel(self.centralwidget)
        self.label_espiras.setGeometry(QtCore.QRect(410, 440, 91, 17))
        self.label_espiras.setText("")
        self.label_espiras.setObjectName("label_espiras")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Ingrese los datos:</span></p></body></html>"))
        self.label_u.setText(_translate("MainWindow", "Permeabilidad magnética del nucleo (H/m):"))
        self.label_N.setText(_translate("MainWindow", "Número de espiras en el conductor:"))
        self.label_A.setText(_translate("MainWindow", "<html><head/><body><p>Area transversal del conductor (cm<span style=\" vertical-align:super;\">2</span>):</p></body></html>"))
        self.label_L.setText(_translate("MainWindow", "Longitud del conductor (cm):"))
        self.label_E.setText(_translate("MainWindow", "Tension de linea (Voltios):"))
        self.label_F.setText(_translate("MainWindow", "Frecuencia (Hz):"))
        self.label_Kd.setText(_translate("MainWindow", "Kd:"))
        self.pushButton_2.setText(_translate("MainWindow", "Limpiar"))
        self.pushButton.setText(_translate("MainWindow", "Calcular"))
        self.pushButtonAtras.setText(_translate("MainWindow", "Atras"))
        self.label_2.setText(_translate("MainWindow", "Induccion del flujo magnetico (B):"))
        self.label_3.setText(_translate("MainWindow", "Conductores de bobina por fase:"))
        self.label_Induccion.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">-</p></body></html>"))
        self.label_EspirasF.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">-</p></body></html>"))
        self.label_F_2.setText(_translate("MainWindow", "Corriente (Amperios):"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
