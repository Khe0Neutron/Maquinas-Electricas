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

def exit_program():
    main.close()

exit_signal = Login.ExitSignal()
exit_signal.exit_program.connect(exit_program)

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi('window4.ui',self)
        self.pushButton_Exit.clicked.connect(self.Salir)
        self.pushButton.clicked.connect(self.abrirVentanaTension)
        self.pushButton_2.clicked.connect(self.abrirVentanaIntNominal)
        self.pushButton_3.clicked.connect(self.abrirVentanaCambiarTensionNominalMotor)
        self.pushButton_4.clicked.connect(self.VentanaIndFlujoMagnetico)
        self.pushButton_5.clicked.connect(self.TablaFlujoMagneticoMotores3F)
        self.pushButton_6.clicked.connect(self.CambioDeFrecuenciaMotor)
        self.pushButton_7.clicked.connect(self.CambioDePolaridad)
        self.pushButton_8.clicked.connect(self.motorMonofasicoCalc)
        self.pushButton_9.clicked.connect(self.calculosVarios)
        self.pushButton_10.clicked.connect(self.probarNucleo)
        self.pushButton_11.clicked.connect(self.pesoCobre)

         
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
        super(VentanaTension, self).__init__(parent)
        loadUi('window5.ui', self)
        self.setWindowTitle("Tension, Intensidad y Potencia")
        #
        self.label_12.setText("")
        self.radio_value()
        self.radioButton.clicked.connect(self.triangulo)
        self.radioButton_2.clicked.connect(self.estrella)
        self.pushButton.clicked.connect(self.radio_value)
        self.pushButton_2.clicked.connect(self.limpiar)
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)

    
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
        

    def radio_value(self):
        if self.radioButton.isChecked():
            self.calcularTriangulo()
        elif self.radioButton_2.isChecked():
            self.calcularEstrella()
        else:
            print("err")
    def limpiar(self):
        self.text_IL.setText("")
        self.text_IF.setText("")
        self.text_EL.setText("")
        self.text_EF.setText("")
        self.text_Phi.setText("")
        self.text_PL.setText("")
        self.text_PF.setText("")
        self.label_12.setText("Limpio!")
        
    def triangulo(self):
        pix = QPixmap("triangulo.png")
        self.label_2.setPixmap(pix)
        #self.pushButton.clicked.connect(self.calcularTriangulo)

    def estrella(self):
        pix = QPixmap("estrella.png")
        self.label_2.setPixmap(pix)
        #self.pushButton.clicked.connect(self.calcularEstrella)
              
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def calcularTriangulo(self):
        print("estas en triangulo")
        i_l=i_f=e_l=e_f=phi=p_f=p_l=""
        i_l = str(self.text_IL.toPlainText())
        i_f = str(self.text_IF.toPlainText())
        e_l = str(self.text_EL.toPlainText())
        e_f = str(self.text_EF.toPlainText())
        phi = str(self.text_Phi.toPlainText())
        p_f = str(self.text_IF.toPlainText())
        p_l = str(self.text_IF.toPlainText())
        if i_l != "" and i_f == "":
            print("entraste a t_i_f")
            i_l=float(i_l)
            result= VentanaTension.t_IF(i_l)
            i_f=float("%.4f" % result)
            self.text_IF.setText(str(i_f))
            self.label_12.setText("Calculado!")
        elif i_f != "" and i_l == "":
            print("entraste a t_i_l")
            i_f = float(i_f)
            result= VentanaTension.t_IL(i_f)
            i_l=float("%.4f" % result)
            self.text_IL.setText(str(i_l))
            self.label_12.setText("Calculado!")
        elif i_l == "" and i_f == "":
            self.label_12.setText("Calculado!")
        else:    
            self.label_12.setText("Limpie! no calculo...")

        if e_l != "" and e_f == "":
            print("entraste a t_e_f")
            e_l=float(e_l)
            result= VentanaTension.t_EF(e_l)
            e_f=float("%.4f" % result)
            self.text_EF.setText(str(e_f))
            self.label_12.setText("Calculado!")  
        elif e_f != "" and e_l == "":
            print("entraste a t_e_l")
            e_f = float(e_f)
            result= VentanaTension.t_EL(e_f)
            e_l=float("%.4f" % result)
            self.text_EL.setText(str(e_l))
            self.label_12.setText("Calculado!")
        elif e_l == "" and e_f == "":
            self.label_12.setText("Esperando...")
        else:    
            self.label_12.setText("Limpie! no calculo...")
            
        if phi != "":
            phi = float(phi)
            phi = phi*math.pi/180
            p_f = VentanaTension.p_fase(e_f,i_f,phi)
            p_l = VentanaTension.p_fase(e_l,i_l,phi)
            p_f=float("%.4f" % p_f)
            p_l=float("%.4f" % p_l)
            self.text_PF.setText(str(p_f))
            self.text_PL.setText(str(p_l))
            self.label_12.setText("Calculado!")
        
    def calcularEstrella(self):
        print("estas en estrella")
        i_l=i_f=e_l=e_f=phi=p_f=p_l=""
        i_l = str(self.text_IL.toPlainText())
        i_f = str(self.text_IF.toPlainText())
        e_l = str(self.text_EL.toPlainText())
        e_f = str(self.text_EF.toPlainText())
        phi = str(self.text_Phi.toPlainText())
        p_f = str(self.text_IF.toPlainText())
        p_l = str(self.text_IF.toPlainText())
        if i_l != "" and i_f == "":
            print("entraste a e_i_f")
            i_l=float(i_l)
            result= VentanaTension.e_IF(i_l)
            i_f=float("%.4f" % result)
            self.text_IF.setText(str(i_f))
            self.label_12.setText("Calculado!")
        elif i_f != "" and i_l == "":
            print("entraste a e_i_l")
            i_f = float(i_f)
            result= VentanaTension.e_IL(i_f)
            i_l=float("%.4f" % result)
            self.text_IL.setText(str(i_l))
            self.label_12.setText("Calculado!")
        elif i_l == "" and i_f == "":
            print("entraste a e_i_f")
            self.label_12.setText("Calculado!")
        else:    
            self.label_12.setText("Limpie! no calculo...")

        if e_l != "" and e_f == "":
            print("entraste a e_e_f")
            e_l=float(e_l)
            result= VentanaTension.e_EF(e_l)
            e_f=float("%.4f" % result)
            self.text_EF.setText(str(e_f))
            self.label_12.setText("Calculado!")  
        elif e_f != "" and e_l == "":
            print("entraste a e_e_l")
            e_f = float(e_f)
            result= VentanaTension.e_EL(e_f)
            e_l=float("%.4f" % result)
            self.text_EL.setText(str(e_l))
            self.label_12.setText("Calculado!")
        elif e_l == "" and e_f == "":
            print("entraste a e_e_f")
            self.label_12.setText("Calculado!")
        else:    
            self.label_12.setText("Limpie! no calculo...")
            
        if phi != "":
            phi = float(phi)
            phi = phi*math.pi/180
            p_f = VentanaTension.p_fase(e_f,i_f,phi)
            p_l = VentanaTension.p_fase(e_l,i_l,phi)
            p_f=float("%.4f" % p_f)
            p_l=float("%.4f" % p_l)
            self.text_PF.setText(str(p_f))
            self.text_PL.setText(str(p_l))

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
        loadUi('window6.ui',self)
        self.setWindowTitle("Intensidad Nominal")
        self.pushButton.clicked.connect(self.calcular)
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.pushButton_2.clicked.connect(self.limpiar)
    
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def limpiar(self):
        self.text_IN.setText("")
        self.text_EN.setText("")
        self.text_Phi.setText("")
        self.text_EF.setText("")
        self.text_I.setText("")
        self.text_E.setText("")
    def calcular(self):
        i_n = str(self.text_IN.toPlainText())
        e_n = str(self.text_EN.toPlainText())
        phi = str(self.text_Phi.toPlainText())
        e_f = str(self.text_EF.toPlainText())
        i = str(self.text_I.toPlainText())
        e = str(self.text_E.toPlainText())
        if i_n!="" and e_n!="" and phi!="" and e_f!="" and i!="" and e!="":
            i_n = float(self.text_IN.toPlainText())
            e_n = float(self.text_EN.toPlainText())
            phi = float(self.text_Phi.toPlainText())
            e_f = float(self.text_EF.toPlainText())
            i = float(self.text_I.toPlainText())
            e = float(self.text_E.toPlainText())
            phi = phi*math.pi/180
            hp = i_n*e_n*math.cos(phi)*e_f*1.73/746
            kw = i*e*math.cos(phi)*(3**(1/2))/1000
            int_nom=hp*746/(e*math.cos(phi)*(3**(1/2))*e_f)
            hp = float("%.4f" % hp)
            kw = float("%.4f" % kw)
            int_nom = float("%.4f" % int_nom)
            self.label_HP.setText(str(hp))
            self.label_KW.setText(str(kw))
            self.label_IntNom.setText(str(int_nom))
            self.label_mensaje.setStyleSheet("color:green;")
            self.label_mensaje.setText("Calculado!")
        else:
            self.label_mensaje.setStyleSheet("color:red")
            self.label_mensaje.setText("No calculado... Faltan Datos")

