# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindows(object):
    def setupUi(self, MainWindows):
        if not MainWindows.objectName():
            MainWindows.setObjectName(u"MainWindows")
        MainWindows.resize(1120, 620)
        MainWindows.setMinimumSize(QSize(900, 400))
        MainWindows.setStyleSheet(u"* {\n"
"border: none;\n"
"}\n"
"\n"
"#top { border-top-left-radius: 4px; border-top-right-radius: 4px; }\n"
"#side_bar { border-bottom-left-radius: 4px; }\n"
"#bottom { border-bottom-right-radius: 4px }\n"
"\n"
"#top {\n"
"background: #212634;\n"
"}\n"
"\n"
"\n"
"#side_bar {\n"
"background: #212634;\n"
"}\n"
"#toggle_bar {\n"
"background: #212634;\n"
"}\n"
"\n"
"#page_container {\n"
"background: #293546;\n"
"}\n"
"\n"
"#bottom {\n"
"background: #89a;\n"
"}\n"
"\n"
"QLabel {\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton {\n"
"background: #212634;\n"
"color: #fff;\n"
"}\n"
"\n"
"#side_bar QPushButton:hover, #toggle_bar QLabel:hover {\n"
"background: #293546;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/********************************/\n"
"#btn_toggle { image: url(:/icons/assets/icons/toggle menu.png); }\n"
"#btn_compras { image: url(:/icons/assets/icons/compras.png); }\n"
"#btn_ventas { image: url(:/icons/assets/icons/ventas.png); }\n"
"#btn_productos { image: url(:/icons/assets/icons/productos.png); }\n"
"#btn_"
                        "proveedores { image: url(:/icons/assets/icons/proveedores.png); }\n"
"#btn_tickets { image: url(:/icons/assets/icons/tickets.png); }\n"
"#btn_recorte_caja { image: url(:/icons/assets/icons/corte caja.png); }\n"
"#btn_copia_seguridad { image: url(:/icons/assets/icons/backup.png); }\n"
"\n"
"#box_size { image: url(:/icons/assets/icons/resize.png); }\n"
"\n"
"\n"
"#btn_usuario { image: url(:/icons/assets/icons/profile.png); }\n"
"\n"
"#btn_minimized { image: url(:/icons/assets/icons/minimized.png); }\n"
"#btn_maximized { image: url(:/icons/assets/icons/maximized.png); }\n"
"#btn_closed { image: url(:/icons/assets/icons/closed.png); }\n"
"\n"
"\n"
"\n"
"#btn_minimized:hover, #btn_maximized:hover,  #btn_closed:hover {\n"
"background: #293546;\n"
"}\n"
"\n"
"\n"
"/********************************/")
        self.main = QWidget(MainWindows)
        self.main.setObjectName(u"main")
        self.main.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.App = QFrame(self.main)
        self.App.setObjectName(u"App")
        self.App.setFrameShape(QFrame.StyledPanel)
        self.App.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.App)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.App)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 45))
        self.top.setMaximumSize(QSize(16777215, 45))
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.top.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.box_logo = QFrame(self.top)
        self.box_logo.setObjectName(u"box_logo")
        self.box_logo.setEnabled(True)
        self.box_logo.setMinimumSize(QSize(60, 45))
        self.box_logo.setMaximumSize(QSize(60, 45))
        self.box_logo.setToolTipDuration(0)
        self.box_logo.setFrameShape(QFrame.StyledPanel)
        self.box_logo.setFrameShadow(QFrame.Raised)
        self.box_logo.setLineWidth(1)
        self.logo = QFrame(self.box_logo)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(9, 2, 42, 42))
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.box_logo)

        self.box_title = QFrame(self.top)
        self.box_title.setObjectName(u"box_title")
        self.box_title.setMaximumSize(QSize(16777215, 45))
        self.box_title.setLayoutDirection(Qt.LeftToRight)
        self.box_title.setFrameShape(QFrame.StyledPanel)
        self.box_title.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.box_title)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.box_title)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setMargin(0)
        self.title.setIndent(10)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.box_title)

        self.right_top_buttons = QFrame(self.top)
        self.right_top_buttons.setObjectName(u"right_top_buttons")
        self.right_top_buttons.setMaximumSize(QSize(150, 45))
        self.right_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.right_top_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.right_top_buttons)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 10, 10, 0)
        self.btn_usuario = QPushButton(self.right_top_buttons)
        self.btn_usuario.setObjectName(u"btn_usuario")
        self.btn_usuario.setMinimumSize(QSize(28, 28))
        self.btn_usuario.setMaximumSize(QSize(28, 16777215))

        self.horizontalLayout_4.addWidget(self.btn_usuario)

        self.btn_minimized = QPushButton(self.right_top_buttons)
        self.btn_minimized.setObjectName(u"btn_minimized")
        self.btn_minimized.setMinimumSize(QSize(28, 28))
        self.btn_minimized.setMaximumSize(QSize(28, 16777215))

        self.horizontalLayout_4.addWidget(self.btn_minimized)

        self.btn_maximized = QPushButton(self.right_top_buttons)
        self.btn_maximized.setObjectName(u"btn_maximized")
        self.btn_maximized.setMinimumSize(QSize(28, 28))
        self.btn_maximized.setMaximumSize(QSize(28, 16777215))

        self.horizontalLayout_4.addWidget(self.btn_maximized)

        self.btn_closed = QPushButton(self.right_top_buttons)
        self.btn_closed.setObjectName(u"btn_closed")
        self.btn_closed.setMinimumSize(QSize(28, 28))
        self.btn_closed.setMaximumSize(QSize(28, 16777215))

        self.horizontalLayout_4.addWidget(self.btn_closed)


        self.horizontalLayout.addWidget(self.right_top_buttons)


        self.verticalLayout_2.addWidget(self.top)

        self.container = QFrame(self.App)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.side_bar = QFrame(self.container)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setMinimumSize(QSize(45, 0))
        self.side_bar.setMaximumSize(QSize(60, 16777215))
        self.side_bar.setFrameShape(QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.side_bar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.side_bar)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setMinimumSize(QSize(0, 60))

        self.verticalLayout_4.addWidget(self.btn_toggle)

        self.btn_compras = QPushButton(self.side_bar)
        self.btn_compras.setObjectName(u"btn_compras")
        self.btn_compras.setMinimumSize(QSize(0, 60))

        self.verticalLayout_4.addWidget(self.btn_compras)

        self.btn_ventas = QPushButton(self.side_bar)
        self.btn_ventas.setObjectName(u"btn_ventas")
        self.btn_ventas.setMinimumSize(QSize(0, 60))

        self.verticalLayout_4.addWidget(self.btn_ventas)

        self.btn_productos = QPushButton(self.side_bar)
        self.btn_productos.setObjectName(u"btn_productos")
        self.btn_productos.setMinimumSize(QSize(0, 60))

        self.verticalLayout_4.addWidget(self.btn_productos)

        self.btn_proveedores = QPushButton(self.side_bar)
        self.btn_proveedores.setObjectName(u"btn_proveedores")
        self.btn_proveedores.setMinimumSize(QSize(0, 60))

        self.verticalLayout_4.addWidget(self.btn_proveedores)

        self.btn_tickets = QPushButton(self.side_bar)
        self.btn_tickets.setObjectName(u"btn_tickets")
        self.btn_tickets.setMinimumSize(QSize(45, 60))

        self.verticalLayout_4.addWidget(self.btn_tickets)

        self.btn_recorte_caja = QPushButton(self.side_bar)
        self.btn_recorte_caja.setObjectName(u"btn_recorte_caja")
        self.btn_recorte_caja.setMinimumSize(QSize(45, 60))

        self.verticalLayout_4.addWidget(self.btn_recorte_caja)

        self.btn_copia_seguridad = QPushButton(self.side_bar)
        self.btn_copia_seguridad.setObjectName(u"btn_copia_seguridad")
        self.btn_copia_seguridad.setMinimumSize(QSize(45, 60))

        self.verticalLayout_4.addWidget(self.btn_copia_seguridad)

        self.frame = QFrame(self.side_bar)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.side_bar)

        self.toggle_bar = QFrame(self.container)
        self.toggle_bar.setObjectName(u"toggle_bar")
        self.toggle_bar.setMaximumSize(QSize(0, 16777215))
        self.toggle_bar.setFrameShape(QFrame.StyledPanel)
        self.toggle_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.toggle_bar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbl_toggle = QLabel(self.toggle_bar)
        self.lbl_toggle.setObjectName(u"lbl_toggle")
        self.lbl_toggle.setMinimumSize(QSize(150, 60))
        self.lbl_toggle.setMaximumSize(QSize(16777215, 60))
        self.lbl_toggle.setIndent(10)

        self.verticalLayout_5.addWidget(self.lbl_toggle)

        self.lbl_ventas = QLabel(self.toggle_bar)
        self.lbl_ventas.setObjectName(u"lbl_ventas")
        self.lbl_ventas.setMinimumSize(QSize(150, 60))
        self.lbl_ventas.setMaximumSize(QSize(16777215, 60))
        self.lbl_ventas.setIndent(10)

        self.verticalLayout_5.addWidget(self.lbl_ventas)

        self.lbl_compras = QLabel(self.toggle_bar)
        self.lbl_compras.setObjectName(u"lbl_compras")
        self.lbl_compras.setMinimumSize(QSize(150, 60))
        self.lbl_compras.setMaximumSize(QSize(16777215, 60))
        self.lbl_compras.setIndent(10)

        self.verticalLayout_5.addWidget(self.lbl_compras)

        self.lbl_productos = QLabel(self.toggle_bar)
        self.lbl_productos.setObjectName(u"lbl_productos")
        self.lbl_productos.setMinimumSize(QSize(150, 60))
        self.lbl_productos.setMaximumSize(QSize(16777215, 60))
        self.lbl_productos.setIndent(10)

        self.verticalLayout_5.addWidget(self.lbl_productos)

        self.lbl_proveedores = QLabel(self.toggle_bar)
        self.lbl_proveedores.setObjectName(u"lbl_proveedores")
        self.lbl_proveedores.setMinimumSize(QSize(150, 60))
        self.lbl_proveedores.setMaximumSize(QSize(16777215, 60))
        self.lbl_proveedores.setIndent(10)

        self.verticalLayout_5.addWidget(self.lbl_proveedores)

        self.lbl_tickets = QLabel(self.toggle_bar)
        self.lbl_tickets.setObjectName(u"lbl_tickets")
        self.lbl_tickets.setMinimumSize(QSize(150, 60))
        self.lbl_tickets.setMaximumSize(QSize(16777215, 60))
        self.lbl_tickets.setIndent(10)

        self.verticalLayout_5.addWidget(self.lbl_tickets)

        self.lbl_recorte_caja = QLabel(self.toggle_bar)
        self.lbl_recorte_caja.setObjectName(u"lbl_recorte_caja")
        self.lbl_recorte_caja.setMinimumSize(QSize(150, 60))
        self.lbl_recorte_caja.setMaximumSize(QSize(16777215, 60))
        self.lbl_recorte_caja.setIndent(10)

        self.verticalLayout_5.addWidget(self.lbl_recorte_caja)

        self.lbl_copia_seguridad = QLabel(self.toggle_bar)
        self.lbl_copia_seguridad.setObjectName(u"lbl_copia_seguridad")
        self.lbl_copia_seguridad.setMinimumSize(QSize(150, 60))
        self.lbl_copia_seguridad.setMaximumSize(QSize(16777215, 60))
        self.lbl_copia_seguridad.setIndent(10)

        self.verticalLayout_5.addWidget(self.lbl_copia_seguridad)

        self.frame_2 = QFrame(self.toggle_bar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.toggle_bar)

        self.content = QFrame(self.container)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page_container = QFrame(self.content)
        self.page_container.setObjectName(u"page_container")
        self.page_container.setFrameShape(QFrame.StyledPanel)
        self.page_container.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.page_container)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(self.page_container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_ventas = QWidget()
        self.page_ventas.setObjectName(u"page_ventas")
        self.label = QLabel(self.page_ventas)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(400, 200, 55, 16))
        self.stackedWidget.addWidget(self.page_ventas)
        self.page_compras = QWidget()
        self.page_compras.setObjectName(u"page_compras")
        self.label_3 = QLabel(self.page_compras)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 200, 55, 16))
        self.stackedWidget.addWidget(self.page_compras)
        self.page_productos = QWidget()
        self.page_productos.setObjectName(u"page_productos")
        self.label_4 = QLabel(self.page_productos)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 140, 55, 16))
        self.stackedWidget.addWidget(self.page_productos)
        self.page_proveedores = QWidget()
        self.page_proveedores.setObjectName(u"page_proveedores")
        self.label_5 = QLabel(self.page_proveedores)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 160, 55, 16))
        self.stackedWidget.addWidget(self.page_proveedores)
        self.page_tickets = QWidget()
        self.page_tickets.setObjectName(u"page_tickets")
        self.label_6 = QLabel(self.page_tickets)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 120, 55, 16))
        self.stackedWidget.addWidget(self.page_tickets)
        self.page_recorte_caja = QWidget()
        self.page_recorte_caja.setObjectName(u"page_recorte_caja")
        self.label_7 = QLabel(self.page_recorte_caja)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(420, 140, 55, 16))
        self.stackedWidget.addWidget(self.page_recorte_caja)
        self.page_copia_seguridad = QWidget()
        self.page_copia_seguridad.setObjectName(u"page_copia_seguridad")
        self.label_8 = QLabel(self.page_copia_seguridad)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(350, 130, 55, 16))
        self.stackedWidget.addWidget(self.page_copia_seguridad)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.label_9 = QLabel(self.page_admin)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(360, 180, 55, 16))
        self.stackedWidget.addWidget(self.page_admin)
        self.page_empleado = QWidget()
        self.page_empleado.setObjectName(u"page_empleado")
        self.label_10 = QLabel(self.page_empleado)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 120, 55, 16))
        self.stackedWidget.addWidget(self.page_empleado)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.page_container)

        self.bottom = QFrame(self.content)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMaximumSize(QSize(16777215, 22))
        self.bottom.setFrameShape(QFrame.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottom)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.box_under_description = QFrame(self.bottom)
        self.box_under_description.setObjectName(u"box_under_description")
        self.box_under_description.setFrameShape(QFrame.StyledPanel)
        self.box_under_description.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.box_under_description)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.box_under_description)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMargin(0)
        self.label_2.setIndent(10)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.box_under_description)

        self.box_version = QFrame(self.bottom)
        self.box_version.setObjectName(u"box_version")
        self.box_version.setMaximumSize(QSize(150, 16777215))
        self.box_version.setFrameShape(QFrame.StyledPanel)
        self.box_version.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.box_version)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.box_version)
        self.version.setObjectName(u"version")
        self.version.setMargin(0)
        self.version.setIndent(10)

        self.gridLayout_3.addWidget(self.version, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.box_version)

        self.box_size = QFrame(self.bottom)
        self.box_size.setObjectName(u"box_size")
        self.box_size.setMaximumSize(QSize(18, 16777215))
        self.box_size.setFrameShape(QFrame.StyledPanel)
        self.box_size.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.box_size)


        self.verticalLayout_3.addWidget(self.bottom)


        self.horizontalLayout_2.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.container)


        self.verticalLayout.addWidget(self.App)

        MainWindows.setCentralWidget(self.main)

        self.retranslateUi(MainWindows)

        self.stackedWidget.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(MainWindows)
    # setupUi

    def retranslateUi(self, MainWindows):
        MainWindows.setWindowTitle(QCoreApplication.translate("MainWindows", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindows", u"Ba\u00f1os Charly", None))
        self.btn_usuario.setText("")
        self.btn_minimized.setText("")
        self.btn_maximized.setText("")
        self.btn_closed.setText("")
        self.btn_toggle.setText("")
        self.btn_compras.setText("")
        self.btn_ventas.setText("")
        self.btn_productos.setText("")
        self.btn_proveedores.setText("")
        self.btn_tickets.setText("")
        self.btn_recorte_caja.setText("")
        self.btn_copia_seguridad.setText("")
        self.lbl_toggle.setText(QCoreApplication.translate("MainWindows", u"Toggle", None))
        self.lbl_ventas.setText(QCoreApplication.translate("MainWindows", u"Ventas", None))
        self.lbl_compras.setText(QCoreApplication.translate("MainWindows", u"Compras", None))
        self.lbl_productos.setText(QCoreApplication.translate("MainWindows", u"Productos", None))
        self.lbl_proveedores.setText(QCoreApplication.translate("MainWindows", u"Proveedores", None))
        self.lbl_tickets.setText(QCoreApplication.translate("MainWindows", u"Tickets", None))
        self.lbl_recorte_caja.setText(QCoreApplication.translate("MainWindows", u"Recorte de caja", None))
        self.lbl_copia_seguridad.setText(QCoreApplication.translate("MainWindows", u"Copia de seguridad", None))
        self.label.setText(QCoreApplication.translate("MainWindows", u"ventas", None))
        self.label_3.setText(QCoreApplication.translate("MainWindows", u"compras", None))
        self.label_4.setText(QCoreApplication.translate("MainWindows", u"productos", None))
        self.label_5.setText(QCoreApplication.translate("MainWindows", u"proveedores", None))
        self.label_6.setText(QCoreApplication.translate("MainWindows", u"tickets", None))
        self.label_7.setText(QCoreApplication.translate("MainWindows", u"recorte de caja", None))
        self.label_8.setText(QCoreApplication.translate("MainWindows", u"copia de seguridad", None))
        self.label_9.setText(QCoreApplication.translate("MainWindows", u"admin", None))
        self.label_10.setText(QCoreApplication.translate("MainWindows", u"empleado", None))
        self.label_2.setText(QCoreApplication.translate("MainWindows", u"Team Lost Souls", None))
        self.version.setText(QCoreApplication.translate("MainWindows", u"V. 1.5.3", None))
    # retranslateUi

