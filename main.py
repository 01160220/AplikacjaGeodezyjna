# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:49:12 2022

@author: 48518
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from ap_interfejs import *
import math as m
from math import sqrt, radians
import numpy as np

class MyApp(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #8fd970;")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('ikonka.png'))
        self.setWindowIcon(QtGui.QIcon('ikonka.png'))
        
        self.ui.przeliczenie92.clicked.connect(self.obsluga_1992)
        self.ui.przeliczenie00_2.clicked.connect(self.obsluga_2000)
        self.ui.przeliczenieXYZ.clicked.connect(self.obsluga_XYZ)
        
        self.ui.przeliczenie92_2.clicked.connect(self.obsluga_1992_SMS)
        self.ui.przeliczenie00_3.clicked.connect(self.obsluga_2000_SMS)
        self.ui.przeliczenieXYZ_2.clicked.connect(self.obsluga_XYZ_SMS)
        
        self.ui.przeliczenie92_4.clicked.connect(self.obsluga_1992_grad)
        self.ui.przeliczenie00_5.clicked.connect(self.obsluga_2000_grad)
        self.ui.przeliczenieXYZ_4.clicked.connect(self.obsluga_XYZ_grad)
        
        self.ui.przeliczenie92_5.clicked.connect(self.obsluga_1992_rad)
        self.ui.przeliczenie00_6.clicked.connect(self.obsluga_2000_rad)
        self.ui.przeliczenieXYZ_5.clicked.connect(self.obsluga_XYZ_rad)
        self.show()

    def wybor_elipsoidy(self):
        if self.ui.radioButton.isChecked() or self.ui.radioButton_10.isChecked() or self.ui.radioButton_20.isChecked() or self.ui.radioButton_25.isChecked():
            self.a = 6378137.0
            self.b = 6356752.31414036
        elif self.ui.wgs_2.isChecked() or self.ui.wgs_3.isChecked() or self.ui.wgs_6.isChecked() or self.ui.wgs_5.isChecked():
            self.a = 6378137.0 
            self.b = 6356752.31424518 
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Wybierz elipsoide!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
        self.flattening = (self.a - self.b) / self.a
        self.ecc2 = (2 * self.flattening - self.flattening ** 2)
        
    def obsluga_1992(self):
        self.wybor_elipsoidy()
        zmienna = 'stopnie'
        self.wprowadzanie_danych(zmienna)
        self.fi = radians(self.fi)
        self.lam = radians(self.lam)
        self.xy1992()
        self.ui.label.setText('x1992 =' + str(self.x1992) + ' ' + '[m]')
        self.ui.label_2.setText('y1992 =' + str(self.y1992) + ' ' + '[m]')
        self.ui.label_3.setText('')
        
    def obsluga_2000(self):
        self.wybor_elipsoidy()
        zmienna = 'stopnie'
        self.wprowadzanie_danych(zmienna)
        self.fi = radians(self.fi)
        self.lam = radians(self.lam)
        self.xy2000_strefy()
        self.ui.label.setText('x1992 =' + str(self.x2000) + ' ' + '[m]')
        self.ui.label_2.setText('y1992 =' + str(self.y2000) + ' ' + '[m]')
        self.ui.label_3.setText('')
        
    def obsluga_XYZ(self):
        self.wybor_elipsoidy()
        zmienna = 'stopnie'
        self.wprowadzanie_danych(zmienna)   
        self.fi = radians(self.fi)
        self.lam = radians(self.lam)
        self.XYZ(zmienna)
        self.ui.label.setText('X =' + str(self.X) + ' ' + '[m]')
        self.ui.label_2.setText('Y =' + str(self.Y) + ' ' + '[m]')
        self.ui.label_3.setText('Z =' + str(self.Z) + ' ' + '[m]')
    
    def obsluga_1992_SMS(self):
        self.wybor_elipsoidy()
        self.wprowadzanie_SMS()    
        self.xy1992()
        self.ui.label_4.setText('x1992 =' + str(self.x1992) + ' ' + '[m]')
        self.ui.label_7.setText('y1992 =' + str(self.y1992) + ' ' + '[m]')
        self.ui.label_8.setText('')
        
    def obsluga_2000_SMS(self):
        self.wybor_elipsoidy()
        self.wprowadzanie_SMS()    
        self.xy2000_strefy_SMS()
        self.ui.label_4.setText('x1992 =' + str(self.x2000) + ' ' + '[m]')
        self.ui.label_7.setText('y1992 =' + str(self.y2000) + ' ' + '[m]')
        self.ui.label_8.setText('')
        
    def obsluga_XYZ_SMS(self):
        self.wybor_elipsoidy()
        self.wprowadzanie_SMS()   
        self.XYZ_SMS()
        self.ui.label_4.setText('X =' + str(self.X) + ' ' + '[m]')
        self.ui.label_7.setText('Y =' + str(self.Y) + ' ' + '[m]')
        self.ui.label_8.setText('Z =' + str(self.Z) + ' ' + '[m]')
    
    
    def obsluga_1992_grad(self):
        self.wybor_elipsoidy()
        zmienna = 'grady'
        self.wprowadzanie_danych(zmienna) 
        self.fi = self.fi*np.pi/200
        self.lam = self.lam*np.pi/200
        self.xy1992()
        self.ui.label_31.setText('x1992 =' + str(self.x1992) + ' ' + '[m]')
        self.ui.label_32.setText('y1992 =' + str(self.y1992) + ' ' + '[m]')
        self.ui.label_33.setText('')
        
    def obsluga_2000_grad(self):
        self.wybor_elipsoidy()
        zmienna = 'grady'
        self.wprowadzanie_danych(zmienna) 
        self.fi = self.fi*np.pi/200
        self.lam = self.lam*np.pi/200
        self.xy2000_strefy()
        self.ui.label_31.setText('x1992 =' + str(self.x2000) + ' ' + '[m]')
        self.ui.label_32.setText('y1992 =' + str(self.y2000) + ' ' + '[m]')
        self.ui.label_33.setText('')
        
    def obsluga_XYZ_grad(self):
        self.wybor_elipsoidy()
        zmienna = 'grady'
        self.wprowadzanie_danych(zmienna)   
        self.fi = self.fi*np.pi/200
        self.lam = self.lam*np.pi/200
        self.XYZ(zmienna)
        self.ui.label_31.setText('X =' + str(self.X) + ' ' + '[m]')
        self.ui.label_32.setText('Y =' + str(self.Y) + ' ' + '[m]')
        self.ui.label_33.setText('Z =' + str(self.Z) + ' ' + '[m]')
    
     
    def obsluga_1992_rad(self):
        self.wybor_elipsoidy()
        zmienna = 'radiany'
        self.wprowadzanie_danych(zmienna) 
        self.fi = radians(self.fi)
        self.lam = radians(self.lam)
        self.xy1992()
        self.ui.label_39.setText('x1992 =' + str(self.x1992) + ' ' + '[m]')
        self.ui.label_40.setText('y1992 =' + str(self.y1992) + ' ' + '[m]')
        self.ui.label_41.setText('')
        
    def obsluga_2000_rad(self):
        self.wybor_elipsoidy()
        zmienna = 'radiany'
        self.wprowadzanie_danych(zmienna) 
        self.fi = radians(self.fi)
        self.lam = radians(self.lam)
        self.xy2000_strefy()
        self.ui.label_39.setText('x1992 =' + str(self.x2000) + ' ' + '[m]')
        self.ui.label_40.setText('y1992 =' + str(self.y2000) + ' ' + '[m]')
        self.ui.label_41.setText('')
        
    def obsluga_XYZ_rad(self):
        self.wybor_elipsoidy()
        zmienna = 'radiany'
        self.wprowadzanie_danych(zmienna)   
        self.fi = radians(self.fi)
        self.lam = radians(self.lam)
        self.XYZ(zmienna)
        self.ui.label_39.setText('X =' + str(self.X) + ' ' + '[m]')
        self.ui.label_40.setText('Y =' + str(self.Y) + ' ' + '[m]')
        self.ui.label_41.setText('Z =' + str(self.Z) + ' ' + '[m]')


    def wprowadzanie_danych(self,zmienna):
        if zmienna == 'stopnie':
            dlugosc_fi = len(self.ui.fi_wprow_2.text())
            wartosc_fi = float(self.ui.fi_wprow_2.text())
            dol_fi = 49
            gora_fi = 54.8333
            dol_lam = 14.1167
            gora_lam = 24.15
        elif zmienna == 'grady':
            dlugosc_fi = len(self.ui.fi_wprow_9.text())
            wartosc_fi = float(self.ui.fi_wprow_9.text())
            dol_fi = 54.4444
            gora_fi = 60.9259
            dol_lam = 15.6852
            gora_lam = 26.8333
        elif zmienna == 'radiany':
            dlugosc_fi = len(self.ui.fi_wprow_10.text())
            wartosc_fi = float(self.ui.fi_wprow_10.text())
            dol_fi = 0.855211
            gora_fi = 0.957022
            dol_lam = 0.246383
            gora_lam = 0.421497
        
    
        if dlugosc_fi != 0 and wartosc_fi >= dol_fi and wartosc_fi <= gora_fi: # zakres na phi <49 stopni, 54 stopni 50 minut>
            self.fi = wartosc_fi
        elif dlugosc_fi == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Wprowadz fi!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Zakres fi jest nieprawidłowy!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
        
        
        if zmienna == 'stopnie':
            dlugosc_lam = len(self.ui.lambda_wprow_2.text())
            wartosc_fi = float(self.ui.lambda_wprow_2.text())
        if zmienna == 'grady':
            dlugosc_lam = len(self.ui.lambda_wprow_5.text())
            wartosc_fi = float(self.ui.lambda_wprow_5.text())
        if zmienna == 'radiany':
            dlugosc_lam = len(self.ui.lambda_wprow_6.text())
            wartosc_fi = float(self.ui.lambda_wprow_6.text())
            
        if dlugosc_lam != 0 and wartosc_fi >= dol_lam and wartosc_fi <= gora_lam: # zakres na lambda <14 stopni 07 minut, 24 stopnie 09 minut>
            self.lam = wartosc_fi
        elif dlugosc_lam == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Wprowadz lambda!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Zakres lambda jest nieprawidłowy!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
        
    
    def wprowadzanie_SMS(self):
        # stopnie fi
        if len(self.ui.fi_wprow_3.text()) != 0 and float(self.ui.fi_wprow_3.text()) >= 49 and float(self.ui.fi_wprow_3.text()) <= 54.8333: # zakres na phi <49 stopni, 54 stopni 50 minut>
            fi_1 = float(self.ui.fi_wprow_3.text())
            #minuty fi
            if len(self.ui.fi_wprow_4.text()) != 0 and float(self.ui.fi_wprow_4.text()) >= 0 and float(self.ui.fi_wprow_4.text()) < 60: # zakres na phi <49 stopni, 54 stopni 50 minut>
                fi_2 = float(self.ui.fi_wprow_4.text())
            elif len(self.ui.fi_wprow_4.text()) == 0:
                fi_2 = 0
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
                msg.setText('Zakres minuty_fi jest nieprawidłowy!')
                msg.setInformativeText
                msg.setWindowTitle("Sprawdź wprowadzone dane!")
                msg.exec_()
            
            #sekundfy fi
            if len(self.ui.fi_wprow_5.text()) != 0 and float(self.ui.fi_wprow_5.text()) >= 0 and float(self.ui.fi_wprow_5.text()) < 60: # zakres na phi <49 stopni, 54 stopni 50 minut>
                fi_3 = float(self.ui.fi_wprow_5.text())
            elif len(self.ui.fi_wprow_5.text()) == 0:
                fi_3 = 0
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
                msg.setText('Zakres sekundy_fi jest nieprawidłowy!')
                msg.setInformativeText
                msg.setWindowTitle("Sprawdź wprowadzone dane!")
                msg.exec_()
        elif len(self.ui.fi_wprow_2.text()) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Wprowadz fi!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Zakres stopnie_fi jest nieprawidłowy!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
        
        #stopnie lambda
        if len(self.ui.lambda_wprow_3.text()) != 0 and float(self.ui.lambda_wprow_3.text()) >= 14.1167 and float(self.ui.lambda_wprow_3.text()) <= 24.15: # zakres na lambda <14 stopni 07 minut, 24 stopnie 09 minut>
            lam_1 = float(self.ui.lambda_wprow_3.text())
            #minuty lambda
            if len(self.ui.fi_wprow_6.text()) != 0 and len(self.ui.fi_wprow_6.text()) >= 0 and len(self.ui.fi_wprow_6.text()) < 60:
                lam_2 = float(self.ui.fi_wprow_4.text())
            elif len(self.ui.fi_wprow_6.text()) == 0:
                lam_2 = 0
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
                msg.setText('Zakres minuty_lambda jest nieprawidłowy!')
                msg.setInformativeText
                msg.setWindowTitle("Sprawdź wprowadzone dane!")
                msg.exec_()
            
            #sekundy lambda
            if len(self.ui.fi_wprow_7.text()) != 0 and len(self.ui.fi_wprow_7.text()) >= 0 and len(self.ui.fi_wprow_7.text()) < 60:
                lam_3 = float(self.ui.fi_wprow_7.text())
            elif len(self.ui.fi_wprow_7.text()) == 0:
                lam_3 = 0
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
                msg.setText('Zakres sekundy_fi jest nieprawidłowy!')
                msg.setInformativeText
                msg.setWindowTitle("Sprawdź wprowadzone dane!")
                msg.exec_()
        elif len(self.ui.lambda_wprow_2.text()) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Wprowadz lambda!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Zakres stopnie_lambda jest nieprawidłowy!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
        
        
        self.fi = radians(fi_1+(fi_2/60)+(fi_3/3600))
        self.lam = radians(lam_1+(lam_2/60)+(lam_3/3600))
    
    def xy1992(self):
        lam0 = radians(19)
        b2 = (self.a**2)*(1 - self.ecc2)
        ep2 = ((self.a**2 - b2))/(b2)
        t = np.tan(self.fi)
        n2 = ep2 * ((np.cos(self.fi))**2)
        N =  self.a / (np.sqrt(1 - self.ecc2 * (np.sin(self.fi)) ** 2))
        A0 = 1-(self.ecc2/4) - ((3*(self.ecc2**2))/64)-((5*(self.ecc2**3))/256)
        A2 = (3/8)*(self.ecc2+((self.ecc2**2)/4)+((15*(self.ecc2**3))/128))
        A4 = (15/256)*((self.ecc2**2)+((3*(self.ecc2**3))/4))
        A6 = (35*(self.ecc2**3))/3072
        dlam = self.lam - lam0
        sigma = self.a * (A0 * (self.fi) - (A2 * np.sin(2 * self.fi)) + (A4 * np.sin(4 * self.fi)) - (A6 * np.sin(6 * self.fi)))
        xgk = sigma + ((dlam**2)/2) * N * np.sin(self.fi) * np.cos(self.fi) * (1 + ((dlam**2)/12) * ((np.cos(self.fi))**2) * (5 - t**2 + 9 * n2 + 4 * (n2**2)) + ((dlam**4)/360) * ((np.cos(self.fi))**4) * (61 - (58 * (t**2)) + (t**4) + (270 * n2) - (330 * n2 * (t**2))))
        ygk = dlam * (N * np.cos(self.fi)) * (1 + ((((dlam**2)/6) * (np.cos(self.fi))**2) * (1 - t**2 + n2)) + (((dlam**4)/(120)) * (np.cos(self.fi)**4)) * (5 - (18 * (t**2)) + (t**4) + (14 * n2) - (58 * n2 * (t**2))))
        m0 = 0.9993
        self.x1992 = round((xgk * m0) - 5300000, 5)
        self.y1992 = round((ygk * m0) + 500000, 5)
        
    def xy2000_strefy(self):
        if self.ui.radioButton_2.isChecked() or self.ui.radioButton_16.isChecked() or self.ui.radioButton_21.isChecked():
            self.strefa_00 = 5
            self.lam_0 = 15
            self.xy2000()
            
        elif self.ui.radioButton_3.isChecked() or self.ui.radioButton_17.isChecked() or self.ui.radioButton_22.isChecked():
            self.strefa_00 = 6
            self.lam_0 = 18
            self.xy2000()
            
        elif self.ui.radioButton_4.isChecked() or self.ui.radioButton_18.isChecked() or self.ui.radioButton_23.isChecked():
            self.strefa_00 = 7
            self.lam_0 = 21
            self.xy2000()
            
        elif self.ui.radioButton_5.isChecked() or self.ui.radioButton_19.isChecked() or self.ui.radioButton_24.isChecked():
            self.strefa_00 = 8
            self.lam_0 = 24
            self.xy2000()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Wybierz strefe!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
            
    def xy2000_strefy_SMS(self):        
        if self.ui.radioButton_6.isChecked():
            self.strefa_00 = 5
            self.lam_0 = 15
            self.xy2000()
            
        elif self.ui.radioButton_7.isChecked():
            self.strefa_00 = 6
            self.lam_0 = 18
            self.xy2000()
            
        elif self.ui.radioButton_8.isChecked():
            self.strefa_00 = 7
            self.lam_0 = 21
            self.xy2000()
            
        elif self.ui.radioButton_9.isChecked():
            self.strefa_00 = 8
            self.lam_0 = 24
            self.xy2000()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Wybierz strefe!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()

    def xy2000(self):
        b2 = (self.a**2)*(1 - self.ecc2)
        ep2 = ((self.a**2 - b2))/(b2)
        t = np.tan(self.fi)
        n2 = ep2 * ((np.cos(self.fi))**2)
        N =  self.a / (np.sqrt(1 - self.ecc2 * (np.sin(self.fi)) ** 2))
        A0 = 1-(self.ecc2/4) - ((3*(self.ecc2**2))/64)-((5*(self.ecc2**3))/256)
        A2 = (3/8)*(self.ecc2+((self.ecc2**2)/4)+((15*(self.ecc2**3))/128))
        A4 = (15/256)*((self.ecc2**2)+((3*(self.ecc2**3))/4))
        A6 = (35*(self.ecc2**3))/3072
        lam_0 = radians(self.lam_0)
        dlam_00 = self.lam - lam_0
        sigma = self.a * (A0 * (self.fi) - (A2 * np.sin(2 * self.fi)) + (A4 * np.sin(4 * self.fi)) - (A6 * np.sin(6 * self.fi)))
        xgk_00 = sigma + ((dlam_00**2)/2) * N * np.sin(self.fi) * np.cos(self.fi) * (1 + ((dlam_00**2)/12) * ((np.cos(self.fi))**2) * (5 - t**2 + 9 * n2 + 4 * (n2**2)) + ((dlam_00**4)/360) * ((np.cos(self.fi))**4) * (61 - (58 * (t**2)) + (t**4) + (270 * n2) - (330 * n2 * (t**2))))
        ygk_00 = dlam_00 * (N * np.cos(self.fi)) * (1 + ((((dlam_00**2)/6) * (np.cos(self.fi))**2) * (1 - t**2 + n2)) + (((dlam_00**4)/(120)) * (np.cos(self.fi)**4)) * (5 - (18 * (t**2)) + (t**4) + (14 * n2) - (58 * n2 * (t**2))))
        m_00 = 0.999923 #skala PL-2000
        self.x2000 = round((xgk_00 * m_00), 5)
        self.y2000 = round(((ygk_00 * m_00) + (self.strefa_00 * 1000000) + 500000), 5)
       
    def XYZ(self,zmienna):
        if zmienna == 'stopnie':
            dlugosc_h = len(self.ui.lineEdit.text())
            wartosc_h = float(self.ui.lineEdit.text())
        if zmienna == 'grady':
            dlugosc_h = len(self.ui.lineEdit_4.text())
            wartosc_h = float(self.ui.lineEdit_4.text())
        if zmienna == 'radiany':
            dlugosc_h = len(self.ui.lineEdit_5.text())
            wartosc_h = float(self.ui.lineEdit_5.text())
            
        if dlugosc_h != 0:
            self.hel = wartosc_h
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Wprowadź h!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
            
        N =  self.a / (sqrt(1 - self.ecc2 * (np.sin(self.fi)) ** 2))
        
        self.X = round(((N + self.hel) * np.cos(self.fi) * np.cos(self.lam)), 3)
        self.Y = round(((N + self.hel) * np.cos(self.fi) * np.sin(self.lam)), 3)
        self.Z = round(((N * (1 - self.ecc2) + self.hel) * np.sin(self.fi)), 3)
        
    def XYZ_SMS(self):
        if len(self.ui.lineEdit_2.text()) != 0:
            self.hel = float(self.ui.lineEdit_2.text())
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('wykrzyknik.png'))
            msg.setText('Wprowadź h!')
            msg.setInformativeText
            msg.setWindowTitle("Sprawdź wprowadzone dane!")
            msg.exec_()
            
        N =  self.a / (sqrt(1 - self.ecc2 * (np.sin(self.fi)) ** 2))
        
        self.X = round(((N + self.hel) * np.cos(self.fi) * np.cos(self.lam)), 3)
        self.Y = round(((N + self.hel) * np.cos(self.fi) * np.sin(self.lam)), 3)
        self.Z = round(((N * (1 - self.ecc2) + self.hel) * np.sin(self.fi)), 3)
        
        

    













if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())