class VentanaCambiarTensionNominalMotor(QMainWindow):
     def __init__(self, parent=None):
        super(VentanaCambiarTensionNominalMotor, self).__init__(parent)
        loadUi('cambiarTenNom.ui',self)
        self.setWindowTitle("Cambio de Tension Nominal de motor 3F")
        self.pushButton.clicked.connect(self.calcular)
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.pushButton_2.clicked.connect(self.limpiar)

     def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
     def limpiar(self):
        self.text_NumPriEsp.setText("")
        self.text_CapAnt.setText("")
        self.text_SecCobAnt.setText("")
        self.text_TenRedAnt.setText("")
        self.text_TenRedNue.setText("")
        self.text_VueRanAnt.setText("")
        self.label_NumEspNue.setText("-")
        self.label_VueRanNue.setText("-")
        self.label_SecAlaNue.setText("-")
        self.label_CapNue.setText("-")
        self.label_mensaje.setStyleSheet("color:black;")
        self.label_mensaje.setText("")

     def calcular(self):
         v_r_a= self.text_VueRanAnt.toPlainText()
         e_n= self.text_TenRedNue.toPlainText()
         e_a= self.text_TenRedAnt.toPlainText()
         s_a_a= self.text_SecCobAnt.toPlainText()
         c_p= self.text_CapAnt.toPlainText()
         n_p_e= self.text_NumPriEsp.toPlainText()
         if e_a!="" and e_n!="":
            if v_r_a!="":   
                v_r_n = VentanaCambiarTensionNominalMotor.calculoVueltasRanuraNueva(v_r_a,e_n,e_a)
                v_r_n = float("%.4f" % v_r_n)
                v_r_n = str(v_r_n)
                self.label_VueRanNue.setText(v_r_n)
                self.label_mensaje.setStyleSheet("color:black;")
                self.label_mensaje.setText("Calculado!")
                if s_a_a!="":
                    s_a_n = VentanaCambiarTensionNominalMotor.calculoSeccionAlamNuevo(s_a_a,v_r_a,v_r_n)
                    s_a_n = float("%.4f" % s_a_n)
                    s_a_n = str(s_a_n)
                    self.label_SecAlaNue.setText(s_a_n)
                    self.label_mensaje.setStyleSheet("color:black;")
                    self.label_mensaje.setText("Calculado!")
                else:
                    self.label_mensaje.setStyleSheet("color:black;")
                    self.label_mensaje.setText("Calculo parcial... complete seccion del \n alambre para obtener la nueva seccion")
            else:
                self.label_mensaje.setStyleSheet("color:black;")
                self.label_mensaje.setText("Datos insuficientes! complete las vueltas de ranura antigua")
                
            if c_p!="":
                c_n = VentanaCambiarTensionNominalMotor.calculoNuevaCapacidad(e_a,c_p,e_n)
                c_n = float("%.4f" % c_n)
                c_n = str(c_n)
                self.label_CapNue.setText(c_n)
                self.label_mensaje.setStyleSheet("color:black;")
                self.label_mensaje.setText("Calculado!")
            
            if n_p_e!="":
                n_e_n = VentanaCambiarTensionNominalMotor.calculoNUmeroEspirasNuevo(n_p_e,e_n,e_a)
                n_e_n = float("%.4f" % n_e_n)
                n_e_n = str(n_e_n)
                self.label_NumEspNue.setText(n_e_n)
                self.label_mensaje.setStyleSheet("color:black;")
                self.label_mensaje.setText("Calculado!")
         else:
            self.label_mensaje.setStyleSheet("color:red;")
            self.label_mensaje.setText("Datos insuficientes!")

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
        super(VentanaIndFlujoMagnetico, self).__init__(parent)
        loadUi('indFlujoMagnetico.ui',self)
        self.setWindowTitle("Induccion de Flujo Magnetico")
        self.pushButton.clicked.connect(self.calcular)
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.pushButton_2.clicked.connect(self.limpiar)

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def limpiar(self):
        self.text_u.setText("")
        self.text_N.setText("")
        self.text_A.setText("")
        self.text_L.setText("")
        self.text_E.setText("")
        self.text_I.setText("")
        self.text_F.setText("")
        self.text_Kd.setText("")
        self.label_Induccion.setText("-")
        self.label_EspirasF.setText("-")
        self.label_mensaje.setStyleSheet("color: black; background-color:transparent;")
        self.label_mensaje.setText("limpio!")
        self.label_gauss.setText("")
        self.label_espiras  .setText("")

    def calcular(self):
        u = self.text_u.toPlainText()
        n = self.text_N.toPlainText()
        a = self.text_A.toPlainText()
        l = self.text_L.toPlainText()
        e = self.text_E.toPlainText()
        i = self.text_I.toPlainText()
        f = self.text_F.toPlainText()
        kd = self.text_Kd.toPlainText()
        

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
            self.label_mensaje.setStyleSheet("color: black; background-color:transparent;")
            self.label_mensaje.setText("calculado!")
            self.label_Induccion.setAlignment(QtCore.Qt.AlignRight)
            self.label_EspirasF.setAlignment(QtCore.Qt.AlignRight)
            self.label_Induccion.setText(str(ind))
            self.label_EspirasF.setText(str(cond))
            self.label_gauss.setText("[Gauss]")
            self.label_espiras.setText("[Espiras]")

        else:
            self.label_mensaje.setStyleSheet("color:red; background-color:yellow;")
            self.label_mensaje.setText("Faltan datos!")
            self.label_gauss.setText("")
            self.label_gauss.setText("")


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
        super(TablaFlujoMagneticoMotores3F, self).__init__(parent)
        self.ui = ('flujoMagneticoM3F.ui')
        loadUi(self.ui, self)
        self.setWindowTitle("Tabla de Flujo Magnnetico Motores 3F")
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)   
        self.pushButton.clicked.connect(self.mostrar_tabla)

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def crear_tabla(self):
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
        
        self.table.setRowCount(y)
        self.table.setColumnCount(x)
        self.table.resize(770, 480)

        for j in range(x):
            encabezado = QtWidgets.QTableWidgetItem(columnas[j])
            self.table.setHorizontalHeaderItem(j,encabezado)
            for i in range(y):
                dato = str(df_fila[i][j])
                if dato == 'nan':
                    dato=''
                self.table.setItem(i,j,QTableWidgetItem(dato))  
    
    def mostrar_tabla(self):
        pix = QPixmap("img/tablaFlujoMagneticoM3F.png").scaled(450, 480)
        
        self.label.resize(450,480)
        self.label.setPixmap(pix)

