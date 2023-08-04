import sys
import math
import pandas as pd 
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QDialog,QFileDialog, QMainWindow, QTableWidgetItem, QTableWidget, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPalette, QColor
import Login
from recursos_rc import *
import ventanas

def exit_program():
    main.close()

exit_signal = Login.ExitSignal()
exit_signal.exit_program.connect(exit_program)

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = ventanas.VentanaPrincipal()  # Crear una instancia de la clase Ui_MainWindow
        self.ui.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Main Window")
        self.ui.pushButton_Exit.clicked.connect(self.Salir)
        self.ui.pushButton.clicked.connect(self.abrirVentanaTension)
        self.ui.pushButton_2.clicked.connect(self.abrirVentanaIntNominal)
        self.ui.pushButton_3.clicked.connect(self.abrirVentanaCambiarTensionNominalMotor)
        self.ui.pushButton_4.clicked.connect(self.VentanaIndFlujoMagnetico)
        self.ui.pushButton_5.clicked.connect(self.TablaFlujoMagneticoMotores3F)
        self.ui.pushButton_6.clicked.connect(self.CambioDeFrecuenciaMotor)
        self.ui.pushButton_7.clicked.connect(self.CambioDePolaridad)
        self.ui.pushButton_8.clicked.connect(self.motorMonofasicoCalc)
        self.ui.pushButton_9.clicked.connect(self.calculosVarios)
        self.ui.pushButton_10.clicked.connect(self.probarNucleo)
        self.ui.pushButton_11.clicked.connect(self.pesoCobre)

         
    def Salir(self):
        self.close()

    def abrirVentanaTension(self):
        self.hide()
        otraventana=VentanaTension(self)
        otraventana.show()
        
    def abrirVentanaIntNominal(self):
        self.hide()
        otraventana=VentanaIntNominal(self)
        otraventana.show()

    def abrirVentanaCambiarTensionNominalMotor(self):
        self.hide()
        otraventana=VentanaCambiarTensionNominalMotor(self)
        otraventana.show()  

    def VentanaIndFlujoMagnetico(self):
        self.hide()
        otraventana=VentanaIndFlujoMagnetico(self)
        otraventana.show()

    def TablaFlujoMagneticoMotores3F(self):
        self.hide()
        otraventana=TablaFlujoMagneticoMotores3F(self)
        otraventana.show()

    def CambioDeFrecuenciaMotor(self):
        self.hide()
        otraventana=CambioDeFrecuenciaMotor(self)
        otraventana.show() 
    
    def CambioDePolaridad(self):
        self.hide()
        otraventana=CambioDePolaridad(self)
        otraventana.show() 

    def motorMonofasicoCalc(self):
        self.hide()
        otraventana=motorMonofasicoCalc(self)
        otraventana.show() 
    
    def calculosVarios(self):
        self.hide()
        otraventana=calculosVarios(self)
        otraventana.show()

    def probarNucleo(self):
        self.hide()
        otraventana=probarNucleo(self)
        otraventana.show()

    def pesoCobre(self):
        self.hide()
        otraventana=pesoCobre(self)
        otraventana.show()

class VentanaTension(QMainWindow):
    def __init__(self, parent=None):
        #
        #
        super(VentanaTension, self).__init__(parent)
        self.ui1 = ventanas.VentanaTension()
        self.ui1.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Tension, Intensidad y Potencia")
        #loadUi('window5.ui', self)
        #self.setWindowTitle("Tension, Intensidad y Potencia")
        #
        self.ui1.label_12.setText("")
        self.radio_value()
        self.ui1.radioButton.clicked.connect(self.triangulo)
        self.ui1.radioButton_2.clicked.connect(self.estrella)
        self.ui1.pushButton.clicked.connect(self.radio_value)
        self.ui1.pushButton_2.clicked.connect(self.limpiar)
        self.ui1.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)


    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
        

    def radio_value(self):
        if self.ui1.radioButton.isChecked():
            self.calcularTriangulo()
        elif self.ui1.radioButton_2.isChecked():
            self.calcularEstrella()
        else:
            print("err")
    def limpiar(self):
        self.ui1.text_IL.setText("")
        self.ui1.text_IF.setText("")
        self.ui1.text_EL.setText("")
        self.ui1.text_EF.setText("")
        self.ui1.text_Phi.setText("")
        self.ui1.text_PL.setText("")
        self.ui1.text_PF.setText("")
        self.ui1.label_12.setText("Limpio!")
        
    def triangulo(self):
        pix = QPixmap(":/img/triangulo.png")
        self.ui1.label_2.setPixmap(pix)
        #self.pushButton.clicked.connect(self.calcularTriangulo)

    def estrella(self):
        pix = QPixmap(":/img/estrella.png")
        self.ui1.label_2.setPixmap(pix)
        #self.pushButton.clicked.connect(self.calcularEstrella)
              
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def calcularTriangulo(self):
        print("estas en triangulo")
        i_l=i_f=e_l=e_f=phi=p_f=p_l=""
        i_l = str(self.ui1.text_IL.toPlainText())
        i_f = str(self.ui1.text_IF.toPlainText())
        e_l = str(self.ui1.text_EL.toPlainText())
        e_f = str(self.ui1.text_EF.toPlainText())
        phi = str(self.ui1.text_Phi.toPlainText())
        p_f = str(self.ui1.text_IF.toPlainText())
        p_l = str(self.ui1.text_IF.toPlainText())
        if i_l != "" and i_f == "":
            print("entraste a t_i_f")
            i_l=float(i_l)
            result= VentanaTension.t_IF(i_l)
            i_f=float("%.4f" % result)
            self.ui1.text_IF.setText(str(i_f))
            self.ui1.label_12.setText("Calculado!")
        elif i_f != "" and i_l == "":
            print("entraste a t_i_l")
            i_f = float(i_f)
            result= VentanaTension.t_IL(i_f)
            i_l=float("%.4f" % result)
            self.ui1.text_IL.setText(str(i_l))
            self.ui1.label_12.setText("Calculado!")
        elif i_l == "" and i_f == "":
            self.ui1.label_12.setText("Calculado!")
        else:    
            self.ui1.label_12.setText("Limpie! no calculo...")

        if e_l != "" and e_f == "":
            print("entraste a t_e_f")
            e_l=float(e_l)
            result= VentanaTension.t_EF(e_l)
            e_f=float("%.4f" % result)
            self.ui1.text_EF.setText(str(e_f))
            self.ui1.label_12.setText("Calculado!")  
        elif e_f != "" and e_l == "":
            print("entraste a t_e_l")
            e_f = float(e_f)
            result= VentanaTension.t_EL(e_f)
            e_l=float("%.4f" % result)
            self.ui1.text_EL.setText(str(e_l))
            self.ui1.label_12.setText("Calculado!")
        elif e_l == "" and e_f == "":
            self.ui1.label_12.setText("Esperando...")
        else:    
            self.ui1.label_12.setText("Limpie! no calculo...")
            
        if phi != "":
            phi = float(phi)
            phi = phi*math.pi/180
            p_f = VentanaTension.p_fase(e_f,i_f,phi)
            p_l = VentanaTension.p_fase(e_l,i_l,phi)
            p_f=float("%.4f" % p_f)
            p_l=float("%.4f" % p_l)
            self.ui1.text_PF.setText(str(p_f))
            self.ui1.text_PL.setText(str(p_l))
            self.ui1.label_12.setText("Calculado!")
        
    def calcularEstrella(self):
        print("estas en estrella")
        i_l=i_f=e_l=e_f=phi=p_f=p_l=""
        i_l = str(self.ui1.text_IL.toPlainText())
        i_f = str(self.ui1.text_IF.toPlainText())
        e_l = str(self.ui1.text_EL.toPlainText())
        e_f = str(self.ui1.text_EF.toPlainText())
        phi = str(self.ui1.text_Phi.toPlainText())
        p_f = str(self.ui1.text_IF.toPlainText())
        p_l = str(self.ui1.text_IF.toPlainText())
        if i_l != "" and i_f == "":
            print("entraste a e_i_f")
            i_l=float(i_l)
            result= VentanaTension.e_IF(i_l)
            i_f=float("%.4f" % result)
            self.ui1.text_IF.setText(str(i_f))
            self.ui1.label_12.setText("Calculado!")
        elif i_f != "" and i_l == "":
            print("entraste a e_i_l")
            i_f = float(i_f)
            result= VentanaTension.e_IL(i_f)
            i_l=float("%.4f" % result)
            self.ui1.text_IL.setText(str(i_l))
            self.ui1.label_12.setText("Calculado!")
        elif i_l == "" and i_f == "":
            print("entraste a e_i_f")
            self.ui1.label_12.setText("Calculado!")
        else:    
            self.ui1.label_12.setText("Limpie! no calculo...")

        if e_l != "" and e_f == "":
            print("entraste a e_e_f")
            e_l=float(e_l)
            result= VentanaTension.e_EF(e_l)
            e_f=float("%.4f" % result)
            self.ui1.text_EF.setText(str(e_f))
            self.ui1.label_12.setText("Calculado!")  
        elif e_f != "" and e_l == "":
            print("entraste a e_e_l")
            e_f = float(e_f)
            result= VentanaTension.e_EL(e_f)
            e_l=float("%.4f" % result)
            self.ui1.text_EL.setText(str(e_l))
            self.ui1.label_12.setText("Calculado!")
        elif e_l == "" and e_f == "":
            print("entraste a e_e_f")
            self.ui1.label_12.setText("Calculado!")
        else:    
            self.ui1.label_12.setText("Limpie! no calculo...")
            
        if phi != "":
            phi = float(phi)
            phi = phi*math.pi/180
            p_f = VentanaTension.p_fase(e_f,i_f,phi)
            p_l = VentanaTension.p_fase(e_l,i_l,phi)
            p_f=float("%.4f" % p_f)
            p_l=float("%.4f" % p_l)
            self.ui1.text_PF.setText(str(p_f))
            self.ui1.text_PL.setText(str(p_l))

    def t_IL(int_fase):
        int_linea=int_fase*1.732
        return int_linea
    def t_EL(ten_fase):
        ten_linea=ten_fase
        return ten_linea     
    def t_IF(int_linea):
        int_fase=int_linea/1.732
        return int_fase
    def t_EF(ten_linea):
        ten_fase=ten_linea
        return ten_fase
    def p_fase(ten_fase, int_fase, angulo):
        pot_fase = ten_fase*int_fase*math.cos(angulo)
        return pot_fase
    def p_linea(ten_linea, int_linea, angulo):
        pot_linea = ten_linea*int_linea*(3**(0.5))*math.cos(angulo)
        return pot_linea
    def e_IL(int_fase):
        int_linea=int_fase
        return int_linea
    def e_EL(ten_fase):
        ten_linea=ten_fase*(3**(0.5))
        return ten_linea     
    def e_IF(int_linea):
        int_fase=int_linea
        return int_fase
    def e_EF(ten_linea):
        ten_fase=ten_linea/(3**(0.5))
        return ten_fase        
