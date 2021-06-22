# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(274, 394)
        Dialog.setStyleSheet(u"* {\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"#App {\n"
"background: #212634;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"#line, #line_2 {\n"
"background: #fff;\n"
"}\n"
"\n"
"QLabel {\n"
"color: #fff;\n"
"}\n"
"\n"
"#btn_accept {\n"
"background: #2A91FF;\n"
"color: #fff;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#btn_closed {\n"
" background: #FF5C67;\n"
"	image: url(:/icons/assets/icons/closed.png);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background: transparent;\n"
"color: #fff;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QDialog QDialog QPushButton, QDialog QDialog QPushButton:hover, QDialog QDialog QPushButton:focus {\n"
"    background: #2A91FF;\n"
"    border-radius: 5px;\n"
"	color: #fff;\n"
"	font-size: 18px;\n"
"	width: 80px;\n"
"}\n"
"\n"
"QDialog QDialog {\n"
"	background-color: #212634;\n"
"}\n"
"\n"
"QDialog QDialog QLabel {\n"
"	font: 17px;\n"
"	color: #eaeaea;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.App = QFrame(Dialog)
        self.App.setObjectName(u"App")
        self.App.setFrameShape(QFrame.StyledPanel)
        self.App.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.App)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 20, 191, 31))
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)
        self.User = QLineEdit(self.App)
        self.User.setObjectName(u"User")
        self.User.setGeometry(QRect(60, 130, 150, 30))
        font1 = QFont()
        font1.setFamilies([u"Bell MT"])
        font1.setPointSize(12)
        self.User.setFont(font1)
        self.label = QLabel(self.App)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 110, 151, 16))
        self.label.setFont(font1)
        self.Password = QLineEdit(self.App)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(60, 230, 150, 30))
        self.Password.setFont(font1)
        self.Password.setInputMethodHints(Qt.ImhHiddenText)
        self.label_2 = QLabel(self.App)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 210, 151, 20))
        self.label_2.setFont(font1)
        self.btn_accept = QPushButton(self.App)
        self.btn_accept.setObjectName(u"btn_accept")
        self.btn_accept.setGeometry(QRect(60, 320, 150, 40))
        font2 = QFont()
        font2.setFamilies([u"Bell MT"])
        font2.setPointSize(13)
        self.btn_accept.setFont(font2)
        self.btn_accept.setCursor(QCursor(Qt.PointingHandCursor))
        self.line = QFrame(self.App)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(60, 160, 150, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.btn_closed = QPushButton(self.App)
        self.btn_closed.setObjectName(u"btn_closed")
        self.btn_closed.setGeometry(QRect(230, 20, 30, 30))
        self.btn_closed.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_2 = QFrame(self.App)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(60, 270, 150, 3))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.App)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Ba\u00f1os Charly", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a", None))
        self.btn_accept.setText(QCoreApplication.translate("Dialog", u"Iniciar Sesi\u00f3n", None))
        self.btn_closed.setText("")
    # retranslateUi