class CambioDeFrecuenciaMotor(QMainWindow):
    def __init__(self, parent=None):
        super(CambioDeFrecuenciaMotor, self).__init__(parent)
        loadUi('cambioDeFrecuenciaM.ui', self)
        self.setWindowTitle("Cambio de Frecuencia de Motor")
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.pushButtonLimpiar.clicked.connect(self.limpiar)
        self.pushButton.clicked.connect(self.calcular)


    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def limpiar(self):
        self.textPotAnt.setText("")
        self.textFreAnt.setText("")
        self.textRanEstAnt.setText("")
        self.textSecCobAnt.setText("")
        self.textNueFre.setText("")
        self.label_PotNue.setText("")
        self.label_RanEstNue.setText("")
        self.label_SecCobNue.setText("")
        self.label_7.setText("")


    def calcular(self):
        potAnt = self.textPotAnt.toPlainText()
        frecAnt = self.textFreAnt.toPlainText()
        ranEstAnt = self.textRanEstAnt.toPlainText()
        secCobAnt = self.textSecCobAnt.toPlainText()
        nueFrec = self.textNueFre.toPlainText()
        
        potNue = CambioDeFrecuenciaMotor.calcularPot(nueFrec,frecAnt,potAnt)
        ranEstNue = CambioDeFrecuenciaMotor.calcularRan(nueFrec,frecAnt,ranEstAnt)
        #if secCobAnt!="":
        secCobNue = CambioDeFrecuenciaMotor.calcularSec(nueFrec,frecAnt,secCobAnt)
        secCobNue = float("%.4f" % secCobNue)
        secCobNue = str(secCobNue)
        #else:
        secCobNue = ""    
        potNue = float("%.4f" % potNue)
        ranEstNue = float("%.4f" % ranEstNue)
        potNue = str(potNue)
        ranEstNue = str(ranEstNue)
        self.label_PotNue.setText(potNue)
        self.label_7.setText("HP")
        self.label_RanEstNue.setText(ranEstNue)
        self.label_SecCobNue.setText(secCobNue)


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
        loadUi('cambioDePolaridad.ui', self)
        self.setWindowTitle("Cambio de Polaridad")
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.pushButton.clicked.connect(self.calcular)
        self.pushButtonLimpiar.clicked.connect(self.limpiar)
        self.pushButton_2.clicked.connect(self.abrirVentana_2)
         

    def abrirVentana_2(self):
        self.hide()
        otraventana=CambioDePolaridad_2(self)
        otraventana.show()

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def limpiar(self):
        self.textEdit_DenCorAnt.setText("")
        self.textEdit_2_FacBobAnt.setText("")
        self.textEdit_3_IndAntDie.setText("")
        self.textEdit_4_PotAnt.setText("")
        self.textEdit_5_DenCorNue.setText("")
        self.textEdit_6_FacBobNue.setText("")
        self.textEdit_7_IndNueDie.setText("")
        self.label_PotNue.setText("")

    def calcular(self):
        denCorAnt = self.textEdit_DenCorAnt.toPlainText()
        facBobAnt = self.textEdit_2_FacBobAnt.toPlainText()
        indAntDie = self.textEdit_3_IndAntDie.toPlainText()
        potAnt = self.textEdit_4_PotAnt.toPlainText()
        denCorNue = self.textEdit_5_DenCorNue.toPlainText()
        facBobNue = self.textEdit_6_FacBobNue.toPlainText()
        indNueDie = self.textEdit_7_IndNueDie.toPlainText()

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
        self.label_PotNue.setText(potNue)