class VentanaIntNominal(QMainWindow):
    
    def __init__(self, parent=None):
        super(VentanaIntNominal, self).__init__(parent)
        self.ui2 = ventanas.VentanaIntNominal()
        self.ui2.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Intensidad Nominal")
        #
        self.ui2.pushButton.clicked.connect(self.calcular)
        self.ui2.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.ui2.pushButton_2.clicked.connect(self.limpiar)
    
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def limpiar(self):
        self.ui2.text_IN.setText("")
        self.ui2.text_EN.setText("")
        self.ui2.text_Phi.setText("")
        self.ui2.text_EF.setText("")
        self.ui2.text_I.setText("")
        self.ui2.text_E.setText("")
    def calcular(self):
        i_n = str(self.ui2.text_IN.toPlainText())
        e_n = str(self.ui2.text_EN.toPlainText())
        phi = str(self.ui2.text_Phi.toPlainText())
        e_f = str(self.ui2.text_EF.toPlainText())
        i = str(self.ui2.text_I.toPlainText())
        e = str(self.ui2.text_E.toPlainText())
        if i_n!="" and e_n!="" and phi!="" and e_f!="" and i!="" and e!="":
            i_n = float(self.ui2.text_IN.toPlainText())
            e_n = float(self.ui2.text_EN.toPlainText())
            phi = float(self.ui2.text_Phi.toPlainText())
            e_f = float(self.ui2.text_EF.toPlainText())
            i = float(self.ui2.text_I.toPlainText())
            e = float(self.ui2.text_E.toPlainText())
            phi = phi*math.pi/180
            hp = i_n*e_n*math.cos(phi)*e_f*1.73/746
            kw = i*e*math.cos(phi)*(3**(1/2))/1000
            int_nom=hp*746/(e*math.cos(phi)*(3**(1/2))*e_f)
            hp = float("%.4f" % hp)
            kw = float("%.4f" % kw)
            int_nom = float("%.4f" % int_nom)
            self.ui2.label_HP.setText(str(hp))
            self.ui2.label_KW.setText(str(kw))
            self.ui2.label_IntNom.setText(str(int_nom))
            self.ui2.label_mensaje.setStyleSheet("color:green;")
            self.ui2.label_mensaje.setText("Calculado!")
        else:
            self.ui2.label_mensaje.setStyleSheet("color:red")
            self.ui2.label_mensaje.setText("No calculado... Faltan Datos")
