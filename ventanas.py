# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window4.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from img import imagenes

class VentanaPrincipal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 250, 151, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../media/neutron/Nuevo vol/proyectos demi parami/MartLab/img/mot.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 40, 281, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 80, 281, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 120, 281, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 160, 281, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 200, 281, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 240, 281, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 280, 281, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 320, 281, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 360, 281, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 400, 281, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(30, 440, 281, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(610, 510, 101, 41))
        self.pushButton_Exit.setStyleSheet("background-color: rgb(192, 28, 40);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 170, 201, 231))
        self.label.setStyleSheet("image: url(:/img/motor.jpg);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Tension, Intensidad y Potencia"))
        self.pushButton_2.setText(_translate("MainWindow", "Intensidad Nominal"))
        self.pushButton_3.setText(_translate("MainWindow", "Cambio de Tension Nom de un motor 3F"))
        self.pushButton_4.setText(_translate("MainWindow", "Ventana Induccion de Flujo Magnetico"))
        self.pushButton_5.setText(_translate("MainWindow", "Flujo Magnetico de Motores 3F"))
        self.pushButton_6.setText(_translate("MainWindow", "Cambio de Frecuencia de la red Motores"))
        self.pushButton_7.setText(_translate("MainWindow", "Cambio de Polaridad Motor Trifasico"))
        self.pushButton_8.setText(_translate("MainWindow", "Calculos de Motores Monofasicos"))
        self.pushButton_9.setText(_translate("MainWindow", "Calculos Varios"))
        self.pushButton_10.setText(_translate("MainWindow", "Formas de probar el nucleo de motores"))
        self.pushButton_11.setText(_translate("MainWindow", "Peso del Cobre"))
        self.pushButton_Exit.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Salir</span></p></body></html>"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Salir"))

class VentanaTension(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 558)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 171, 23))
        self.radioButton.setChecked(True)
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 20, 161, 23))
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setAutoRepeat(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 250, 321, 251))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 131, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 60, 131, 20))
        self.label_3.setObjectName("label_3")
        self.text_IL = QtWidgets.QTextEdit(self.centralwidget)
        self.text_IL.setGeometry(QtCore.QRect(30, 90, 121, 31))
        self.text_IL.setObjectName("text_IL")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 90, 16, 31))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.text_IF = QtWidgets.QTextEdit(self.centralwidget)
        self.text_IF.setGeometry(QtCore.QRect(180, 90, 131, 31))
        self.text_IF.setObjectName("text_IF")
        self.text_EL = QtWidgets.QTextEdit(self.centralwidget)
        self.text_EL.setGeometry(QtCore.QRect(30, 170, 121, 31))
        self.text_EL.setObjectName("text_EL")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 121, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 140, 111, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 170, 16, 31))
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName("label_7")
        self.text_EF = QtWidgets.QTextEdit(self.centralwidget)
        self.text_EF.setGeometry(QtCore.QRect(180, 170, 131, 31))
        self.text_EF.setObjectName("text_EF")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 300, 121, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 390, 131, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 230, 91, 17))
        self.label_10.setObjectName("label_10")
        self.text_Phi = QtWidgets.QTextEdit(self.centralwidget)
        self.text_Phi.setGeometry(QtCore.QRect(140, 220, 41, 31))
        self.text_Phi.setObjectName("text_Phi")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 220, 67, 17))
        self.label_11.setObjectName("label_11")
        self.text_PF = QtWidgets.QTextEdit(self.centralwidget)
        self.text_PF.setGeometry(QtCore.QRect(40, 330, 141, 41))
        self.text_PF.setObjectName("text_PF")
        self.text_PL = QtWidgets.QTextEdit(self.centralwidget)
        self.text_PL.setGeometry(QtCore.QRect(40, 410, 141, 41))
        self.text_PL.setObjectName("text_PL")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 330, 151, 61))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(420, 40, 231, 131))
        self.label_12.setStyleSheet("color: rgb(87, 227, 137);\n"
"font-size: 18;")
        self.label_12.setObjectName("label_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 410, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButtonAtras = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAtras.setGeometry(QtCore.QRect(0, 490, 89, 25))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Conexion Triangulo"))
        self.radioButton_2.setText(_translate("MainWindow", "Conexion Estrella"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#57e389;\">Elige un tipo de conexion.</span></p><p align=\"center\"><span style=\" color:#57e389;\">Triangulo o Estrella</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Intensidad de Linea"))
        self.label_3.setText(_translate("MainWindow", "Intensidad de fase"))
        self.text_IL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">=</span></p></body></html>"))
        self.text_IF.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Tension de Linea"))
        self.label_6.setText(_translate("MainWindow", "Tension de fase"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">=</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Potencia de fase"))
        self.label_9.setText(_translate("MainWindow", "Potencia de linea"))
        self.label_10.setText(_translate("MainWindow", "Angulo ( φ ) :"))
        self.text_Phi.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">°</span></p></body></html>"))
        self.text_PF.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_PL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Calcular"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#33d17a;\">Elige un tipo de conexion.</span></p><p align=\"center\"><span style=\" color:#33d17a;\">Triangulo o Estrella</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Limpiar"))
        self.pushButtonAtras.setText(_translate("MainWindow", "Atras"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
