# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginBjVcMO.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

#import res_rc
usernamelst = []
passwordlst = []
mainlst = []

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(450, 550)
        self.widget = QWidget(LoginWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 370, 480))
        self.widget.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(105,118,132,200);\n"
"}")
        font1 = QFont()
        font1.setPointSize(10)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 300, 420))
        self.label.setStyleSheet(u"border-image:url(background.png);\n"
"border-radius:20px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 300, 420))
        self.label_2.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0,0,0,9), stop:0.375 rgba(0, 0, 0, 50),stop:0.835227 rgba(0,0,0,75));\n"
"border-radius:20px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 60, 280, 390))
        self.label_3.setStyleSheet(u"background-color:rgba(0,0,0,100);\n"
"border-radius:15px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(135, 95, 111, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgba(255,255,255,210);")
        
        self.lineEdit_2 = QLineEdit(self.widget)
        value = self.lineEdit_2.text()
        self.lineEdit_2.setObjectName(u"user")
        self.lineEdit_2.setGeometry(QRect(80, 165, 200, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px\n"
"}\n"
"QLineEdit:hover{\n"
"border:none;\n"
"border-bottom:2px solid rgb(0, 132, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"border:none;\n"
"border-bottom:2px solid rgb(58, 255, 114);\n"
"}\n"
"")
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 230, 200, 40))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px\n"
"}\n"
"QLineEdit:hover{\n"
"border:none;\n"
"border-bottom:2px solid rgb(0, 132, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"border:none;\n"
"border-bottom:2px solid rgb(58, 255, 114);\n"
"}")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 360, 261, 20))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel {\n"
"color:red;\n"
"}")
        self.label_5.setTextFormat(Qt.PlainText)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 310, 200, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.pushButton.clicked.connect(self.button_click)
        self.button_close = QPushButton(self.widget)
        self.button_close.setCursor(Qt.PointingHandCursor)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(260, 40, 45, 21))
        font3 = QFont()
        font3.setFamily(u";")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.button_close.setFont(font3)
        self.button_close.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(53, 50, 67);\n"
"color: rgb(208, 208, 208);\n"
"font: 10pt \\;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)

    
    # setupUi
        #print(self.lineEdit_2.text())

    

        

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"Log In", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"User Name", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("LoginWindow", u"Log In", None))
        self.button_close.setText(QCoreApplication.translate("LoginWindow", u"X", None))
        self.label_5.setText(QCoreApplication.translate("LoginWindow", u"", None))
    def button_click(self):
        # shost is a QString object
        username = self.lineEdit_2.text()
        usernamelst.append(username)
        passwrd = self.lineEdit_3.text()
        passwordlst.append(passwrd)
    mainlst.append(usernamelst)
    mainlst.append(passwordlst)
        
class sing():
    def loginsignal():
        return mainlst      
    # retranslateUi
    
   