class VentanaCambiarTensionNominalMotor(QMainWindow):
     def __init__(self, parent=None):
        #
        super(VentanaCambiarTensionNominalMotor, self).__init__(parent)
        self.ui3 = ventanas.VentanaCambiarTensionNominalMotor()
        self.ui3.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Cambio de Tension Nominal de motor 3F")
        #
        self.ui3.pushButton.clicked.connect(self.calcular)
        self.ui3.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.ui3.pushButton_2.clicked.connect(self.limpiar)

     def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
     def limpiar(self):
        self.ui3.text_NumPriEsp.setText("")
        self.ui3.text_CapAnt.setText("")
        self.ui3.text_SecCobAnt.setText("")
        self.ui3.text_TenRedAnt.setText("")
        self.ui3.text_TenRedNue.setText("")
        self.ui3.text_VueRanAnt.setText("")
        self.ui3.label_NumEspNue.setText("-")
        self.ui3.label_VueRanNue.setText("-")
        self.ui3.label_SecAlaNue.setText("-")
        self.ui3.label_CapNue.setText("-")
        self.ui3.label_mensaje.setStyleSheet("color:black;")
        self.ui3.label_mensaje.setText("")

     def calcular(self):
         v_r_a= self.ui3.text_VueRanAnt.toPlainText()
         e_n= self.ui3.text_TenRedNue.toPlainText()
         e_a= self.ui3.text_TenRedAnt.toPlainText()
         s_a_a= self.ui3.text_SecCobAnt.toPlainText()
         c_p= self.ui3.text_CapAnt.toPlainText()
         n_p_e= self.ui3.text_NumPriEsp.toPlainText()
         if e_a!="" and e_n!="":
            if v_r_a!="":   
                v_r_n = VentanaCambiarTensionNominalMotor.calculoVueltasRanuraNueva(v_r_a,e_n,e_a)
                v_r_n = float("%.4f" % v_r_n)
                v_r_n = str(v_r_n)
                self.ui3.label_VueRanNue.setText(v_r_n)
                self.ui3.label_mensaje.setStyleSheet("color:black;")
                self.ui3.label_mensaje.setText("Calculado!")
                if s_a_a!="":
                    s_a_n = VentanaCambiarTensionNominalMotor.calculoSeccionAlamNuevo(s_a_a,v_r_a,v_r_n)
                    s_a_n = float("%.4f" % s_a_n)
                    s_a_n = str(s_a_n)
                    self.ui3.label_SecAlaNue.setText(s_a_n)
                    self.ui3.label_mensaje.setStyleSheet("color:black;")
                    self.ui3.label_mensaje.setText("Calculado!")
                else:
                    self.ui3.label_mensaje.setStyleSheet("color:black;")
                    self.ui3.label_mensaje.setText("Calculo parcial... complete seccion del \n alambre para obtener la nueva seccion")
            else:
                self.ui3.label_mensaje.setStyleSheet("color:black;")
                self.ui3.label_mensaje.setText("Datos insuficientes! complete las vueltas de ranura antigua")
                
            if c_p!="":
                c_n = VentanaCambiarTensionNominalMotor.calculoNuevaCapacidad(e_a,c_p,e_n)
                c_n = float("%.4f" % c_n)
                c_n = str(c_n)
                self.ui3.label_CapNue.setText(c_n)
                self.ui3.label_mensaje.setStyleSheet("color:black;")
                self.ui3.label_mensaje.setText("Calculado!")
            
            if n_p_e!="":
                n_e_n = VentanaCambiarTensionNominalMotor.calculoNUmeroEspirasNuevo(n_p_e,e_n,e_a)
                n_e_n = float("%.4f" % n_e_n)
                n_e_n = str(n_e_n)
                self.ui3.label_NumEspNue.setText(n_e_n)
                self.ui3.label_mensaje.setStyleSheet("color:black;")
                self.ui3.label_mensaje.setText("Calculado!")
         else:
            self.ui3.label_mensaje.setStyleSheet("color:red;")
            self.ui3.label_mensaje.setText("Datos insuficientes!")

     def calculoVueltasRanuraNueva(v_r_a,e_n,e_a):
         v_r_a=float(v_r_a)
         e_n=float(e_n)
         e_a=float(e_a)
         result=v_r_a*e_n/e_a
         return result
     
     def calculoSeccionAlamNuevo(s_a_a,v_r_a,v_r_n):
         s_a_a=float(s_a_a)
         v_r_a=float(v_r_a)
         v_r_n=float(v_r_n)
         result=s_a_a*v_r_a/v_r_n
         return result
     
     def calculoNuevaCapacidad(e_a,c_p,e_n):
         e_a=float(e_a)
         c_p=float(c_p)
         e_n=float(e_n)
         result=e_a*c_p/e_n
         return result
     
     def calculoNUmeroEspirasNuevo(n_p_e,e_n,e_a):
         n_p_e=float(n_p_e)
         e_n=float(e_n)
         e_a=float(e_a)
         result=e_n*n_p_e/e_a
         return result
class VentanaIndFlujoMagnetico(QMainWindow):
    def __init__(self, parent=None):
        
        #
        super(VentanaIndFlujoMagnetico, self).__init__(parent)
        self.ui4 = ventanas.VentanaIndFlujoMagnetico()
        self.ui4.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Induccion de Flujo Magnetico")
        #
        self.ui4.pushButton.clicked.connect(self.calcular)
        self.ui4.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.ui4.pushButton_2.clicked.connect(self.limpiar)

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def limpiar(self):
        self.ui4.text_u.setText("")
        self.ui4.text_N.setText("")
        self.ui4.text_A.setText("")
        self.ui4.text_L.setText("")
        self.ui4.text_E.setText("")
        self.ui4.text_I.setText("")
        self.ui4.text_F.setText("")
        self.ui4.text_Kd.setText("")
        self.ui4.label_Induccion.setText("-")
        self.ui4.label_EspirasF.setText("-")
        self.ui4.label_mensaje.setStyleSheet("color: black; background-color:transparent;")
        self.ui4.label_mensaje.setText("limpio!")
        self.ui4.label_gauss.setText("")
        self.ui4.label_espiras  .setText("")

    def calcular(self):
        u = self.ui4.text_u.toPlainText()
        n = self.ui4.text_N.toPlainText()
        a = self.ui4.text_A.toPlainText()
        l = self.ui4.text_L.toPlainText()
        e = self.ui4.text_E.toPlainText()
        i = self.ui4.text_I.toPlainText()
        f = self.ui4.text_F.toPlainText()
        kd = self.ui4.text_Kd.toPlainText()
        

        if u !="" and n!="" and a!="" and l!="" and e!="" and i!="" and f!="" and kd!="":
            u=float(u)
            n=float(n)
            a=float(a) #cm2
            a=a/10**4  #m2
            l=float(l) #centimetros
            l = l/100  #metros
            e=float(e)
            i=float(i)
            f=float(f)
            kd=float(kd)

            ind = VentanaIndFlujoMagnetico.induccionFlujoMagnetico(u,n,a,l,i)
            flujo = VentanaIndFlujoMagnetico.flujoMagnetico(a,l,ind)
            cond = VentanaIndFlujoMagnetico.conductoresBobinaFase(e,f,kd,flujo)
            self.ui4.label_mensaje.setStyleSheet("color: black; background-color:transparent;")
            self.ui4.label_mensaje.setText("calculado!")
            self.ui4.label_Induccion.setAlignment(QtCore.Qt.AlignRight)
            self.ui4.label_EspirasF.setAlignment(QtCore.Qt.AlignRight)
            self.ui4.label_Induccion.setText(str(ind))
            self.ui4.label_EspirasF.setText(str(cond))
            self.ui4.label_gauss.setText("[Gauss]")
            self.ui4.label_espiras.setText("[Espiras]")

        else:
            self.ui4.label_mensaje.setStyleSheet("color:red; background-color:yellow;")
            self.ui4.label_mensaje.setText("Faltan datos!")
            self.ui4.label_gauss.setText("")
            self.ui4.label_gauss.setText("")


    def induccionFlujoMagnetico(u,n,a,l,i):

        result = u*n*i/l
        result = float("%.2f" %result)
        return result
    def flujoMagnetico(a,l,ind):
        result =2*ind*a*l
        result = float("%.2f" %result)
        return result
    def conductoresBobinaFase(e,f,kd,flujo):
        result = 472*e*(10**5)/(f*kd*flujo)
        result = float("%.2f" %result)
        return result