class CambioDePolaridad_2(QMainWindow):
    def __init__(self, parent=None):
        super(CambioDePolaridad_2, self).__init__(parent)
        loadUi('cambioDePolaridad_2.ui', self)
        self.setWindowTitle("Cambio de Polaridad 2")
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.pushButton.clicked.connect(self.calcular)
        #self.pushButtonLimpiar.clicked.connect(self.limpiar)
        

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def calcular(self):
        numRan = self.textEdit_1_NumRan.toPlainText()
        numPol = self.textEdit_2_NumPol.toPlainText()
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
        self.textEdit_Y.setText(y)
        self.textEdit_Yc.setText(yc)
        self.textEdit_AngEle.setText(angElec)
        self.textEdit_Kd.setText(Kd)
        self.textEdit_Kp.setText(Kp)
        self.textEdit_Kw.setText(Kw)

class motorMonofasicoCalc(QMainWindow):
    def __init__(self, parent=None):
        super(motorMonofasicoCalc, self).__init__(parent)
        loadUi('motorMonofasicoCalc.ui', self)
        self.setWindowTitle("Calculos Motor Monofasico")
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.pushButtonLimpiar.clicked.connect(self.limpiar)
        self.pushButton.clicked.connect(self.calNumEsp)
        self.pushButton_2.clicked.connect(self.calSecMayNue)
        self.pushButton_3.clicked.connect(self.calCapacidad)
        self.pushButton_4.clicked.connect(self.calSecNue2)

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def limpiar(self):
        self.textTenPrim.setText("")
        self.textTenNue.setText("")
        self.textEspPrim.setText("")
        self.label_EspNue.setText("")
        self.textSeccPrim.setText("")
        self.label_SeccNue.setText("")
        self.textCapPrim.setText("")
        self.label_CapNue.setText("")
        self.textVelPrim.setText("")
        self.textVelNue.setText("")
        self.textSeccPrim_2.setText("")
        self.label_SeccNue_2.setText("")

    def calNumEsp(self):
        tenPrim = float(self.textTenPrim.toPlainText())
        tenNue = float(self.textTenNue.toPlainText())
        espPrim = float(self.textEspPrim.toPlainText())

        espNue = espPrim*tenNue/tenPrim
        espNue = str(float("%.2f" %espNue))
        
        self.label_EspNue.setText(espNue)
        

    def calSecMayNue(self):
        tenPrim = float(self.textTenPrim.toPlainText())
        tenNue = float(self.textTenNue.toPlainText())
        secPrim = float(self.textSeccPrim.toPlainText())
        
        secNue = secPrim*tenNue/tenPrim
        secNue = str(float("%.2f" %secNue))

        self.label_SeccNue.setText(secNue) 

    def calCapacidad(self):
        tenPrim = float(self.textTenPrim.toPlainText())
        tenNue = float(self.textTenNue.toPlainText())
        capPrim = float(self.textCapPrim.toPlainText())
        
        capNue = capPrim*tenNue/tenPrim
        capNue = str(float("%.4f" %capNue))

        self.label_CapNue.setText(capNue)


    def calSecNue2(self):
        velPrim = float(self.textVelPrim.toPlainText())
        velNue = float(self.textVelNue.toPlainText())
        secPrim2 = float(self.textSeccPrim_2.toPlainText())
        
        secNue2 = secPrim2*velNue/velPrim
        secNue2 = str(float("%.4f" %secNue2))

        self.label_SeccNue_2.setText(secNue2)

