# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apinterfejs.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 318)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pixil-frame-0_2_.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.tabWidget_2 = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 641, 311))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget = QtWidgets.QTabWidget(self.tab)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 631, 281))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.karta_1 = QtWidgets.QWidget()
        self.karta_1.setObjectName("karta_1")
        self.label_15 = QtWidgets.QLabel(self.karta_1)
        self.label_15.setGeometry(QtCore.QRect(40, 10, 141, 141))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("ikonka.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.karta_1)
        self.label_16.setGeometry(QtCore.QRect(20, 220, 16, 16))
        self.label_16.setObjectName("label_16")
        self.groupBox_11 = QtWidgets.QGroupBox(self.karta_1)
        self.groupBox_11.setGeometry(QtCore.QRect(250, 30, 91, 71))
        self.groupBox_11.setObjectName("groupBox_11")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_11)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 71, 41))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_8.setObjectName("radioButton_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_9.setObjectName("radioButton_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.radioButton_9)
        self.lam_txt_5 = QtWidgets.QLabel(self.karta_1)
        self.lam_txt_5.setGeometry(QtCore.QRect(0, 190, 51, 20))
        self.lam_txt_5.setMinimumSize(QtCore.QSize(0, 16))
        self.lam_txt_5.setObjectName("lam_txt_5")
        self.fi_txt_5 = QtWidgets.QLabel(self.karta_1)
        self.fi_txt_5.setGeometry(QtCore.QRect(20, 160, 16, 16))
        self.fi_txt_5.setMinimumSize(QtCore.QSize(0, 16))
        self.fi_txt_5.setObjectName("fi_txt_5")
        self.groupBox_12 = QtWidgets.QGroupBox(self.karta_1)
        self.groupBox_12.setGeometry(QtCore.QRect(410, 0, 211, 121))
        self.groupBox_12.setObjectName("groupBox_12")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_12)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 191, 91))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_10 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout_4.addWidget(self.radioButton_10)
        self.wgs_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.wgs_3.setObjectName("wgs_3")
        self.verticalLayout_4.addWidget(self.wgs_3)
        self.groupBox_13 = QtWidgets.QGroupBox(self.karta_1)
        self.groupBox_13.setGeometry(QtCore.QRect(410, 120, 211, 131))
        self.groupBox_13.setObjectName("groupBox_13")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_13)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 191, 101))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.przeliczenieXYZ_2 = QtWidgets.QPushButton(self.karta_1)
        self.przeliczenieXYZ_2.setGeometry(QtCore.QRect(230, 160, 131, 21))
        self.przeliczenieXYZ_2.setObjectName("przeliczenieXYZ_2")
        self.przeliczenie92_2 = QtWidgets.QPushButton(self.karta_1)
        self.przeliczenie92_2.setGeometry(QtCore.QRect(230, 190, 131, 21))
        self.przeliczenie92_2.setObjectName("przeliczenie92_2")
        self.przeliczenie00_3 = QtWidgets.QPushButton(self.karta_1)
        self.przeliczenie00_3.setGeometry(QtCore.QRect(230, 220, 131, 21))
        self.przeliczenie00_3.setObjectName("przeliczenie00_3")
        self.fi_wprow_3 = QtWidgets.QLineEdit(self.karta_1)
        self.fi_wprow_3.setGeometry(QtCore.QRect(40, 160, 41, 21))
        self.fi_wprow_3.setObjectName("fi_wprow_3")
        self.fi_wprow_4 = QtWidgets.QLineEdit(self.karta_1)
        self.fi_wprow_4.setGeometry(QtCore.QRect(100, 160, 41, 20))
        self.fi_wprow_4.setObjectName("fi_wprow_4")
        self.fi_wprow_5 = QtWidgets.QLineEdit(self.karta_1)
        self.fi_wprow_5.setGeometry(QtCore.QRect(160, 160, 41, 20))
        self.fi_wprow_5.setObjectName("fi_wprow_5")
        self.lambda_wprow_3 = QtWidgets.QLineEdit(self.karta_1)
        self.lambda_wprow_3.setGeometry(QtCore.QRect(40, 190, 41, 20))
        self.lambda_wprow_3.setObjectName("lambda_wprow_3")
        self.fi_wprow_6 = QtWidgets.QLineEdit(self.karta_1)
        self.fi_wprow_6.setGeometry(QtCore.QRect(100, 190, 41, 20))
        self.fi_wprow_6.setObjectName("fi_wprow_6")
        self.fi_wprow_7 = QtWidgets.QLineEdit(self.karta_1)
        self.fi_wprow_7.setGeometry(QtCore.QRect(160, 190, 41, 20))
        self.fi_wprow_7.setObjectName("fi_wprow_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.karta_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 220, 51, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.karta_1)
        self.label_6.setGeometry(QtCore.QRect(90, 160, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_19 = QtWidgets.QLabel(self.karta_1)
        self.label_19.setGeometry(QtCore.QRect(100, 230, 47, 13))
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(self.karta_1)
        self.label_21.setGeometry(QtCore.QRect(90, 190, 16, 16))
        self.label_21.setObjectName("label_21")
        self.label_17 = QtWidgets.QLabel(self.karta_1)
        self.label_17.setGeometry(QtCore.QRect(150, 160, 16, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.karta_1)
        self.label_18.setGeometry(QtCore.QRect(150, 190, 16, 16))
        self.label_18.setObjectName("label_18")
        self.label_22 = QtWidgets.QLabel(self.karta_1)
        self.label_22.setGeometry(QtCore.QRect(210, 160, 16, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.karta_1)
        self.label_23.setGeometry(QtCore.QRect(210, 190, 16, 16))
        self.label_23.setObjectName("label_23")
        self.tabWidget.addTab(self.karta_1, "")
        self.karta_2 = QtWidgets.QWidget()
        self.karta_2.setObjectName("karta_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.karta_2)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 0, 211, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 191, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.wgs_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.wgs_2.setObjectName("wgs_2")
        self.verticalLayout_2.addWidget(self.wgs_2)
        self.fi_wprow_2 = QtWidgets.QLineEdit(self.karta_2)
        self.fi_wprow_2.setGeometry(QtCore.QRect(90, 160, 91, 21))
        self.fi_wprow_2.setObjectName("fi_wprow_2")
        self.fi_txt_2 = QtWidgets.QLabel(self.karta_2)
        self.fi_txt_2.setGeometry(QtCore.QRect(60, 160, 16, 16))
        self.fi_txt_2.setMinimumSize(QtCore.QSize(0, 16))
        self.fi_txt_2.setObjectName("fi_txt_2")
        self.lam_txt_2 = QtWidgets.QLabel(self.karta_2)
        self.lam_txt_2.setGeometry(QtCore.QRect(30, 190, 51, 20))
        self.lam_txt_2.setMinimumSize(QtCore.QSize(0, 16))
        self.lam_txt_2.setObjectName("lam_txt_2")
        self.lambda_wprow_2 = QtWidgets.QLineEdit(self.karta_2)
        self.lambda_wprow_2.setGeometry(QtCore.QRect(90, 190, 91, 21))
        self.lambda_wprow_2.setObjectName("lambda_wprow_2")
        self.przeliczenie92 = QtWidgets.QPushButton(self.karta_2)
        self.przeliczenie92.setGeometry(QtCore.QRect(230, 190, 131, 21))
        self.przeliczenie92.setObjectName("przeliczenie92")
        self.x_92_wynik = QtWidgets.QLabel(self.karta_2)
        self.x_92_wynik.setGeometry(QtCore.QRect(370, 240, 47, 13))
        self.x_92_wynik.setText("")
        self.x_92_wynik.setObjectName("x_92_wynik")
        self.y_92_wynik_2 = QtWidgets.QLabel(self.karta_2)
        self.y_92_wynik_2.setGeometry(QtCore.QRect(370, 260, 47, 13))
        self.y_92_wynik_2.setText("")
        self.y_92_wynik_2.setObjectName("y_92_wynik_2")
        self.label_5 = QtWidgets.QLabel(self.karta_2)
        self.label_5.setGeometry(QtCore.QRect(50, 220, 16, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.karta_2)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 30, 91, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 71, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.radioButton_5)
        self.lineEdit = QtWidgets.QLineEdit(self.karta_2)
        self.lineEdit.setGeometry(QtCore.QRect(90, 220, 91, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.przeliczenie00_2 = QtWidgets.QPushButton(self.karta_2)
        self.przeliczenie00_2.setGeometry(QtCore.QRect(230, 220, 131, 21))
        self.przeliczenie00_2.setObjectName("przeliczenie00_2")
        self.przeliczenieXYZ = QtWidgets.QPushButton(self.karta_2)
        self.przeliczenieXYZ.setGeometry(QtCore.QRect(230, 160, 131, 21))
        self.przeliczenieXYZ.setObjectName("przeliczenieXYZ")
        self.groupBox_4 = QtWidgets.QGroupBox(self.karta_2)
        self.groupBox_4.setGeometry(QtCore.QRect(410, 120, 211, 131))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 191, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_9 = QtWidgets.QLabel(self.karta_2)
        self.label_9.setGeometry(QtCore.QRect(40, 10, 141, 141))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("ikonka.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_20 = QtWidgets.QLabel(self.karta_2)
        self.label_20.setGeometry(QtCore.QRect(190, 160, 16, 16))
        self.label_20.setObjectName("label_20")
        self.label_24 = QtWidgets.QLabel(self.karta_2)
        self.label_24.setGeometry(QtCore.QRect(190, 190, 16, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.karta_2)
        self.label_25.setGeometry(QtCore.QRect(190, 220, 16, 16))
        self.label_25.setObjectName("label_25")
        self.tabWidget.addTab(self.karta_2, "")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.przeliczenie00_5 = QtWidgets.QPushButton(self.tab_2)
        self.przeliczenie00_5.setGeometry(QtCore.QRect(230, 240, 131, 21))
        self.przeliczenie00_5.setObjectName("przeliczenie00_5")
        self.przeliczenie92_4 = QtWidgets.QPushButton(self.tab_2)
        self.przeliczenie92_4.setGeometry(QtCore.QRect(230, 210, 131, 21))
        self.przeliczenie92_4.setObjectName("przeliczenie92_4")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(190, 170, 16, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(190, 240, 16, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(40, 30, 141, 141))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("ikonka.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(190, 200, 16, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(50, 240, 16, 16))
        self.label_30.setObjectName("label_30")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(250, 50, 91, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_5)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 71, 42))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.radioButton_16 = QtWidgets.QRadioButton(self.formLayoutWidget_4)
        self.radioButton_16.setObjectName("radioButton_16")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_16)
        self.radioButton_17 = QtWidgets.QRadioButton(self.formLayoutWidget_4)
        self.radioButton_17.setObjectName("radioButton_17")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radioButton_17)
        self.radioButton_18 = QtWidgets.QRadioButton(self.formLayoutWidget_4)
        self.radioButton_18.setObjectName("radioButton_18")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_18)
        self.radioButton_19 = QtWidgets.QRadioButton(self.formLayoutWidget_4)
        self.radioButton_19.setObjectName("radioButton_19")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.radioButton_19)
        self.przeliczenieXYZ_4 = QtWidgets.QPushButton(self.tab_2)
        self.przeliczenieXYZ_4.setGeometry(QtCore.QRect(230, 180, 131, 21))
        self.przeliczenieXYZ_4.setObjectName("przeliczenieXYZ_4")
        self.lam_txt_3 = QtWidgets.QLabel(self.tab_2)
        self.lam_txt_3.setGeometry(QtCore.QRect(30, 210, 51, 20))
        self.lam_txt_3.setMinimumSize(QtCore.QSize(0, 16))
        self.lam_txt_3.setObjectName("lam_txt_3")
        self.fi_txt_3 = QtWidgets.QLabel(self.tab_2)
        self.fi_txt_3.setGeometry(QtCore.QRect(60, 180, 16, 16))
        self.fi_txt_3.setMinimumSize(QtCore.QSize(0, 16))
        self.fi_txt_3.setObjectName("fi_txt_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 240, 91, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lambda_wprow_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lambda_wprow_5.setGeometry(QtCore.QRect(90, 210, 91, 21))
        self.lambda_wprow_5.setObjectName("lambda_wprow_5")
        self.fi_wprow_9 = QtWidgets.QLineEdit(self.tab_2)
        self.fi_wprow_9.setGeometry(QtCore.QRect(90, 180, 91, 21))
        self.fi_wprow_9.setObjectName("fi_wprow_9")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(410, 20, 211, 121))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.groupBox_6)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 20, 191, 91))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.radioButton_20 = QtWidgets.QRadioButton(self.verticalLayoutWidget_8)
        self.radioButton_20.setObjectName("radioButton_20")
        self.verticalLayout_8.addWidget(self.radioButton_20)
        self.wgs_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_8)
        self.wgs_5.setObjectName("wgs_5")
        self.verticalLayout_8.addWidget(self.wgs_5)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(410, 140, 211, 131))
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.groupBox_7)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 20, 191, 101))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_9.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_9.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_9.addWidget(self.label_33)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.przeliczenie00_6 = QtWidgets.QPushButton(self.tab_3)
        self.przeliczenie00_6.setGeometry(QtCore.QRect(230, 240, 131, 21))
        self.przeliczenie00_6.setObjectName("przeliczenie00_6")
        self.przeliczenie92_5 = QtWidgets.QPushButton(self.tab_3)
        self.przeliczenie92_5.setGeometry(QtCore.QRect(230, 210, 131, 21))
        self.przeliczenie92_5.setObjectName("przeliczenie92_5")
        self.label_34 = QtWidgets.QLabel(self.tab_3)
        self.label_34.setGeometry(QtCore.QRect(190, 180, 21, 16))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.tab_3)
        self.label_35.setGeometry(QtCore.QRect(190, 240, 16, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab_3)
        self.label_36.setGeometry(QtCore.QRect(40, 30, 141, 141))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("ikonka.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tab_3)
        self.label_37.setGeometry(QtCore.QRect(190, 210, 21, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.tab_3)
        self.label_38.setGeometry(QtCore.QRect(50, 240, 16, 16))
        self.label_38.setObjectName("label_38")
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_14.setGeometry(QtCore.QRect(250, 50, 91, 71))
        self.groupBox_14.setObjectName("groupBox_14")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_14)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 71, 42))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.radioButton_21 = QtWidgets.QRadioButton(self.formLayoutWidget_5)
        self.radioButton_21.setObjectName("radioButton_21")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_21)
        self.radioButton_22 = QtWidgets.QRadioButton(self.formLayoutWidget_5)
        self.radioButton_22.setObjectName("radioButton_22")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radioButton_22)
        self.radioButton_23 = QtWidgets.QRadioButton(self.formLayoutWidget_5)
        self.radioButton_23.setObjectName("radioButton_23")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_23)
        self.radioButton_24 = QtWidgets.QRadioButton(self.formLayoutWidget_5)
        self.radioButton_24.setObjectName("radioButton_24")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.radioButton_24)
        self.przeliczenieXYZ_5 = QtWidgets.QPushButton(self.tab_3)
        self.przeliczenieXYZ_5.setGeometry(QtCore.QRect(230, 180, 131, 21))
        self.przeliczenieXYZ_5.setObjectName("przeliczenieXYZ_5")
        self.lam_txt_6 = QtWidgets.QLabel(self.tab_3)
        self.lam_txt_6.setGeometry(QtCore.QRect(30, 210, 51, 20))
        self.lam_txt_6.setMinimumSize(QtCore.QSize(0, 16))
        self.lam_txt_6.setObjectName("lam_txt_6")
        self.fi_txt_6 = QtWidgets.QLabel(self.tab_3)
        self.fi_txt_6.setGeometry(QtCore.QRect(60, 180, 16, 16))
        self.fi_txt_6.setMinimumSize(QtCore.QSize(0, 16))
        self.fi_txt_6.setObjectName("fi_txt_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 240, 91, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lambda_wprow_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lambda_wprow_6.setGeometry(QtCore.QRect(90, 210, 91, 21))
        self.lambda_wprow_6.setObjectName("lambda_wprow_6")
        self.fi_wprow_10 = QtWidgets.QLineEdit(self.tab_3)
        self.fi_wprow_10.setGeometry(QtCore.QRect(90, 180, 91, 21))
        self.fi_wprow_10.setObjectName("fi_wprow_10")
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_15.setGeometry(QtCore.QRect(410, 20, 211, 121))
        self.groupBox_15.setObjectName("groupBox_15")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.groupBox_15)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(10, 20, 191, 91))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.radioButton_25 = QtWidgets.QRadioButton(self.verticalLayoutWidget_10)
        self.radioButton_25.setObjectName("radioButton_25")
        self.verticalLayout_10.addWidget(self.radioButton_25)
        self.wgs_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget_10)
        self.wgs_6.setObjectName("wgs_6")
        self.verticalLayout_10.addWidget(self.wgs_6)
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_16.setGeometry(QtCore.QRect(410, 140, 211, 131))
        self.groupBox_16.setObjectName("groupBox_16")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.groupBox_16)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(10, 20, 191, 101))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_39 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_11.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_11.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_11.addWidget(self.label_41)
        self.tabWidget_2.addTab(self.tab_3, "")

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikacja Geodezyjna"))
        self.label_16.setText(_translate("MainWindow", "h"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Wybór strefy"))
        self.radioButton_6.setText(_translate("MainWindow", "5 "))
        self.radioButton_7.setText(_translate("MainWindow", "6"))
        self.radioButton_8.setText(_translate("MainWindow", "7"))
        self.radioButton_9.setText(_translate("MainWindow", "8"))
        self.lam_txt_5.setText(_translate("MainWindow", "Lambda"))
        self.fi_txt_5.setText(_translate("MainWindow", "Fi"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Elipsoida"))
        self.radioButton_10.setText(_translate("MainWindow", "GRS80"))
        self.wgs_3.setText(_translate("MainWindow", "WGS84"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Wyniki"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.przeliczenieXYZ_2.setText(_translate("MainWindow", "Przelicz do XYZ"))
        self.przeliczenie92_2.setText(_translate("MainWindow", "Przelicz do xy92"))
        self.przeliczenie00_3.setText(_translate("MainWindow", "Przelicz do xy2000"))
        self.label_6.setText(_translate("MainWindow", "°"))
        self.label_19.setText(_translate("MainWindow", "m"))
        self.label_21.setText(_translate("MainWindow", "°"))
        self.label_17.setText(_translate("MainWindow", "\'"))
        self.label_18.setText(_translate("MainWindow", "\'"))
        self.label_22.setText(_translate("MainWindow", "\""))
        self.label_23.setText(_translate("MainWindow", "\""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.karta_1), _translate("MainWindow", "Stopnie, minuty, sekundy"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Elipsoida"))
        self.radioButton.setText(_translate("MainWindow", "GRS80"))
        self.wgs_2.setText(_translate("MainWindow", "WGS84"))
        self.fi_txt_2.setText(_translate("MainWindow", "Fi"))
        self.lam_txt_2.setText(_translate("MainWindow", "Lambda"))
        self.przeliczenie92.setText(_translate("MainWindow", "Przelicz do xy92"))
        self.label_5.setText(_translate("MainWindow", "h"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Wybór strefy"))
        self.radioButton_2.setText(_translate("MainWindow", "5 "))
        self.radioButton_3.setText(_translate("MainWindow", "6"))
        self.radioButton_4.setText(_translate("MainWindow", "7"))
        self.radioButton_5.setText(_translate("MainWindow", "8"))
        self.przeliczenie00_2.setText(_translate("MainWindow", "Przelicz do xy2000"))
        self.przeliczenieXYZ.setText(_translate("MainWindow", "Przelicz do XYZ"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Wyniki"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "°"))
        self.label_24.setText(_translate("MainWindow", "°"))
        self.label_25.setText(_translate("MainWindow", "m"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.karta_2), _translate("MainWindow", "Stopnie dziesiętne "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Stopnie"))
        self.przeliczenie00_5.setText(_translate("MainWindow", "Przelicz do xy2000"))
        self.przeliczenie92_4.setText(_translate("MainWindow", "Przelicz do xy92"))
        self.label_26.setText(_translate("MainWindow", "g"))
        self.label_27.setText(_translate("MainWindow", "m"))
        self.label_29.setText(_translate("MainWindow", "g"))
        self.label_30.setText(_translate("MainWindow", "h"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Wybór strefy"))
        self.radioButton_16.setText(_translate("MainWindow", "5 "))
        self.radioButton_17.setText(_translate("MainWindow", "6"))
        self.radioButton_18.setText(_translate("MainWindow", "7"))
        self.radioButton_19.setText(_translate("MainWindow", "8"))
        self.przeliczenieXYZ_4.setText(_translate("MainWindow", "Przelicz do XYZ"))
        self.lam_txt_3.setText(_translate("MainWindow", "Lambda"))
        self.fi_txt_3.setText(_translate("MainWindow", "Fi"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Elipsoida"))
        self.radioButton_20.setText(_translate("MainWindow", "GRS80"))
        self.wgs_5.setText(_translate("MainWindow", "WGS84"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Wyniki"))
        self.label_31.setText(_translate("MainWindow", "TextLabel"))
        self.label_32.setText(_translate("MainWindow", "TextLabel"))
        self.label_33.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Grady "))
        self.przeliczenie00_6.setText(_translate("MainWindow", "Przelicz do xy2000"))
        self.przeliczenie92_5.setText(_translate("MainWindow", "Przelicz do xy92"))
        self.label_34.setText(_translate("MainWindow", "rad"))
        self.label_35.setText(_translate("MainWindow", "m"))
        self.label_37.setText(_translate("MainWindow", "rad"))
        self.label_38.setText(_translate("MainWindow", "h"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Wybór strefy"))
        self.radioButton_21.setText(_translate("MainWindow", "5 "))
        self.radioButton_22.setText(_translate("MainWindow", "6"))
        self.radioButton_23.setText(_translate("MainWindow", "7"))
        self.radioButton_24.setText(_translate("MainWindow", "8"))
        self.przeliczenieXYZ_5.setText(_translate("MainWindow", "Przelicz do XYZ"))
        self.lam_txt_6.setText(_translate("MainWindow", "Lambda"))
        self.fi_txt_6.setText(_translate("MainWindow", "Fi"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Elipsoida"))
        self.radioButton_25.setText(_translate("MainWindow", "GRS80"))
        self.wgs_6.setText(_translate("MainWindow", "WGS84"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Wyniki"))
        self.label_39.setText(_translate("MainWindow", "TextLabel"))
        self.label_40.setText(_translate("MainWindow", "TextLabel"))
        self.label_41.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Radiany"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