class TablaFlujoMagneticoMotores3F(QMainWindow):
    def __init__(self, parent=None):
        #
        super(TablaFlujoMagneticoMotores3F, self).__init__(parent)
        self.ui5 = ventanas.TablaFlujoMagneticoMotores3F()
        self.ui5.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Tabla de Flujo Magnnetico Motores 3F")
        #
        self.ui5.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)   
        self.ui5.pushButton.clicked.connect(self.mostrar_tabla)

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    """ def crear_tabla(self):
        try:
            direccion = '/home/neutron/Documentos/Proyectos/2/tabla flujo magnetico en motor 3f.xlsx'
            df = pd.read_excel(direccion, sheet_name='Hoja1')
            columnas = list(df.columns)
            df_fila = df.to_numpy().tolist()
            x = len(columnas)
            y = len(df_fila)
        except ValueError:
            QMessageBox.about(self,'Informacion', 'formato incorrecto')
            return None
        except FileNotFoundError:
            QMessageBox.about(self,'Informacion', 'El archivo esta \n malogrado')
            return None
        
        self.ui5.table.setRowCount(y)
        self.ui5.table.setColumnCount(x)
        self.ui5.table.resize(770, 480)

        for j in range(x):
            encabezado = QtWidgets.QTableWidgetItem(columnas[j])
            self.ui5.table.setHorizontalHeaderItem(j,encabezado)
            for i in range(y):
                dato = str(df_fila[i][j])
                if dato == 'nan':
                    dato=''
                self.ui5.table.setItem(i,j,QTableWidgetItem(dato)) """
    
    def mostrar_tabla(self):
        pix = QPixmap("img/tablaFlujoMagneticoM3F.png").scaled(450, 480)
        
        self.ui5.label.resize(450,480)
        self.ui5.label.setPixmap(pix)

class CambioDeFrecuenciaMotor(QMainWindow):
    def __init__(self, parent=None):
        #
        super(CambioDeFrecuenciaMotor, self).__init__(parent)
        self.ui6 = ventanas.CambioDeFrecuenciaMotor()
        self.ui6.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Cambio de Frecuencia de Motor")
        self.ui6.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.ui6.pushButtonLimpiar.clicked.connect(self.limpiar)
        self.ui6.pushButton.clicked.connect(self.calcular)


    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def limpiar(self):
        self.ui6.textPotAnt.setText("")
        self.ui6.textFreAnt.setText("")
        self.ui6.textRanEstAnt.setText("")
        self.ui6.textSecCobAnt.setText("")
        self.ui6.textNueFre.setText("")
        self.ui6.label_PotNue.setText("")
        self.ui6.label_RanEstNue.setText("")
        self.ui6.label_SecCobNue.setText("")
        self.ui6.label_7.setText("")


    def calcular(self):
        potAnt = self.ui6.textPotAnt.toPlainText()
        frecAnt = self.ui6.textFreAnt.toPlainText()
        ranEstAnt = self.ui6.textRanEstAnt.toPlainText()
        secCobAnt = self.ui6.textSecCobAnt.toPlainText()
        nueFrec = self.ui6.textNueFre.toPlainText()
        secCobAnt = str(secCobAnt)
        potNue = CambioDeFrecuenciaMotor.calcularPot(nueFrec,frecAnt,potAnt)
        ranEstNue = CambioDeFrecuenciaMotor.calcularRan(nueFrec,frecAnt,ranEstAnt)
        if secCobAnt != "":
            secCobNue = CambioDeFrecuenciaMotor.calcularSec(nueFrec,frecAnt,secCobAnt)
            secCobNue = float("%.4f" % secCobNue)
            secCobNue = str(secCobNue)
            potNue = float("%.4f" % potNue)
            ranEstNue = float("%.4f" % ranEstNue)
            potNue = str(potNue)
            ranEstNue = str(ranEstNue)
            self.ui6.label_PotNue.setText(potNue)
            self.ui6.label_7.setText("HP")
            self.ui6.label_RanEstNue.setText(ranEstNue)
            self.ui6.label_SecCobNue.setText(secCobNue)

        else:
            secCobNue = ""    
            potNue = float("%.4f" % potNue)
            ranEstNue = float("%.4f" % ranEstNue)
            potNue = str(potNue)
            ranEstNue = str(ranEstNue)
            self.ui6.label_PotNue.setText(potNue)
            self.ui6.label_7.setText("HP")
            self.ui6.label_RanEstNue.setText(ranEstNue)
            self.ui6.label_SecCobNue.setText(secCobNue)


    def calcularPot(nueFrec,frecAnt,potAnt):
        nueFrec=float(nueFrec)
        frecAnt =float(frecAnt)
        potAnt=float(potAnt)
        result=potAnt*frecAnt/nueFrec
        return result 

    def calcularRan(nueFrec,frecAnt,ranEstAnt):
        nueFrec=float(nueFrec)
        frecAnt =float(frecAnt)
        ranEstAnt=float(ranEstAnt)
        result=ranEstAnt*frecAnt/nueFrec
        return result  
    
    def calcularSec(nueFrec,frecAnt,secCobAnt):
        nueFrec=float(nueFrec)
        frecAnt =float(frecAnt)
        secCobAnt=float(secCobAnt)
        result=secCobAnt*frecAnt/nueFrec
        return result
    
class CambioDePolaridad(QMainWindow):
    def __init__(self, parent=None):
        super(CambioDePolaridad, self).__init__(parent)
        self.ui7 = ventanas.CambioDePolaridad()
        self.ui7.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Cambio de Polaridad")
        self.ui7.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.ui7.pushButton.clicked.connect(self.calcular)
        self.ui7.pushButtonLimpiar.clicked.connect(self.limpiar)
        self.ui7.pushButton_2.clicked.connect(self.abrirVentana_2)
         

    def abrirVentana_2(self):
        self.hide()
        otraventana=CambioDePolaridad_2(self)
        otraventana.show()

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def limpiar(self):
        self.ui7.textEdit_DenCorAnt.setText("")
        self.ui7.textEdit_2_FacBobAnt.setText("")
        self.ui7.textEdit_3_IndAntDie.setText("")
        self.ui7.textEdit_4_PotAnt.setText("")
        self.ui7.textEdit_5_DenCorNue.setText("")
        self.ui7.textEdit_6_FacBobNue.setText("")
        self.ui7.textEdit_7_IndNueDie.setText("")
        self.ui7.label_PotNue.setText("")

    def calcular(self):
        denCorAnt = self.ui7.textEdit_DenCorAnt.toPlainText()
        facBobAnt = self.ui7.textEdit_2_FacBobAnt.toPlainText()
        indAntDie = self.ui7.textEdit_3_IndAntDie.toPlainText()
        potAnt = self.ui7.textEdit_4_PotAnt.toPlainText()
        denCorNue = self.ui7.textEdit_5_DenCorNue.toPlainText()
        facBobNue = self.ui7.textEdit_6_FacBobNue.toPlainText()
        indNueDie = self.ui7.textEdit_7_IndNueDie.toPlainText()

        denCorAnt=float(denCorAnt)
        facBobAnt=float(facBobAnt)
        indAntDie=float(indAntDie)
        potAnt=float(potAnt)
        denCorNue=float(denCorNue)
        facBobNue=float(facBobNue)
        indNueDie=float(indNueDie)


        potNue = potAnt*denCorNue*facBobNue*indNueDie/(denCorAnt*facBobAnt*indAntDie)
        potNue = float("%.4f" %potNue)
        potNue = str(potNue)
        self.ui7.label_PotNue.setText(potNue)