class calculosVarios(QMainWindow):
    def __init__(self,parent):
        super(calculosVarios, self).__init__(parent)
        loadUi('calculosVarios.ui', self)
        self.setWindowTitle("Calculos Varios")
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.pushButton.clicked.connect(self.seleccion)
    
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def  seleccion(self):
        #primera seleccion
        if self.radioButton_DC.isChecked():
            sel1=1
        elif self.radioButton_ACM.isChecked():
            sel1=2
        elif self.radioButton_ACB.isChecked():
            sel1=3
        elif self.radioButton_ACT.isChecked():
            sel1=4
        else:
            sel1=0
            print("err")
        #segunda seleccion
        if self.radioButton_A_HP.isChecked():
            sel2=1
        elif self.radioButton_A_KW.isChecked():
            sel2=2
        elif self.radioButton_A_KVA.isChecked():
            sel2=3
        elif self.radioButton_KW_IE.isChecked():
            sel2=4
        elif self.radioButton_KVA_IE.isChecked():
            sel2=5
        elif self.radioButton_HP_IE.isChecked():
            sel2=6
        elif self.radioButton_FP_IE.isChecked():
            sel2=7
        else:
            print("err")
            sel2=0

        self.label_mensaje.setText("")

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
            self.label_mensaje.setStyleSheet("color: green;font-weight: bold;")
            self.label_mensaje.setText("El factor de potencia o PF es igual a 1 en CC")
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
            self.label_mensaje.setStyleSheet("color: red;font-weight: bold;")
            self.label_mensaje.setText("No se puede calcular! Sin formula...")
        elif ventana == "Falta seleccionar":
            self.label_mensaje.setStyleSheet("color: red;font-weight: bold;")
            self.label_mensaje.setText("Falta seleccionar!!!")
        else:
            self.label_mensaje.setStyleSheet("color: red;font-weight: bold;")
            self.label_mensaje.setText("Algo salio Mal!")

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
        loadUi('probarNucleo.ui', self)
        self.setWindowTitle("Calculos para Probar el Nucleo")
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.pushButton.clicked.connect(self.calcularInduccion)
        self.pushButton_2.clicked.connect(self.calcularTension)
        self.pushButton_3.clicked.connect(self.calcularVueltas)
    
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
        loadUi('pesoCobre.ui', self)
        self.setWindowTitle("Calcular Peso del Cobre")
        self.pushButtonAtras.clicked.connect(self.abrirVentanaPrincipal)
        self.pushButton_limpiar.clicked.connect(self.limpiar)
        self.pushButton.clicked.connect(self.calcular)
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def limpiar(self):
        self.textEdit_long.setText("")
        self.textEdit_cpar.setText("")
        self.textEdit_nbob.setText("")
        self.textEdit_nesp.setText("")
        self.textEdit_diam.setText("")
        self.label_peso.setText("-")
    def calcular(self):
        long = float(self.textEdit_long.toPlainText())
        cpar = float(self.textEdit_cpar.toPlainText())
        nbob = float(self.textEdit_nbob.toPlainText())
        nesp = float(self.textEdit_nesp.toPlainText())
        diam = float(self.textEdit_diam.toPlainText())
        long_total = long*cpar*nbob*nesp
        radio = diam/2000
        volumen = long_total*math.pi*(radio**2)

        peso= volumen*8960
        peso = float("%.2f" %peso)
        peso = str(peso)
        self.label_peso.setText(peso)
        
