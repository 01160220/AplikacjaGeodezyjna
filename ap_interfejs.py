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
        MainWindow.resize(1125, 856)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pixil-frame-0_2_.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.tabWidget_2 = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 1111, 771))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget = QtWidgets.QTabWidget(self.tab)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1111, 851))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.karta_1 = QtWidgets.QWidget()
        self.karta_1.setObjectName("karta_1")
        self.przeliczenie00_3 = QtWidgets.QPushButton(self.karta_1)
        self.przeliczenie00_3.setGeometry(QtCore.QRect(310, 250, 131, 28))
        self.przeliczenie00_3.setObjectName("przeliczenie00_3")
        self.przeliczenie92_2 = QtWidgets.QPushButton(self.karta_1)
        self.przeliczenie92_2.setGeometry(QtCore.QRect(310, 210, 131, 28))
        self.przeliczenie92_2.setObjectName("przeliczenie92_2")
        self.label_6 = QtWidgets.QLabel(self.karta_1)
        self.label_6.setGeometry(QtCore.QRect(50, 260, 16, 16))
        self.label_6.setObjectName("label_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.karta_1)
        self.groupBox_5.setGeometry(QtCore.QRect(230, 50, 111, 81))
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_5)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 91, 51))
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
        self.lam_txt_3 = QtWidgets.QLabel(self.karta_1)
        self.lam_txt_3.setGeometry(QtCore.QRect(25, 220, 41, 20))
        self.lam_txt_3.setMinimumSize(QtCore.QSize(0, 16))
        self.lam_txt_3.setObjectName("lam_txt_3")
        self.przeliczenieXYZ_2 = QtWidgets.QPushButton(self.karta_1)
        self.przeliczenieXYZ_2.setGeometry(QtCore.QRect(310, 170, 131, 28))
        self.przeliczenieXYZ_2.setObjectName("przeliczenieXYZ_2")
        self.fi_txt_3 = QtWidgets.QLabel(self.karta_1)
        self.fi_txt_3.setGeometry(QtCore.QRect(50, 180, 16, 16))
        self.fi_txt_3.setMinimumSize(QtCore.QSize(0, 16))
        self.fi_txt_3.setObjectName("fi_txt_3")
        self.lambda_wprow_3 = QtWidgets.QLineEdit(self.karta_1)
        self.lambda_wprow_3.setGeometry(QtCore.QRect(80, 220, 51, 20))
        self.lambda_wprow_3.setObjectName("lambda_wprow_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.karta_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 260, 51, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.fi_wprow_3 = QtWidgets.QLineEdit(self.karta_1)
        self.fi_wprow_3.setGeometry(QtCore.QRect(80, 180, 51, 20))
        self.fi_wprow_3.setObjectName("fi_wprow_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.karta_1)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 20, 161, 121))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_6)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 141, 91))
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
        self.groupBox_7 = QtWidgets.QGroupBox(self.karta_1)
        self.groupBox_7.setGeometry(QtCore.QRect(490, 160, 261, 131))
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_7)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 241, 101))
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
        self.fi_wprow_4 = QtWidgets.QLineEdit(self.karta_1)
        self.fi_wprow_4.setGeometry(QtCore.QRect(150, 180, 51, 20))
        self.fi_wprow_4.setObjectName("fi_wprow_4")
        self.fi_wprow_5 = QtWidgets.QLineEdit(self.karta_1)
        self.fi_wprow_5.setGeometry(QtCore.QRect(220, 180, 51, 20))
        self.fi_wprow_5.setObjectName("fi_wprow_5")
        self.fi_wprow_6 = QtWidgets.QLineEdit(self.karta_1)
        self.fi_wprow_6.setGeometry(QtCore.QRect(150, 220, 51, 20))
        self.fi_wprow_6.setObjectName("fi_wprow_6")
        self.fi_wprow_7 = QtWidgets.QLineEdit(self.karta_1)
        self.fi_wprow_7.setGeometry(QtCore.QRect(220, 220, 51, 20))
        self.fi_wprow_7.setObjectName("fi_wprow_7")
        self.tabWidget.addTab(self.karta_1, "")
        self.karta_2 = QtWidgets.QWidget()
        self.karta_2.setObjectName("karta_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.karta_2)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 40, 161, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 141, 91))
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
        self.fi_wprow_2.setGeometry(QtCore.QRect(120, 200, 71, 20))
        self.fi_wprow_2.setObjectName("fi_wprow_2")
        self.fi_txt_2 = QtWidgets.QLabel(self.karta_2)
        self.fi_txt_2.setGeometry(QtCore.QRect(90, 200, 16, 16))
        self.fi_txt_2.setMinimumSize(QtCore.QSize(0, 16))
        self.fi_txt_2.setObjectName("fi_txt_2")
        self.lam_txt_2 = QtWidgets.QLabel(self.karta_2)
        self.lam_txt_2.setGeometry(QtCore.QRect(65, 240, 41, 20))
        self.lam_txt_2.setMinimumSize(QtCore.QSize(0, 16))
        self.lam_txt_2.setObjectName("lam_txt_2")
        self.lambda_wprow_2 = QtWidgets.QLineEdit(self.karta_2)
        self.lambda_wprow_2.setGeometry(QtCore.QRect(120, 240, 71, 20))
        self.lambda_wprow_2.setObjectName("lambda_wprow_2")
        self.przeliczenie92 = QtWidgets.QPushButton(self.karta_2)
        self.przeliczenie92.setGeometry(QtCore.QRect(250, 230, 131, 28))
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
        self.label_5.setGeometry(QtCore.QRect(90, 280, 16, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.karta_2)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 70, 111, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 91, 51))
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
        self.lineEdit.setGeometry(QtCore.QRect(120, 280, 71, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.przeliczenie00_2 = QtWidgets.QPushButton(self.karta_2)
        self.przeliczenie00_2.setGeometry(QtCore.QRect(250, 270, 131, 28))
        self.przeliczenie00_2.setObjectName("przeliczenie00_2")
        self.przeliczenieXYZ = QtWidgets.QPushButton(self.karta_2)
        self.przeliczenieXYZ.setGeometry(QtCore.QRect(250, 190, 131, 28))
        self.przeliczenieXYZ.setObjectName("przeliczenieXYZ")
        self.groupBox_4 = QtWidgets.QGroupBox(self.karta_2)
        self.groupBox_4.setGeometry(QtCore.QRect(510, 170, 261, 131))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 241, 101))
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
        self.tabWidget.addTab(self.karta_2, "")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2.addTab(self.tab_2, "")

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikacja Geodezyjna"))
        self.przeliczenie00_3.setText(_translate("MainWindow", "Przelicz do xy2000"))
        self.przeliczenie92_2.setText(_translate("MainWindow", "Przelicz do xy92"))
        self.label_6.setText(_translate("MainWindow", "h"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Wybór strefy"))
        self.radioButton_6.setText(_translate("MainWindow", "5 "))
        self.radioButton_7.setText(_translate("MainWindow", "6"))
        self.radioButton_8.setText(_translate("MainWindow", "7"))
        self.radioButton_9.setText(_translate("MainWindow", "8"))
        self.lam_txt_3.setText(_translate("MainWindow", "Lambda"))
        self.przeliczenieXYZ_2.setText(_translate("MainWindow", "Przelicz do XYZ"))
        self.fi_txt_3.setText(_translate("MainWindow", "Fi"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Elipsoida"))
        self.radioButton_10.setText(_translate("MainWindow", "GRS80"))
        self.wgs_3.setText(_translate("MainWindow", "WGS84"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Wyniki"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.karta_1), _translate("MainWindow", "                                                                      Stopnie, minuty, sekundy                                                                     "))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.karta_2), _translate("MainWindow", "                                                                       Stopnie dziesiętne                                                                          "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Stopnie"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Grady "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