class CambioDePolaridad_2(QMainWindow):
    def __init__(self, parent=None):
        super(CambioDePolaridad_2, self).__init__(parent)
        self.ui71 = ventanas.CambioDePolaridad_2()
        self.ui71.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Cambio de Polaridad 2")
        self.ui71.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.ui71.pushButton.clicked.connect(self.calcular)
        #self.pushButtonLimpiar.clicked.connect(self.limpiar)
        

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def calcular(self):
        numRan = self.ui71.textEdit_1_NumRan.toPlainText()
        numPol = self.ui71.textEdit_2_NumPol.toPlainText()
        numRan = float(numRan)
        numPol = float(numPol)
        yc = numRan/numPol
        yc = float("%.4f" %yc)
        y = (5/6)*yc
        y = float("%.4f" %y)
        
        angElec = 360*numPol/(2*numRan)
        angElec = float("%.4f" %angElec)
        
        Kd = math.sin(numRan*angElec/(2*numPol))
        Kd = float("%.4f" %Kd)
        
        Kp = math.sin(y*90/yc)
        Kp = float("%.4f" %Kp)

        Kw = Kd*Kp
        Kw = float("%.4f" %Kw)

        y = str(y)
        yc = str(yc)
        angElec = str(angElec)
        Kd = str(Kd)
        Kp = str(Kp)
        Kw = str(Kw)
        self.ui71.textEdit_Y.setText(y)
        self.ui71.textEdit_Yc.setText(yc)
        self.ui71.textEdit_AngEle.setText(angElec)
        self.ui71.textEdit_Kd.setText(Kd)
        self.ui71.textEdit_Kp.setText(Kp)
        self.ui71.textEdit_Kw.setText(Kw)

class motorMonofasicoCalc(QMainWindow):
    def __init__(self, parent=None):
        super(motorMonofasicoCalc, self).__init__(parent)
        self.ui8 = ventanas.motorMonofasicoCalc()
        self.ui8.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Calculos Motor Monofasico")

        self.ui8.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.ui8.pushButtonLimpiar.clicked.connect(self.limpiar)
        self.ui8.pushButton.clicked.connect(self.calNumEsp)
        self.ui8.pushButton_2.clicked.connect(self.calSecMayNue)
        self.ui8.pushButton_3.clicked.connect(self.calCapacidad)
        self.ui8.pushButton_4.clicked.connect(self.calSecNue2)

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def limpiar(self):
        self.ui8.textTenPrim.setText("")
        self.ui8.textTenNue.setText("")
        self.ui8.textEspPrim.setText("")
        self.ui8.label_EspNue.setText("")
        self.ui8.textSeccPrim.setText("")
        self.ui8.label_SeccNue.setText("")
        self.ui8.textCapPrim.setText("")
        self.ui8.label_CapNue.setText("")
        self.ui8.textVelPrim.setText("")
        self.ui8.textVelNue.setText("")
        self.ui8.textSeccPrim_2.setText("")
        self.ui8.label_SeccNue_2.setText("")

    def calNumEsp(self):
        tenPrim = float(self.ui8.textTenPrim.toPlainText())
        tenNue = float(self.ui8.textTenNue.toPlainText())
        espPrim = float(self.ui8.textEspPrim.toPlainText())

        espNue = espPrim*tenNue/tenPrim
        espNue = str(float("%.2f" %espNue))
        
        self.ui8.label_EspNue.setText(espNue)
        

    def calSecMayNue(self):
        tenPrim = float(self.ui8.textTenPrim.toPlainText())
        tenNue = float(self.ui8.textTenNue.toPlainText())
        secPrim = float(self.ui8.textSeccPrim.toPlainText())
        
        secNue = secPrim*tenNue/tenPrim
        secNue = str(float("%.2f" %secNue))

        self.ui8.label_SeccNue.setText(secNue) 

    def calCapacidad(self):
        tenPrim = float(self.ui8.textTenPrim.toPlainText())
        tenNue = float(self.ui8.textTenNue.toPlainText())
        capPrim = float(self.ui8.textCapPrim.toPlainText())
        
        capNue = capPrim*tenNue/tenPrim
        capNue = str(float("%.4f" %capNue))

        self.ui8.label_CapNue.setText(capNue)


    def calSecNue2(self):
        velPrim = float(self.ui8.textVelPrim.toPlainText())
        velNue = float(self.ui8.textVelNue.toPlainText())
        secPrim2 = float(self.ui8.textSeccPrim_2.toPlainText())
        
        secNue2 = secPrim2*velNue/velPrim
        secNue2 = str(float("%.4f" %secNue2))

        self.ui8.label_SeccNue_2.setText(secNue2)

class calculosVarios(QMainWindow):
    def __init__(self,parent=None):
        super(calculosVarios, self).__init__(parent)
        self.ui9 = ventanas.calculosVarios()
        self.ui9.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Calculos Varios")
        self.ui9.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.ui9.pushButton.clicked.connect(self.seleccion)
    
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def  seleccion(self):
        #primera seleccion
        if self.ui9.radioButton_DC.isChecked():
            sel1=1
        elif self.ui9.radioButton_ACM.isChecked():
            sel1=2
        elif self.ui9.radioButton_ACB.isChecked():
            sel1=3
        elif self.ui9.radioButton_ACT.isChecked():
            sel1=4
        else:
            sel1=0
            print("err")
        #segunda seleccion
        if self.ui9.radioButton_A_HP.isChecked():
            sel2=1
        elif self.ui9.radioButton_A_KW.isChecked():
            sel2=2
        elif self.ui9.radioButton_A_KVA.isChecked():
            sel2=3
        elif self.ui9.radioButton_KW_IE.isChecked():
            sel2=4
        elif self.ui9.radioButton_KVA_IE.isChecked():
            sel2=5
        elif self.ui9.radioButton_HP_IE.isChecked():
            sel2=6
        elif self.ui9.radioButton_FP_IE.isChecked():
            sel2=7
        else:
            print("err")
            sel2=0

        self.ui9.label_mensaje.setText("")

        ventana = calculosVarios.funcion(sel1, sel2)
        if ventana == "Amperios conociendo HP en CC":
            dialog = Pag11(self)
            dialog.exec_()
            
        elif ventana == "Amp conociendo HP en AC 1F":
            dialog = Pag21(self)
            dialog.exec_()
        elif ventana == "Amp conociendo HP en AC 2F":
            dialog = Pag31(self)
            dialog.exec_()
        elif ventana == "Amp conociendo HP en AC 3F":
            dialog = Pag41(self)
            dialog.exec_()
        elif ventana == "Amp conociendo kW en CC":
            dialog = Pag12(self)
            dialog.exec_()
        elif ventana == "Amp conociendo kW en AC 1F":
            dialog = Pag22(self)
            dialog.exec_()
        elif ventana == "Amp conociendo kW en AC 2F":
            dialog = Pag32(self)
            dialog.exec_()
        elif ventana == "Amp conociendo kW en AC 3F":
            dialog = Pag42(self)
            dialog.exec_()
        elif ventana == "Amp conociendo kVA en AC 1F":
            dialog = Pag23(self)
            dialog.exec_()
        elif ventana == "Amp conociendo kVA en AC 2F":
            dialog = Pag33(self)
            dialog.exec_()
        elif ventana == "Amp conociendo kVA en AC 3F":
            dialog = Pag43(self)
            dialog.exec_()
        elif ventana == "kW conociendo I y E en CC":
            dialog = Pag14(self)
            dialog.exec_()
        elif ventana == "kW conociendo I y E en CA 1F":
            dialog = Pag24(self)
            dialog.exec_()
        elif ventana == "kW conociendo I y E en CA 2F":
            dialog = Pag34(self)
            dialog.exec_()
        elif ventana == "kW conociendo I y E en CA 3F":
            dialog = Pag44(self)
            dialog.exec_()
        elif ventana == "kVA conociendo I y E en CA 1F":
            dialog = Pag25(self)
            dialog.exec_()
        elif ventana == "kVA conociendo I y E en CA 2F":
            dialog = Pag35(self)
            dialog.exec_()
        elif ventana == "kVA conociendo I y E en CA 3F":
            dialog = Pag45(self)
            dialog.exec_()
        elif ventana == "HP en CC":
            dialog = Pag16(self)
            dialog.exec_()
        elif ventana == "HP en CA 1F":
            dialog = Pag26(self)
            dialog.exec_()
        elif ventana == "HP en CA 2F":
            dialog = Pag36(self)
            dialog.exec_()
        elif ventana == "HP en CA 3F":
            dialog = Pag46(self)
            dialog.exec_()
        elif ventana == "PF en CC":
            self.ui9.label_mensaje.setStyleSheet("color: green;font-weight: bold;")
            self.ui9.label_mensaje.setText("El factor de potencia o PF es igual a 1 en CC")
        elif ventana == "PF en CA 1F":
            dialog = Pag27(self)
            dialog.exec_()
        elif ventana == "PF en CA 2F":
            dialog = Pag37(self)
            dialog.exec_()
        elif ventana == "PF en CA 3F":
            dialog = Pag47(self)
            dialog.exec_()
        elif ventana == "Sin formula":
            self.ui9.label_mensaje.setStyleSheet("color: red;font-weight: bold;")
            self.ui9.label_mensaje.setText("No se puede calcular! Sin formula...")
        elif ventana == "Falta seleccionar":
            self.ui9.label_mensaje.setStyleSheet("color: red;font-weight: bold;")
            self.ui9.label_mensaje.setText("Falta seleccionar!!!")
        else:
            self.ui9.label_mensaje.setStyleSheet("color: red;font-weight: bold;")
            self.ui9.label_mensaje.setText("Algo salio Mal!")

    def funcion(sel1, sel2):
        if sel1 == 0 or sel2 == 0:
            return "Falta seleccionar"
    
        switcher = {
            (1, 1): "Amperios conociendo HP en CC",
            (1, 2): "Amp conociendo kW en CC",
            (2, 1): "Amp conociendo HP en AC 1F",
            (3, 1): "Amp conociendo HP en AC 2F",
            (4, 1): "Amp conociendo HP en AC 3F",
            (2, 2): "Amp conociendo kW en AC 1F",
            (3, 2): "Amp conociendo kW en AC 2F",
            (4, 2): "Amp conociendo kW en AC 3F",
            (1, 3): "Sin formula",
            (2, 3): "Amp conociendo kVA en AC 1F",
            (3, 3): "Amp conociendo kVA en AC 2F",
            (4, 3): "Amp conociendo kVA en AC 3F",
            (1, 4): "kW conociendo I y E en CC",
            (2, 4): "kW conociendo I y E en CA 1F",
            (3, 4): "kW conociendo I y E en CA 2F",
            (4, 4): "kW conociendo I y E en CA 3F",
            (1, 5): "Sin formula",
            (2, 5): "kVA conociendo I y E en CA 1F",
            (3, 5): "kVA conociendo I y E en CA 2F",
            (4, 5): "kVA conociendo I y E en CA 3F",
            (1, 6): "HP en CC",
            (2, 6): "HP en CA 1F",
            (3, 6): "HP en CA 2F",
            (4, 6): "HP en CA 3F",
            (1, 7): "PF en CC",
            (2, 7): "PF en CA 1F",
            (3, 7): "PF en CA 2F",
            (4, 7): "PF en CA 3F",


        }
        return switcher.get((sel1, sel2), "Valor inválido")