class Pag11(QDialog):
    def __init__(self, parent):
        super(Pag11,self).__init__(parent)
        loadUi('dialog1.ui', self)
        self.setWindowTitle("Amp conociendo HP en CC")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        efi = float(self.textEdit_Efi.toPlainText())
        hp = float(self.textEdit_HP.toPlainText())
        cor = ten*efi/(746*hp)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag21(QDialog):
    def __init__(self, parent):
        super(Pag21,self).__init__(parent)
        loadUi('dialog2.ui', self)
        self.setWindowTitle("Amp conociendo HP en AC 1F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        efi = float(self.textEdit_Efi.toPlainText())
        hp = float(self.textEdit_HP.toPlainText())
        pf = float(self.textEdit_facPot.toPlainText())
        
        cor = 746*hp/(ten*pf*efi)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag31(QDialog):
    def __init__(self, parent):
        super(Pag31,self).__init__(parent)
        loadUi('dialog31.ui', self)
        self.setWindowTitle("Amp conociendo HP en AC 2F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        efi = float(self.textEdit_Efi.toPlainText())
        hp = float(self.textEdit_HP.toPlainText())
        pf = float(self.textEdit_facPot.toPlainText())
        
        cor = 746*hp/(2*ten*pf*efi)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag41(QDialog):
    def __init__(self, parent):
        super(Pag41,self).__init__(parent)
        loadUi('dialog41.ui', self)
        self.setWindowTitle("Amp conociendo HP en AC 2F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        efi = float(self.textEdit_Efi.toPlainText())
        hp = float(self.textEdit_HP.toPlainText())
        pf = float(self.textEdit_facPot.toPlainText())
        
        cor = 746*hp/(ten*pf*efi*3**(0.5))
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag12(QDialog):
    def __init__(self, parent):
        super(Pag12,self).__init__(parent)
        loadUi('dialog12.ui', self)
        self.setWindowTitle("Amp conociendo kW en CC")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        pot = float(self.textEdit_kW.toPlainText())
        
        cor = pot*1000/ten
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag22(QDialog):
    def __init__(self, parent):
        super(Pag22,self).__init__(parent)
        loadUi('dialog22.ui', self)
        self.setWindowTitle("Amp conociendo kW en AC 1F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        factor = float(self.textEdit_PF.toPlainText())
        pot = float(self.textEdit_kW.toPlainText())
        
        cor = pot*1000/(ten*factor)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag32(QDialog):
    def __init__(self, parent):
        super(Pag32,self).__init__(parent)
        loadUi('dialog32.ui', self)
        self.setWindowTitle("Amp conociendo kW en AC 2F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        factor = float(self.textEdit_PF.toPlainText())
        pot = float(self.textEdit_kW.toPlainText())
        
        cor = pot*1000/(2*ten*factor)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag42(QDialog):
    def __init__(self, parent):
        super(Pag42,self).__init__(parent)
        loadUi('dialog42.ui', self)
        self.setWindowTitle("Amp conociendo kW en AC 3F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        factor = float(self.textEdit_PF.toPlainText())
        pot = float(self.textEdit_kW.toPlainText())
        
        cor = pot*1000/(ten*factor*3**(0.5))
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag23(QDialog):
    def __init__(self, parent):
        super(Pag23,self).__init__(parent)
        loadUi('dialog23.ui', self)
        self.setWindowTitle("Amp conociendo kVA en AC 1F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        pot = float(self.textEdit_kva.toPlainText())
        
        cor = pot*1000/ten
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag33(QDialog):
    def __init__(self, parent):
        super(Pag33,self).__init__(parent)
        loadUi('dialog23.ui', self)
        self.setWindowTitle("Amp conociendo kVA en AC 2F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        pot = float(self.textEdit_kva.toPlainText())
        
        cor = pot*1000/(2*ten)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag43(QDialog):
    def __init__(self, parent):
        super(Pag43,self).__init__(parent)
        loadUi('dialog23.ui', self)
        self.setWindowTitle("Amp conociendo kVA en AC 3F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        pot = float(self.textEdit_kva.toPlainText())
        
        cor = pot*1000/(ten*3**0.5)
        cor = float("%.2f" %cor)
        cor = str(cor)
        self.label_A.setText(cor)
class Pag14(QDialog):
    def __init__(self, parent):
        super(Pag14,self).__init__(parent)
        loadUi('dialog14.ui', self)
        self.setWindowTitle("kW conociendo I y E en CC")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        
        pot = ten*cor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.label_P.setText(pot)
class Pag24(QDialog):
    def __init__(self, parent):
        super(Pag24,self).__init__(parent)
        loadUi('dialog24.ui', self)
        self.setWindowTitle("kW conociendo I y E en CA 1F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        factor = float(self.textEdit_PF.toPlainText())

        pot = ten*cor*factor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.label_P.setText(pot)
class Pag34(QDialog):
    def __init__(self, parent):
        super(Pag34,self).__init__(parent)
        loadUi('dialog24.ui', self)
        self.setWindowTitle("kW conociendo I y E en CA 2F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        factor = float(self.textEdit_PF.toPlainText())

        pot = 2*ten*cor*factor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.label_P.setText(pot)
class Pag44(QDialog):
    def __init__(self, parent):
        super(Pag44,self).__init__(parent)
        loadUi('dialog24.ui', self)
        self.setWindowTitle("kW conociendo I y E en CA 3F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        factor = float(self.textEdit_PF.toPlainText())

        pot = (3**0.5)*ten*cor*factor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.label_P.setText(pot)
class Pag25(QDialog):
    def __init__(self, parent):
        super(Pag25,self).__init__(parent)
        loadUi('dialog25.ui', self)
        self.setWindowTitle("kVA conociendo I y E en CA 1F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())

        pot = ten*cor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.label_P.setText(pot)
class Pag35(QDialog):
    def __init__(self, parent):
        super(Pag35,self).__init__(parent)
        loadUi('dialog25.ui', self)
        self.setWindowTitle("kVA conociendo I y E en CA 2F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())

        pot = 2*ten*cor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.label_P.setText(pot)
class Pag45(QDialog):
    def __init__(self, parent):
        super(Pag45,self).__init__(parent)
        loadUi('dialog25.ui', self)
        self.setWindowTitle("kVA conociendo I y E en CA 3F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())

        pot = (3**0.5)*ten*cor/1000
        pot = float("%.2f" %pot)
        pot = str(pot)
        self.label_P.setText(pot)
class Pag16(QDialog):
    def __init__(self, parent):
        super(Pag16,self).__init__(parent)
        loadUi('dialog16.ui', self)
        self.setWindowTitle("HP en CC")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        efi = float(self.textEdit_efi.toPlainText())

        hp = cor*ten*efi/746
        hp = float("%.2f" %hp)
        hp = str(hp)
        self.label_HP.setText(hp)
class Pag26(QDialog):
    def __init__(self, parent):
        super(Pag26,self).__init__(parent)
        loadUi('dialog26.ui', self)
        self.setWindowTitle("HP en CA 1F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        efi = float(self.textEdit_efi.toPlainText())
        factor = float(self.textEdit_PF.toPlainText())

        hp = cor*ten*efi*factor/746
        hp = float("%.2f" %hp)
        hp = str(hp)
        self.label_HP.setText(hp)
class Pag36(QDialog):
    def __init__(self, parent):
        super(Pag36,self).__init__(parent)
        loadUi('dialog26.ui', self)
        self.setWindowTitle("HP en CA 2F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        efi = float(self.textEdit_efi.toPlainText())
        factor = float(self.textEdit_PF.toPlainText())

        hp = 2*cor*ten*efi*factor/746
        hp = float("%.2f" %hp)
        hp = str(hp)
        self.label_HP.setText(hp)
class Pag46(QDialog):
    def __init__(self, parent):
        super(Pag46,self).__init__(parent)
        loadUi('dialog26.ui', self)
        self.setWindowTitle("HP en CA 3F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        efi = float(self.textEdit_efi.toPlainText())
        factor = float(self.textEdit_PF.toPlainText())

        hp = (3**0.5)*cor*ten*efi*factor/746
        hp = float("%.2f" %hp)
        hp = str(hp)
        self.label_HP.setText(hp)
class Pag27(QDialog):
    def __init__(self, parent):
        super(Pag27,self).__init__(parent)
        loadUi('dialog27.ui', self)
        self.setWindowTitle("PF en CA 1F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        pot = float(self.textEdit_W.toPlainText())

        pf = pot/(ten*cor)
        pf = float("%.2f" %pf)
        pf = str(pf)
        self.label_PF.setText(pf)
class Pag37(QDialog):
    def __init__(self, parent):
        super(Pag37,self).__init__(parent)
        loadUi('dialog27.ui', self)
        self.setWindowTitle("PF en CA 2F")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_E.toPlainText())
        cor = float(self.textEdit_I.toPlainText())
        pot = float(self.textEdit_W.toPlainText())

        pf = pot/(2*ten*cor)
        pf = float("%.2f" %pf)
        pf = str(pf)
        self.label_PF.setText(pf)
class Pag47(QDialog):
    def __init__(self, parent):
        super(Pag47,self).__init__(parent)
        loadUi('dialog27.ui', self)
        self.setWindowTitle("PF en CA 3F")
        self.pushButton.clicked.connect(self.calcular)

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
        super(probarNucleo_1,self).__init__(parent)
        loadUi('calcularInduccion.ui', self)
        self.setWindowTitle("Calcular Induccion de motor")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ten = float(self.textEdit_1.toPlainText())
        f = float(self.textEdit_2.toPlainText())
        esp = float(self.textEdit_3.toPlainText())
        sfe = float(self.textEdit_4.toPlainText())
        n = float(self.textEdit_5.toPlainText())

        ind = ten*(10**8)/(4.44*f*esp*sfe*n)
        ind = float("%.2f" %ind)
        ind = str(ind)

        self.label_7.setText(ind)
class probarNucleo_2(QDialog):
    def __init__(self, parent):
        super(probarNucleo_2,self).__init__(parent)
        loadUi('calcularTension.ui', self)
        self.setWindowTitle("Calcular Tension de motor")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ind = float(self.textEdit_1.toPlainText())
        f = float(self.textEdit_2.toPlainText())
        esp = float(self.textEdit_3.toPlainText())
        sfe = float(self.textEdit_4.toPlainText())
        n = float(self.textEdit_5.toPlainText())

        ten = 4.44*f*esp*sfe*n*ind/(10**8)
        ten = float("%.2f" %ten)
        ten = str(ten)

        self.label_7.setText(ten)        
class probarNucleo_3(QDialog):
    def __init__(self, parent):
        super(probarNucleo_3,self).__init__(parent)
        loadUi('calcularEspiras.ui', self)
        self.setWindowTitle("Calcular Espiras de motor")
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        ind = float(self.textEdit_1.toPlainText())
        f = float(self.textEdit_2.toPlainText())
        ten = float(self.textEdit_3.toPlainText())
        sfe = float(self.textEdit_4.toPlainText())
        n = float(self.textEdit_5.toPlainText())

        esp = ten*(10**8)/(4.44*f*ind*sfe*n)
        esp = float("%.2f" %esp)
        esp = str(esp)

        self.label_7.setText(esp) 

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()        
sys.exit(app.exec_())