class probarNucleo(QMainWindow):
    def __init__(self, parent=None):
        super(probarNucleo, self).__init__(parent)
        self.ui10 = ventanas.probarNucleo()
        self.ui10.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Calculos para Probar el Nucleo")
        self.ui10.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.ui10.pushButton.clicked.connect(self.calcularInduccion)
        self.ui10.pushButton_2.clicked.connect(self.calcularTension)
        self.ui10.pushButton_3.clicked.connect(self.calcularVueltas)
    
    def calcularInduccion(self):
        dialog = probarNucleo_1(self)
        dialog.exec_()
    def calcularTension(self):
        dialog = probarNucleo_2(self)
        dialog.exec_()
    def calcularVueltas(self):
        dialog = probarNucleo_3(self)
        dialog.exec_()

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
class pesoCobre(QMainWindow):
    def __init__(self, parent=None):
        super(pesoCobre, self).__init__(parent)
        self.ui11 = ventanas.pesoCobre()
        self.ui11.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Calcular Peso del Cobre")
        self.ui11.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.ui11.pushButton_limpiar.clicked.connect(self.limpiar)
        self.ui11.pushButton.clicked.connect(self.calcular)
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def limpiar(self):
        self.ui11.textEdit_long.setText("")
        self.ui11.textEdit_cpar.setText("")
        self.ui11.textEdit_nbob.setText("")
        self.ui11.textEdit_nesp.setText("")
        self.ui11.textEdit_diam.setText("")
        self.ui11.label_peso.setText("-")
    def calcular(self):
        long = float(self.ui11.textEdit_long.toPlainText())
        cpar = float(self.ui11.textEdit_cpar.toPlainText())
        nbob = float(self.ui11.textEdit_nbob.toPlainText())
        nesp = float(self.ui11.textEdit_nesp.toPlainText())
        diam = float(self.ui11.textEdit_diam.toPlainText())
        long_total = long*cpar*nbob*nesp
        radio = diam/2000
        volumen = long_total*math.pi*(radio**2)

        peso= volumen*8960
        peso = float("%.2f" %peso)
        peso = str(peso)
        self.ui11.label_peso.setText(peso)
        
class Pag11(QDialog):
    def __init__(self, parent):
        super(Pag11, self).__init__(parent)
        self.ui9_11 = ventanas.Pag11()
        self.ui9_11.setupUi(self)  # Configurar la interfaz en la ventana principal
        
        self.setWindowTitle("Amp conociendo HP en CC")
        self.ui9_11.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_11.textEdit_E.toPlainText())
        efi = float(self.ui9_11.textEdit_Efi.toPlainText())
        hp = float(self.ui9_11.textEdit_HP.toPlainText())
        cor = ten*efi/(746*hp)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_11.label_A.setText(cor)
class Pag21(QDialog):
    def __init__(self, parent):
        super(Pag21, self).__init__(parent)
        self.ui9_21 = ventanas.Pag21()
        self.ui9_21.setupUi(self)
        self.setWindowTitle("Amp conociendo HP en AC 1F")
        self.ui9_21.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_21.textEdit_E.toPlainText())
        efi = float(self.ui9_21.textEdit_Efi.toPlainText())
        hp = float(self.ui9_21.textEdit_HP.toPlainText())
        pf = float(self.ui9_21.textEdit_facPot.toPlainText())
        
        cor = 746*hp/(ten*pf*efi)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_21.label_A.setText(cor)
class Pag31(QDialog):
    def __init__(self, parent):
        super(Pag31, self).__init__(parent)
        self.ui9_31 = ventanas.Pag31()
        self.ui9_31.setupUi(self)
        self.setWindowTitle("Amp conociendo HP en AC 2F")
        self.ui9_31.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_31.textEdit_E.toPlainText())
        efi = float(self.ui9_31.textEdit_Efi.toPlainText())
        hp = float(self.ui9_31.textEdit_HP.toPlainText())
        pf = float(self.ui9_31.textEdit_facPot.toPlainText())
        
        cor = 746*hp/(2*ten*pf*efi)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_31.label_A.setText(cor)
class Pag41(QDialog):
    def __init__(self, parent):
        super(Pag41, self).__init__(parent)
        self.ui9_41 = ventanas.Pag41()
        self.ui9_41.setupUi(self)
        self.setWindowTitle("Amp conociendo HP en AC 2F")
        self.ui9_41.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_41.textEdit_E.toPlainText())
        efi = float(self.ui9_41.textEdit_Efi.toPlainText())
        hp = float(self.ui9_41.textEdit_HP.toPlainText())
        pf = float(self.ui9_41.textEdit_facPot.toPlainText())
        
        cor = 746*hp/(ten*pf*efi*3**(0.5))
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_41.label_A.setText(cor)
class Pag12(QDialog):
    def __init__(self, parent):
        super(Pag12, self).__init__(parent)
        self.ui9_12 = ventanas.Pag12()
        self.ui9_12.setupUi(self)
        self.setWindowTitle("Amp conociendo kW en CC")
        self.ui9_12.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_12.textEdit_E.toPlainText())
        pot = float(self.ui9_12.textEdit_kW.toPlainText())
        
        cor = pot*1000/ten
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_12.label_A.setText(cor)
class Pag22(QDialog):
    def __init__(self, parent):
        super(Pag22, self).__init__(parent)
        self.ui9_22 = ventanas.Pag22()
        self.ui9_22.setupUi(self)
        self.setWindowTitle("Amp conociendo kW en AC 1F")
        self.ui9_22.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_22.textEdit_E.toPlainText())
        factor = float(self.ui9_22.textEdit_PF.toPlainText())
        pot = float(self.ui9_22.textEdit_kW.toPlainText())
        
        cor = pot*1000/(ten*factor)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_22.label_A.setText(cor)
class Pag32(QDialog):
    def __init__(self, parent):
        super(Pag32, self).__init__(parent)
        self.ui9_32 = ventanas.Pag32()
        self.ui9_32.setupUi(self)
        self.setWindowTitle("Amp conociendo kW en AC 2F")
        self.ui9_32.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_32.textEdit_E.toPlainText())
        factor = float(self.ui9_32.textEdit_PF.toPlainText())
        pot = float(self.ui9_32.textEdit_kW.toPlainText())
        
        cor = pot*1000/(2*ten*factor)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_32.label_A.setText(cor)
class Pag42(QDialog):
    def __init__(self, parent):
        super(Pag42, self).__init__(parent)
        self.ui9_42 = ventanas.Pag42()
        self.ui9_42.setupUi(self)
        self.setWindowTitle("Amp conociendo kW en AC 3F")
        self.ui9_42.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_42.textEdit_E.toPlainText())
        factor = float(self.ui9_42.textEdit_PF.toPlainText())
        pot = float(self.ui9_42.textEdit_kW.toPlainText())
        
        cor = pot*1000/(ten*factor*3**(0.5))
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_42.label_A.setText(cor)
class Pag23(QDialog):
    def __init__(self, parent):
        super(Pag23, self).__init__(parent)
        self.ui9_23 = ventanas.Pag23()
        self.ui9_23.setupUi(self)
        self.setWindowTitle("Amp conociendo kVA en AC 1F")
        self.ui9_23.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_23.textEdit_E.toPlainText())
        pot = float(self.ui9_23.textEdit_kva.toPlainText())
        
        cor = pot*1000/ten
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_23.label_A.setText(cor)
class Pag33(QDialog):
    def __init__(self, parent):
        super(Pag33, self).__init__(parent)
        self.ui9_33 = ventanas.Pag23() #Se considera 23 pq es parecida a 33
        self.ui9_33.setupUi(self)
        self.setWindowTitle("Amp conociendo kVA en AC 2F")
        self.ui9_33.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_33.textEdit_E.toPlainText())
        pot = float(self.ui9_33.textEdit_kva.toPlainText())
        
        cor = pot*1000/(2*ten)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_33.label_A.setText(cor)
class Pag43(QDialog):
    def __init__(self, parent):
        super(Pag43, self).__init__(parent)
        self.ui9_43 = ventanas.Pag23() #Se considera 23 pq es parecido a 43
        self.ui9_43.setupUi(self)
        self.setWindowTitle("Amp conociendo kVA en AC 3F")
        self.ui9_43.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_43.textEdit_E.toPlainText())
        pot = float(self.ui9_43.textEdit_kva.toPlainText())
        
        cor = pot*1000/(ten*3**0.5)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.ui9_43.label_A.setText(cor)
class Pag14(QDialog):
    def __init__(self, parent):
        super(Pag14, self).__init__(parent)
        self.ui9_41 = ventanas.Pag14()
        self.ui9_41.setupUi(self)
        self.setWindowTitle("kW conociendo I y E en CC")
        self.ui9_41.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_41.textEdit_E.toPlainText())
        cor = float(self.ui9_41.textEdit_I.toPlainText())
        
        pot = ten*cor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.ui9_41.label_P.setText(pot)
class Pag24(QDialog):
    def __init__(self, parent):
        super(Pag24, self).__init__(parent)
        self.ui9_24 = ventanas.Pag24()
        self.ui9_24.setupUi(self)
        self.setWindowTitle("kW conociendo I y E en CA 1F")
        self.ui9_24.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_24.textEdit_E.toPlainText())
        cor = float(self.ui9_24.textEdit_I.toPlainText())
        factor = float(self.ui9_24.textEdit_PF.toPlainText())

        pot = ten*cor*factor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.ui9_24.label_P.setText(pot)
class Pag34(QDialog):
    def __init__(self, parent):
        super(Pag34, self).__init__(parent)
        self.ui9_34 = ventanas.Pag24() #Parecido a 24
        self.ui9_34.setupUi(self)
        self.setWindowTitle("kW conociendo I y E en CA 2F")
        self.ui9_34.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_34.textEdit_E.toPlainText())
        cor = float(self.ui9_34.textEdit_I.toPlainText())
        factor = float(self.ui9_34.textEdit_PF.toPlainText())

        pot = 2*ten*cor*factor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.ui9_34.label_P.setText(pot)
class Pag44(QDialog):
    def __init__(self, parent):
        super(Pag44, self).__init__(parent)
        self.ui9_44 = ventanas.Pag24() #Parecido a 24
        self.ui9_44.setupUi(self)
        self.setWindowTitle("kW conociendo I y E en CA 3F")
        self.ui9_44.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_44.textEdit_E.toPlainText())
        cor = float(self.ui9_44.textEdit_I.toPlainText())
        factor = float(self.ui9_44.textEdit_PF.toPlainText())

        pot = (3**0.5)*ten*cor*factor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.ui9_44.label_P.setText(pot)
class Pag25(QDialog):
    def __init__(self, parent):
        super(Pag25, self).__init__(parent)
        self.ui9_25 = ventanas.Pag25()
        self.ui9_25.setupUi(self)
        self.setWindowTitle("kVA conociendo I y E en CA 1F")
        self.ui9_25.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_25.textEdit_E.toPlainText())
        cor = float(self.ui9_25.textEdit_I.toPlainText())

        pot = ten*cor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.ui9_25.label_P.setText(pot)
class Pag35(QDialog):
    def __init__(self, parent):
        super(Pag35, self).__init__(parent)
        self.ui9_35 = ventanas.Pag25() #Parecido a 25
        self.ui9_35.setupUi(self)
        self.setWindowTitle("kVA conociendo I y E en CA 2F")
        self.ui9_35.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_35.textEdit_E.toPlainText())
        cor = float(self.ui9_35.textEdit_I.toPlainText())

        pot = 2*ten*cor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.ui9_35.label_P.setText(pot)
class Pag45(QDialog):
    def __init__(self, parent):
        super(Pag45, self).__init__(parent)
        self.ui9_45 = ventanas.Pag25() #Parecida a 25
        self.ui9_45.setupUi(self)
        self.setWindowTitle("kVA conociendo I y E en CA 3F")
        self.ui9_45.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_45.textEdit_E.toPlainText())
        cor = float(self.ui9_45.textEdit_I.toPlainText())

        pot = (3**0.5)*ten*cor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.ui9_45.label_P.setText(pot)
class Pag16(QDialog):
    def __init__(self, parent):
        super(Pag16, self).__init__(parent)
        self.ui9_16 = ventanas.Pag16()
        self.ui9_16.setupUi(self)
        self.setWindowTitle("HP en CC")
        self.ui9_16.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_16.textEdit_E.toPlainText())
        cor = float(self.ui9_16.textEdit_I.toPlainText())
        efi = float(self.ui9_16.textEdit_efi.toPlainText())

        hp = cor*ten*efi/746
        hp = float("%.2f" %hp)
        hp = str(hp)
        self.ui9_16.label_HP.setText(hp)
class Pag26(QDialog):
    def __init__(self, parent):
        super(Pag26, self).__init__(parent)
        self.ui9_26 = ventanas.Pag26()
        self.ui9_26.setupUi(self)
        self.setWindowTitle("HP en CA 1F")
        self.ui9_26.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_26.textEdit_E.toPlainText())
        cor = float(self.ui9_26.textEdit_I.toPlainText())
        efi = float(self.ui9_26.textEdit_efi.toPlainText())
        factor = float(self.ui9_26.textEdit_PF.toPlainText())

        hp = cor*ten*efi*factor/746
        hp = float("%.2f" %hp)
        hp = str(hp)
        self.ui9_26.label_HP.setText(hp)
class Pag36(QDialog):
    def __init__(self, parent):
        super(Pag36, self).__init__(parent)
        self.ui9_36 = ventanas.Pag26() #Parecida a 26
        self.ui9_36.setupUi(self)
        self.setWindowTitle("HP en CA 2F")
        self.ui9_36.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_36.textEdit_E.toPlainText())
        cor = float(self.ui9_36.textEdit_I.toPlainText())
        efi = float(self.ui9_36.textEdit_efi.toPlainText())
        factor = float(self.ui9_36.textEdit_PF.toPlainText())

        hp = 2*cor*ten*efi*factor/746
        hp = float("%.2f" %hp)
        hp = str(hp)
        self.ui9_36.label_HP.setText(hp)
class Pag46(QDialog):
    def __init__(self, parent):
        super(Pag46, self).__init__(parent)
        self.ui9_46 = ventanas.Pag26() #Parecida a 26
        self.ui9_46.setupUi(self)
        self.setWindowTitle("HP en CA 3F")
        self.ui9_46.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_46.textEdit_E.toPlainText())
        cor = float(self.ui9_46.textEdit_I.toPlainText())
        efi = float(self.ui9_46.textEdit_efi.toPlainText())
        factor = float(self.ui9_46.textEdit_PF.toPlainText())

        hp = (3**0.5)*cor*ten*efi*factor/746
        hp = float("%.2f" %hp)
        hp = str(hp)
        self.ui9_46.label_HP.setText(hp)
class Pag27(QDialog):
    def __init__(self, parent):
        super(Pag27, self).__init__(parent)
        self.ui9_27 = ventanas.Pag27()
        self.ui9_27.setupUi(self)
        self.setWindowTitle("PF en CA 1F")
        self.ui9_27.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_27.textEdit_E.toPlainText())
        cor = float(self.ui9_27.textEdit_I.toPlainText())
        pot = float(self.ui9_27.textEdit_W.toPlainText())

        pf = pot/(ten*cor)
        pf = float("%.2f" %pf)
        pf = str(pf)
        self.ui9_27.label_PF.setText(pf)
class Pag37(QDialog):
    def __init__(self, parent):
        super(Pag37, self).__init__(parent)
        self.ui9_37 = ventanas.Pag27() #Parecido a 27
        self.ui9_37.setupUi(self)
        self.setWindowTitle("PF en CA 2F")
        self.ui9_37.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui9_37.textEdit_E.toPlainText())
        cor = float(self.ui9_37.textEdit_I.toPlainText())
        pot = float(self.ui9_37.textEdit_W.toPlainText())

        pf = pot/(2*ten*cor)
        pf = float("%.2f" %pf)
        pf = str(pf)
        self.ui9_37.label_PF.setText(pf)
class Pag47(QDialog):
    def __init__(self, parent):
        super(Pag47, self).__init__(parent)
        self.ui9_11 = ventanas.Pag27() #Parecido a 27
        self.ui9_11.setupUi(self)
        self.setWindowTitle("PF en CA 3F")
        self.ui9_11.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        pot = float(self.textEdit_W.toPlainText())

        pf = pot/(ten*cor*(3**0.5))
        pf = float("%.2f" %pf)
        pf = str(pf)
        self.label_PF.setText(pf)
class probarNucleo_1(QDialog):
    def __init__(self, parent):
        #super(probarNucleo_1,self).__init__(parent)
        #loadUi('calcularInduccion.ui', self)

        super(probarNucleo_1, self).__init__(parent)
        self.ui10_1 = ventanas.calcularInduccion()
        self.ui10_1.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Calcular Induccion de motor")
        self.ui10_1.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.ui10_1.textEdit_1.toPlainText())
        f = float(self.ui10_1.textEdit_2.toPlainText())
        esp = float(self.ui10_1.textEdit_3.toPlainText())
        sfe = float(self.ui10_1.textEdit_4.toPlainText())
        n = float(self.ui10_1.textEdit_5.toPlainText())

        ind = ten*(10**8)/(4.44*f*esp*sfe*n)
        ind = float("%.2f" %ind)
        ind = str(ind)

        self.ui10_1.label_7.setText(ind)
class probarNucleo_2(QDialog):
    def __init__(self, parent):
        super(probarNucleo_2, self).__init__(parent)
        self.ui10_2 = ventanas.calcularTension()
        self.ui10_2.setupUi(self)
        self.setWindowTitle("Calcular Tension de motor")
        self.ui10_2.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ind = float(self.ui10_2.textEdit_1.toPlainText())
        f = float(self.ui10_2.textEdit_2.toPlainText())
        esp = float(self.ui10_2.textEdit_3.toPlainText())
        sfe = float(self.ui10_2.textEdit_4.toPlainText())
        n = float(self.ui10_2.textEdit_5.toPlainText())

        ten = 4.44*f*esp*sfe*n*ind/(10**8)
        ten = float("%.2f" %ten)
        ten = str(ten)

        self.ui10_2.label_7.setText(ten)        
class probarNucleo_3(QDialog):
    def __init__(self, parent):
        super(probarNucleo_3, self).__init__(parent)
        self.ui10_3 = ventanas.calcularEspiras()
        self.ui10_3.setupUi(self)  # Configurar la interfaz en la ventana principal
        self.setWindowTitle("Calcular Espiras de motor")
        self.ui10_3.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ind = float(self.ui10_3.textEdit_1.toPlainText())
        f = float(self.ui10_3.textEdit_2.toPlainText())
        ten = float(self.ui10_3.textEdit_3.toPlainText())
        sfe = float(self.ui10_3.textEdit_4.toPlainText())
        n = float(self.ui10_3.textEdit_5.toPlainText())

        esp = ten*(10**8)/(4.44*f*ind*sfe*n)
        esp = float("%.2f" %esp)
        esp = str(esp)

        self.ui10_3.label_7.setText(esp) 

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()        
sys.exit(app.exec_())