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
        MainWindows.resize(1100, 600)
        MainWindows.setMinimumSize(QSize(900, 500))
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
"#side_bar QPushButton {\n"
"background: transparent;\n"
"}\n"
"\n"
"#lbl_toggle, #lbl_ventas, #lbl_compras, #lbl_productos, #lbl_proveedores, #lbl_tickets, #lbl_recorte_caja, #lbl_copia_seguridad {\n"
"Text-align:left;\n"
"margin-left:22px;\n"
"}\n"
"\n"
"#side_bar QFrame QLabel {\n"
"\n"
"}\n"
"\n"
"#side_bar QFrame:hover {\n"
"background: #293546;\n"
"}\n"
"\n"
"\n"
"\n"
"/********************************/\n"
"#btn_toggle { image: url(:/icons/assets/icons/toggle menu.png); }\n"
"#btn_c"
                        "ompras { image: url(:/icons/assets/icons/compras.png); }\n"
"#btn_ventas { image: url(:/icons/assets/icons/ventas.png); }\n"
"#btn_productos { image: url(:/icons/assets/icons/productos.png); }\n"
"#btn_proveedores { image: url(:/icons/assets/icons/proveedores.png); }\n"
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
"#btn_minimized, #btn_maximized, #btn_closed { border-radius: 4px; }\n"
"\n"
"#btn_minimized:hover, #btn_maximized:hover,  #btn_closed:hover { background: #293546; }\n"
"\n"
"\n"
"/"
                        "********************************/\n"
"\n"
"\n"
"\n"
"#page_proveedores, #page_tickets, #page_recorte_caja, #page_copia_seguridad, #page_admin, #page_empleado {\n"
"background: #333;\n"
"}\n"
"\n"
"QScrollArea {\n"
"background: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollArea QPushButton {\n"
"image: url(:/icons/assets/icons/remove.png);\n"
"background: #FF5C67;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#page_container QLabel, #page_container QLineEdit {\n"
"font: 12pt;\n"
"background: transparent;\n"
"color: white;\n"
"}\n"
"\n"
"#ventas_agregar, #compras_agregar {\n"
"background: #2A91FF;\n"
"border-radius: 5px;\n"
"}\n"
"#ventas_generar, #compras_generar {\n"
"background: #2EAC4B;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QDateEdit {\n"
"background: transparent;\n"
"border-bottom 1px solid red;\n"
"font: 12pt;\n"
"color: #fff;\n"
"}\n"
"\n"
"QDateEdit::down-button, QDateEdit::up-button { image: none; }\n"
"\n"
"QComboBox {\n"
"background: #212634;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {"
                        " \n"
"image: url(:/icons/assets/icons/arrow-down.png);\n"
"margin-top: 5px;\n"
"margin-bottom: 4px;\n"
"	width: 25px; \n"
"	border-left-width: 2px;\n"
"	border-left-color: #374553;\n"
"	border-left-style: solid;\n"
"}\n"
"\n"
"QDoubleSpinBox, QSpinBox {\n"
"background:transparent;\n"
"color: #fff;\n"
"font:11pt;\n"
"}\n"
"QDoubleSpinBox::down-button, QDoubleSpinBox::up-button { image: none; }\n"
"QSpinBox::down-button, QSpinBox::up-button { image: none; }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#productos_stacked > QWidget {\n"
"border: 2px solid #38C3DD;\n"
"border-radius: 5px;\n"
"border-top-left-radius: 0px;\n"
"background: transparent;\n"
"}\n"
"\n"
"#box_productos_top_buttons  > QPushButton{\n"
"background: transparent;\n"
"border: 2px solid #38C3DD;\n"
"border-radius: 5px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizonta"
                        "l {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #707070;\n"
"    width: 8px;\n"
"    margin: 0px;\n"
"	border-radius: 4px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: #"
                        "38C3DD;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 0px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    height: 0px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: none; }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QC"
                        "heckBox::indicator {\n"
"    border: 3px solid #D0D9DC;\n"
"	width: 17px;\n"
"	height: 17px;\n"
"	border-radius: 5px;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    /*border: 3px solid rgb(58, 66, 81);*/\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border: 3px solid #38C3DD;\n"
"	image: url(:/icons/assets/icons/check.png);\n"
"}\n"
"\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"\n"
"QTextEdit {\n"
"background: #212634;\n"
"color: #fff;\n"
"}\n"
"\n"
"")
        self.main = QWidget(MainWindows)
        self.main.setObjectName(u"main")
        self.main.setLayoutDirection(Qt.LeftToRight)
        self.main.setStyleSheet(u"#line, #line_1, #line_2, #line_3, #line_4, #line_5, #line_6, #line_7, #line_8, #line9, #line_10,\n"
"#line_11, #line_12, #line_13, #line_14, #line_15, #line_16, #line_17, #line_18, #line_19, #line_20,\n"
"#line_21, #line_22, #line_23, #line_24, #line_25, #line_26, #line_27, #line_28, #line_29, #line_30,\n"
"#line_31, #line_32, #line_33, #line_34, #line_35, #line_36, #line_37, #line_38, #line_39, #line_40,\n"
"#line_41, #line_42, #line_43, #line_44, #line_45, #line_46, #line_47, #line_48, #line_49, #line_50 {\n"
"background: #fff;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.btn_usuario.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_usuario)

        self.btn_minimized = QPushButton(self.right_top_buttons)
        self.btn_minimized.setObjectName(u"btn_minimized")
        self.btn_minimized.setMinimumSize(QSize(28, 28))
        self.btn_minimized.setMaximumSize(QSize(28, 16777215))
        self.btn_minimized.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_minimized)

        self.btn_maximized = QPushButton(self.right_top_buttons)
        self.btn_maximized.setObjectName(u"btn_maximized")
        self.btn_maximized.setMinimumSize(QSize(28, 28))
        self.btn_maximized.setMaximumSize(QSize(28, 16777215))
        self.btn_maximized.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_maximized)

        self.btn_closed = QPushButton(self.right_top_buttons)
        self.btn_closed.setObjectName(u"btn_closed")
        self.btn_closed.setMinimumSize(QSize(28, 28))
        self.btn_closed.setMaximumSize(QSize(28, 16777215))
        self.btn_closed.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.side_bar.setMaximumSize(QSize(45, 16777215))
        self.side_bar.setFrameShape(QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.side_bar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.box_toggle = QFrame(self.side_bar)
        self.box_toggle.setObjectName(u"box_toggle")
        self.box_toggle.setMinimumSize(QSize(45, 0))
        self.box_toggle.setMaximumSize(QSize(200, 16777215))
        self.box_toggle.setFrameShape(QFrame.StyledPanel)
        self.box_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.box_toggle)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.box_toggle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setMinimumSize(QSize(45, 60))
        self.btn_toggle.setMaximumSize(QSize(45, 16777215))
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.btn_toggle)

        self.lbl_toggle = QPushButton(self.box_toggle)
        self.lbl_toggle.setObjectName(u"lbl_toggle")
        self.lbl_toggle.setMinimumSize(QSize(155, 60))
        self.lbl_toggle.setMaximumSize(QSize(155, 16777215))
        self.lbl_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.lbl_toggle.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_6.addWidget(self.lbl_toggle)

        self.lbl_toggle.raise_()
        self.btn_toggle.raise_()

        self.verticalLayout_4.addWidget(self.box_toggle)

        self.box_ventas = QFrame(self.side_bar)
        self.box_ventas.setObjectName(u"box_ventas")
        self.box_ventas.setMinimumSize(QSize(45, 60))
        self.box_ventas.setFrameShape(QFrame.StyledPanel)
        self.box_ventas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.box_ventas)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_ventas = QPushButton(self.box_ventas)
        self.btn_ventas.setObjectName(u"btn_ventas")
        self.btn_ventas.setMinimumSize(QSize(45, 60))
        self.btn_ventas.setMaximumSize(QSize(45, 16777215))
        self.btn_ventas.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.btn_ventas, 0, Qt.AlignLeft)

        self.lbl_ventas = QPushButton(self.box_ventas)
        self.lbl_ventas.setObjectName(u"lbl_ventas")
        self.lbl_ventas.setMinimumSize(QSize(155, 60))
        self.lbl_ventas.setMaximumSize(QSize(155, 16777215))
        self.lbl_ventas.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.lbl_ventas, 0, Qt.AlignLeft)

        self.lbl_ventas.raise_()
        self.btn_ventas.raise_()

        self.verticalLayout_4.addWidget(self.box_ventas, 0, Qt.AlignLeft)

        self.box_compras = QFrame(self.side_bar)
        self.box_compras.setObjectName(u"box_compras")
        self.box_compras.setFrameShape(QFrame.StyledPanel)
        self.box_compras.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.box_compras)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_compras = QPushButton(self.box_compras)
        self.btn_compras.setObjectName(u"btn_compras")
        self.btn_compras.setMinimumSize(QSize(45, 60))
        self.btn_compras.setMaximumSize(QSize(45, 16777215))
        self.btn_compras.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.btn_compras)

        self.lbl_compras = QPushButton(self.box_compras)
        self.lbl_compras.setObjectName(u"lbl_compras")
        self.lbl_compras.setMinimumSize(QSize(155, 60))
        self.lbl_compras.setMaximumSize(QSize(155, 16777215))
        self.lbl_compras.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.lbl_compras, 0, Qt.AlignLeft)

        self.lbl_compras.raise_()
        self.btn_compras.raise_()

        self.verticalLayout_4.addWidget(self.box_compras, 0, Qt.AlignLeft)

        self.box_productos = QFrame(self.side_bar)
        self.box_productos.setObjectName(u"box_productos")
        self.box_productos.setFrameShape(QFrame.StyledPanel)
        self.box_productos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.box_productos)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_productos = QPushButton(self.box_productos)
        self.btn_productos.setObjectName(u"btn_productos")
        self.btn_productos.setMinimumSize(QSize(45, 60))
        self.btn_productos.setMaximumSize(QSize(45, 16777215))
        self.btn_productos.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.btn_productos)

        self.lbl_productos = QPushButton(self.box_productos)
        self.lbl_productos.setObjectName(u"lbl_productos")
        self.lbl_productos.setMinimumSize(QSize(155, 60))
        self.lbl_productos.setMaximumSize(QSize(155, 16777215))
        self.lbl_productos.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.lbl_productos, 0, Qt.AlignLeft)

        self.lbl_productos.raise_()
        self.btn_productos.raise_()

        self.verticalLayout_4.addWidget(self.box_productos, 0, Qt.AlignLeft)

        self.box_proveedores = QFrame(self.side_bar)
        self.box_proveedores.setObjectName(u"box_proveedores")
        self.box_proveedores.setFrameShape(QFrame.StyledPanel)
        self.box_proveedores.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.box_proveedores)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_proveedores = QPushButton(self.box_proveedores)
        self.btn_proveedores.setObjectName(u"btn_proveedores")
        self.btn_proveedores.setMinimumSize(QSize(45, 60))
        self.btn_proveedores.setMaximumSize(QSize(45, 16777215))
        self.btn_proveedores.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.btn_proveedores)

        self.lbl_proveedores = QPushButton(self.box_proveedores)
        self.lbl_proveedores.setObjectName(u"lbl_proveedores")
        self.lbl_proveedores.setMinimumSize(QSize(155, 60))
        self.lbl_proveedores.setMaximumSize(QSize(155, 16777215))
        self.lbl_proveedores.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.lbl_proveedores, 0, Qt.AlignLeft)

        self.lbl_proveedores.raise_()
        self.btn_proveedores.raise_()

        self.verticalLayout_4.addWidget(self.box_proveedores, 0, Qt.AlignLeft)

        self.box_tickets = QFrame(self.side_bar)
        self.box_tickets.setObjectName(u"box_tickets")
        self.box_tickets.setFrameShape(QFrame.StyledPanel)
        self.box_tickets.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.box_tickets)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_tickets = QPushButton(self.box_tickets)
        self.btn_tickets.setObjectName(u"btn_tickets")
        self.btn_tickets.setMinimumSize(QSize(45, 60))
        self.btn_tickets.setMaximumSize(QSize(45, 16777215))
        self.btn_tickets.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.btn_tickets)

        self.lbl_tickets = QPushButton(self.box_tickets)
        self.lbl_tickets.setObjectName(u"lbl_tickets")
        self.lbl_tickets.setMinimumSize(QSize(155, 60))
        self.lbl_tickets.setMaximumSize(QSize(155, 16777215))
        self.lbl_tickets.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.lbl_tickets, 0, Qt.AlignLeft)

        self.lbl_tickets.raise_()
        self.btn_tickets.raise_()

        self.verticalLayout_4.addWidget(self.box_tickets)

        self.box_recorte_caja = QFrame(self.side_bar)
        self.box_recorte_caja.setObjectName(u"box_recorte_caja")
        self.box_recorte_caja.setFrameShape(QFrame.StyledPanel)
        self.box_recorte_caja.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.box_recorte_caja)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_recorte_caja = QPushButton(self.box_recorte_caja)
        self.btn_recorte_caja.setObjectName(u"btn_recorte_caja")
        self.btn_recorte_caja.setMinimumSize(QSize(45, 60))
        self.btn_recorte_caja.setMaximumSize(QSize(45, 16777215))
        self.btn_recorte_caja.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_recorte_caja)

        self.lbl_recorte_caja = QPushButton(self.box_recorte_caja)
        self.lbl_recorte_caja.setObjectName(u"lbl_recorte_caja")
        self.lbl_recorte_caja.setMinimumSize(QSize(155, 60))
        self.lbl_recorte_caja.setMaximumSize(QSize(155, 16777215))
        self.lbl_recorte_caja.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.lbl_recorte_caja, 0, Qt.AlignLeft)

        self.lbl_recorte_caja.raise_()
        self.btn_recorte_caja.raise_()

        self.verticalLayout_4.addWidget(self.box_recorte_caja)

        self.box_copia_seguridad = QFrame(self.side_bar)
        self.box_copia_seguridad.setObjectName(u"box_copia_seguridad")
        self.box_copia_seguridad.setFrameShape(QFrame.StyledPanel)
        self.box_copia_seguridad.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.box_copia_seguridad)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btn_copia_seguridad = QPushButton(self.box_copia_seguridad)
        self.btn_copia_seguridad.setObjectName(u"btn_copia_seguridad")
        self.btn_copia_seguridad.setMinimumSize(QSize(45, 60))
        self.btn_copia_seguridad.setMaximumSize(QSize(45, 16777215))
        self.btn_copia_seguridad.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.btn_copia_seguridad)

        self.lbl_copia_seguridad = QPushButton(self.box_copia_seguridad)
        self.lbl_copia_seguridad.setObjectName(u"lbl_copia_seguridad")
        self.lbl_copia_seguridad.setMinimumSize(QSize(155, 60))
        self.lbl_copia_seguridad.setMaximumSize(QSize(155, 16777215))
        self.lbl_copia_seguridad.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.lbl_copia_seguridad, 0, Qt.AlignLeft)

        self.lbl_copia_seguridad.raise_()
        self.btn_copia_seguridad.raise_()

        self.verticalLayout_4.addWidget(self.box_copia_seguridad)

        self.frame = QFrame(self.side_bar)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.side_bar)

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
        self.verticalLayout_6 = QVBoxLayout(self.page_ventas)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.box_ventas_top = QFrame(self.page_ventas)
        self.box_ventas_top.setObjectName(u"box_ventas_top")
        self.box_ventas_top.setMinimumSize(QSize(0, 60))
        self.box_ventas_top.setFrameShape(QFrame.StyledPanel)
        self.box_ventas_top.setFrameShadow(QFrame.Raised)
        self.ventas_fecha = QDateEdit(self.box_ventas_top)
        self.ventas_fecha.setObjectName(u"ventas_fecha")
        self.ventas_fecha.setEnabled(False)
        self.ventas_fecha.setGeometry(QRect(0, 26, 130, 22))
        self.label = QLabel(self.box_ventas_top)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1, 0, 150, 20))
        self.line = QFrame(self.box_ventas_top)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 130, 2))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_11 = QLabel(self.box_ventas_top)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(190, 0, 150, 20))
        self.ventas_rfc_cliente = QLineEdit(self.box_ventas_top)
        self.ventas_rfc_cliente.setObjectName(u"ventas_rfc_cliente")
        self.ventas_rfc_cliente.setGeometry(QRect(190, 26, 250, 22))
        self.line_2 = QFrame(self.box_ventas_top)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(190, 50, 250, 2))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.box_ventas_top)

        self.ventas_scroll_area = QScrollArea(self.page_ventas)
        self.ventas_scroll_area.setObjectName(u"ventas_scroll_area")
        self.ventas_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 70, 425))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ventas_scrolling = QFrame(self.scrollAreaWidgetContents)
        self.ventas_scrolling.setObjectName(u"ventas_scrolling")
        self.ventas_scrolling.setMinimumSize(QSize(0, 403))
        self.ventas_scrolling.setFrameShape(QFrame.StyledPanel)
        self.ventas_scrolling.setFrameShadow(QFrame.Raised)
        self.box_venta_header = QFrame(self.ventas_scrolling)
        self.box_venta_header.setObjectName(u"box_venta_header")
        self.box_venta_header.setGeometry(QRect(0, 0, 880, 25))
        self.box_venta_header.setStyleSheet(u"")
        self.box_venta_header.setFrameShape(QFrame.StyledPanel)
        self.box_venta_header.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.box_venta_header)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(440, 0, 61, 20))
        self.label_13 = QLabel(self.box_venta_header)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(520, 0, 91, 20))
        self.label_14 = QLabel(self.box_venta_header)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(620, 0, 100, 20))
        self.label_15 = QLabel(self.box_venta_header)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(740, 0, 75, 20))
        self.label_20 = QLabel(self.box_venta_header)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 0, 201, 24))
        self.label_21 = QLabel(self.box_venta_header)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(220, 0, 201, 24))
        self.box_venta_1 = QFrame(self.ventas_scrolling)
        self.box_venta_1.setObjectName(u"box_venta_1")
        self.box_venta_1.setGeometry(QRect(0, 40, 880, 35))
        self.box_venta_1.setStyleSheet(u"")
        self.box_venta_1.setFrameShape(QFrame.StyledPanel)
        self.box_venta_1.setFrameShadow(QFrame.Raised)
        self.venta_precio_1 = QDoubleSpinBox(self.box_venta_1)
        self.venta_precio_1.setObjectName(u"venta_precio_1")
        self.venta_precio_1.setEnabled(False)
        self.venta_precio_1.setGeometry(QRect(440, 5, 62, 22))
        self.venta_total_1 = QDoubleSpinBox(self.box_venta_1)
        self.venta_total_1.setObjectName(u"venta_total_1")
        self.venta_total_1.setEnabled(False)
        self.venta_total_1.setGeometry(QRect(740, 5, 75, 22))
        self.venta_unidades_1 = QSpinBox(self.box_venta_1)
        self.venta_unidades_1.setObjectName(u"venta_unidades_1")
        self.venta_unidades_1.setGeometry(QRect(520, 5, 42, 22))
        self.venta_remove_1 = QPushButton(self.box_venta_1)
        self.venta_remove_1.setObjectName(u"venta_remove_1")
        self.venta_remove_1.setGeometry(QRect(840, 0, 35, 35))
        self.venta_remove_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_11 = QFrame(self.box_venta_1)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(740, 30, 75, 2))
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.venta_categoria_producto_1 = QComboBox(self.box_venta_1)
        self.venta_categoria_producto_1.setObjectName(u"venta_categoria_producto_1")
        self.venta_categoria_producto_1.setGeometry(QRect(0, 0, 200, 35))
        self.venta_categoria_producto_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.venta_nombre_producto_1 = QComboBox(self.box_venta_1)
        self.venta_nombre_producto_1.setObjectName(u"venta_nombre_producto_1")
        self.venta_nombre_producto_1.setGeometry(QRect(220, 0, 200, 35))
        self.venta_nombre_producto_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_12 = QFrame(self.box_venta_1)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(520, 30, 90, 2))
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.line_13 = QFrame(self.box_venta_1)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(440, 30, 60, 2))
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.line_14 = QFrame(self.box_venta_1)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(620, 30, 100, 2))
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)
        self.venta_color_1 = QLineEdit(self.box_venta_1)
        self.venta_color_1.setObjectName(u"venta_color_1")
        self.venta_color_1.setGeometry(QRect(620, 5, 100, 22))
        self.box_venta_2 = QFrame(self.ventas_scrolling)
        self.box_venta_2.setObjectName(u"box_venta_2")
        self.box_venta_2.setGeometry(QRect(0, 100, 880, 35))
        self.box_venta_2.setStyleSheet(u"")
        self.box_venta_2.setFrameShape(QFrame.StyledPanel)
        self.box_venta_2.setFrameShadow(QFrame.Raised)
        self.venta_precio_5 = QDoubleSpinBox(self.box_venta_2)
        self.venta_precio_5.setObjectName(u"venta_precio_5")
        self.venta_precio_5.setGeometry(QRect(440, 5, 62, 22))
        self.venta_total_5 = QDoubleSpinBox(self.box_venta_2)
        self.venta_total_5.setObjectName(u"venta_total_5")
        self.venta_total_5.setGeometry(QRect(740, 5, 75, 22))
        self.venta_unidades_5 = QSpinBox(self.box_venta_2)
        self.venta_unidades_5.setObjectName(u"venta_unidades_5")
        self.venta_unidades_5.setGeometry(QRect(520, 5, 42, 22))
        self.venta_remove_4 = QPushButton(self.box_venta_2)
        self.venta_remove_4.setObjectName(u"venta_remove_4")
        self.venta_remove_4.setGeometry(QRect(840, 0, 35, 35))
        self.venta_remove_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_19 = QFrame(self.box_venta_2)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setGeometry(QRect(740, 30, 75, 2))
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)
        self.venta_categoria_producto_5 = QComboBox(self.box_venta_2)
        self.venta_categoria_producto_5.setObjectName(u"venta_categoria_producto_5")
        self.venta_categoria_producto_5.setGeometry(QRect(0, 0, 200, 35))
        self.venta_categoria_producto_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.venta_nombre_producto_5 = QComboBox(self.box_venta_2)
        self.venta_nombre_producto_5.setObjectName(u"venta_nombre_producto_5")
        self.venta_nombre_producto_5.setGeometry(QRect(220, 0, 200, 35))
        self.venta_nombre_producto_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_20 = QFrame(self.box_venta_2)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setGeometry(QRect(520, 30, 90, 2))
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)
        self.line_21 = QFrame(self.box_venta_2)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setGeometry(QRect(440, 30, 60, 2))
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)
        self.line_22 = QFrame(self.box_venta_2)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setGeometry(QRect(620, 30, 100, 2))
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)
        self.venta_color_5 = QLineEdit(self.box_venta_2)
        self.venta_color_5.setObjectName(u"venta_color_5")
        self.venta_color_5.setGeometry(QRect(620, 5, 100, 22))
        self.box_venta_3 = QFrame(self.ventas_scrolling)
        self.box_venta_3.setObjectName(u"box_venta_3")
        self.box_venta_3.setGeometry(QRect(0, 160, 880, 35))
        self.box_venta_3.setStyleSheet(u"")
        self.box_venta_3.setFrameShape(QFrame.StyledPanel)
        self.box_venta_3.setFrameShadow(QFrame.Raised)
        self.venta_precio_6 = QDoubleSpinBox(self.box_venta_3)
        self.venta_precio_6.setObjectName(u"venta_precio_6")
        self.venta_precio_6.setGeometry(QRect(440, 5, 62, 22))
        self.venta_total_6 = QDoubleSpinBox(self.box_venta_3)
        self.venta_total_6.setObjectName(u"venta_total_6")
        self.venta_total_6.setGeometry(QRect(740, 5, 75, 22))
        self.venta_unidades_6 = QSpinBox(self.box_venta_3)
        self.venta_unidades_6.setObjectName(u"venta_unidades_6")
        self.venta_unidades_6.setGeometry(QRect(520, 5, 42, 22))
        self.venta_remove_5 = QPushButton(self.box_venta_3)
        self.venta_remove_5.setObjectName(u"venta_remove_5")
        self.venta_remove_5.setGeometry(QRect(840, 0, 35, 35))
        self.venta_remove_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_23 = QFrame(self.box_venta_3)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setGeometry(QRect(740, 30, 75, 2))
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)
        self.venta_categoria_producto_6 = QComboBox(self.box_venta_3)
        self.venta_categoria_producto_6.setObjectName(u"venta_categoria_producto_6")
        self.venta_categoria_producto_6.setGeometry(QRect(0, 0, 200, 35))
        self.venta_categoria_producto_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.venta_nombre_producto_6 = QComboBox(self.box_venta_3)
        self.venta_nombre_producto_6.setObjectName(u"venta_nombre_producto_6")
        self.venta_nombre_producto_6.setGeometry(QRect(220, 0, 200, 35))
        self.venta_nombre_producto_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_24 = QFrame(self.box_venta_3)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setGeometry(QRect(520, 30, 90, 2))
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)
        self.line_25 = QFrame(self.box_venta_3)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setGeometry(QRect(440, 30, 60, 2))
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)
        self.line_26 = QFrame(self.box_venta_3)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setGeometry(QRect(620, 30, 100, 2))
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)
        self.venta_color_6 = QLineEdit(self.box_venta_3)
        self.venta_color_6.setObjectName(u"venta_color_6")
        self.venta_color_6.setGeometry(QRect(620, 5, 100, 22))
        self.box_venta_4 = QFrame(self.ventas_scrolling)
        self.box_venta_4.setObjectName(u"box_venta_4")
        self.box_venta_4.setGeometry(QRect(0, 220, 880, 35))
        self.box_venta_4.setStyleSheet(u"")
        self.box_venta_4.setFrameShape(QFrame.StyledPanel)
        self.box_venta_4.setFrameShadow(QFrame.Raised)
        self.venta_precio_8 = QDoubleSpinBox(self.box_venta_4)
        self.venta_precio_8.setObjectName(u"venta_precio_8")
        self.venta_precio_8.setGeometry(QRect(440, 5, 62, 22))
        self.venta_total_8 = QDoubleSpinBox(self.box_venta_4)
        self.venta_total_8.setObjectName(u"venta_total_8")
        self.venta_total_8.setGeometry(QRect(740, 5, 75, 22))
        self.venta_unidades_8 = QSpinBox(self.box_venta_4)
        self.venta_unidades_8.setObjectName(u"venta_unidades_8")
        self.venta_unidades_8.setGeometry(QRect(520, 5, 42, 22))
        self.venta_remove_7 = QPushButton(self.box_venta_4)
        self.venta_remove_7.setObjectName(u"venta_remove_7")
        self.venta_remove_7.setGeometry(QRect(840, 0, 35, 35))
        self.venta_remove_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_31 = QFrame(self.box_venta_4)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setGeometry(QRect(740, 30, 75, 2))
        self.line_31.setFrameShape(QFrame.HLine)
        self.line_31.setFrameShadow(QFrame.Sunken)
        self.venta_categoria_producto_8 = QComboBox(self.box_venta_4)
        self.venta_categoria_producto_8.setObjectName(u"venta_categoria_producto_8")
        self.venta_categoria_producto_8.setGeometry(QRect(0, 0, 200, 35))
        self.venta_categoria_producto_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.venta_nombre_producto_8 = QComboBox(self.box_venta_4)
        self.venta_nombre_producto_8.setObjectName(u"venta_nombre_producto_8")
        self.venta_nombre_producto_8.setGeometry(QRect(220, 0, 200, 35))
        self.venta_nombre_producto_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_32 = QFrame(self.box_venta_4)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setGeometry(QRect(520, 30, 90, 2))
        self.line_32.setFrameShape(QFrame.HLine)
        self.line_32.setFrameShadow(QFrame.Sunken)
        self.line_33 = QFrame(self.box_venta_4)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setGeometry(QRect(440, 30, 60, 2))
        self.line_33.setFrameShape(QFrame.HLine)
        self.line_33.setFrameShadow(QFrame.Sunken)
        self.line_34 = QFrame(self.box_venta_4)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setGeometry(QRect(620, 30, 100, 2))
        self.line_34.setFrameShape(QFrame.HLine)
        self.line_34.setFrameShadow(QFrame.Sunken)
        self.venta_color_8 = QLineEdit(self.box_venta_4)
        self.venta_color_8.setObjectName(u"venta_color_8")
        self.venta_color_8.setGeometry(QRect(620, 5, 100, 22))

        self.verticalLayout_5.addWidget(self.ventas_scrolling)

        self.ventas_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.ventas_scroll_area)

        self.box_ventas_buttons = QFrame(self.page_ventas)
        self.box_ventas_buttons.setObjectName(u"box_ventas_buttons")
        self.box_ventas_buttons.setMinimumSize(QSize(0, 45))
        self.box_ventas_buttons.setFrameShape(QFrame.StyledPanel)
        self.box_ventas_buttons.setFrameShadow(QFrame.Raised)
        self.ventas_generar = QPushButton(self.box_ventas_buttons)
        self.ventas_generar.setObjectName(u"ventas_generar")
        self.ventas_generar.setGeometry(QRect(10, 10, 150, 35))
        self.ventas_generar.setCursor(QCursor(Qt.PointingHandCursor))
        self.ventas_agregar = QPushButton(self.box_ventas_buttons)
        self.ventas_agregar.setObjectName(u"ventas_agregar")
        self.ventas_agregar.setGeometry(QRect(190, 10, 150, 35))
        self.ventas_agregar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.box_ventas_buttons)

        self.stackedWidget.addWidget(self.page_ventas)
        self.page_compras = QWidget()
        self.page_compras.setObjectName(u"page_compras")
        self.verticalLayout_8 = QVBoxLayout(self.page_compras)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.box_compras_top = QFrame(self.page_compras)
        self.box_compras_top.setObjectName(u"box_compras_top")
        self.box_compras_top.setMinimumSize(QSize(0, 60))
        self.box_compras_top.setFrameShape(QFrame.StyledPanel)
        self.box_compras_top.setFrameShadow(QFrame.Raised)
        self.compras_fecha = QDateEdit(self.box_compras_top)
        self.compras_fecha.setObjectName(u"compras_fecha")
        self.compras_fecha.setEnabled(False)
        self.compras_fecha.setGeometry(QRect(0, 26, 130, 22))
        self.label_3 = QLabel(self.box_compras_top)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1, 0, 150, 20))
        self.line_3 = QFrame(self.box_compras_top)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 50, 130, 2))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.compras_proveedor = QComboBox(self.box_compras_top)
        self.compras_proveedor.setObjectName(u"compras_proveedor")
        self.compras_proveedor.setGeometry(QRect(170, 13, 200, 35))
        self.compras_proveedor.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.box_compras_top)

        self.compras_scroll_area = QScrollArea(self.page_compras)
        self.compras_scroll_area.setObjectName(u"compras_scroll_area")
        self.compras_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 92, 425))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.compras_scrolling = QFrame(self.scrollAreaWidgetContents_2)
        self.compras_scrolling.setObjectName(u"compras_scrolling")
        self.compras_scrolling.setMinimumSize(QSize(0, 403))
        self.compras_scrolling.setFrameShape(QFrame.StyledPanel)
        self.compras_scrolling.setFrameShadow(QFrame.Raised)
        self.venta_header_2 = QFrame(self.compras_scrolling)
        self.venta_header_2.setObjectName(u"venta_header_2")
        self.venta_header_2.setGeometry(QRect(0, 0, 880, 25))
        self.venta_header_2.setStyleSheet(u"")
        self.venta_header_2.setFrameShape(QFrame.StyledPanel)
        self.venta_header_2.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.venta_header_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(440, 0, 61, 20))
        self.label_17 = QLabel(self.venta_header_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(520, 0, 91, 20))
        self.label_18 = QLabel(self.venta_header_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(620, 0, 100, 20))
        self.label_19 = QLabel(self.venta_header_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(740, 0, 75, 20))
        self.label_22 = QLabel(self.venta_header_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 0, 201, 24))
        self.label_23 = QLabel(self.venta_header_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(220, 0, 201, 24))
        self.box_compra_1 = QFrame(self.compras_scrolling)
        self.box_compra_1.setObjectName(u"box_compra_1")
        self.box_compra_1.setGeometry(QRect(0, 40, 880, 35))
        self.box_compra_1.setStyleSheet(u"")
        self.box_compra_1.setFrameShape(QFrame.StyledPanel)
        self.box_compra_1.setFrameShadow(QFrame.Raised)
        self.compra_precio_1 = QDoubleSpinBox(self.box_compra_1)
        self.compra_precio_1.setObjectName(u"compra_precio_1")
        self.compra_precio_1.setEnabled(False)
        self.compra_precio_1.setGeometry(QRect(440, 5, 62, 22))
        self.compra_total_1 = QDoubleSpinBox(self.box_compra_1)
        self.compra_total_1.setObjectName(u"compra_total_1")
        self.compra_total_1.setEnabled(False)
        self.compra_total_1.setGeometry(QRect(740, 5, 75, 22))
        self.compra_unidades_1 = QSpinBox(self.box_compra_1)
        self.compra_unidades_1.setObjectName(u"compra_unidades_1")
        self.compra_unidades_1.setGeometry(QRect(520, 5, 42, 22))
        self.compra_remove_1 = QPushButton(self.box_compra_1)
        self.compra_remove_1.setObjectName(u"compra_remove_1")
        self.compra_remove_1.setGeometry(QRect(840, 0, 35, 35))
        self.compra_remove_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_35 = QFrame(self.box_compra_1)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setGeometry(QRect(740, 30, 75, 2))
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)
        self.compra_categoria_producto_1 = QComboBox(self.box_compra_1)
        self.compra_categoria_producto_1.setObjectName(u"compra_categoria_producto_1")
        self.compra_categoria_producto_1.setGeometry(QRect(0, 0, 200, 35))
        self.compra_categoria_producto_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.compra_nombre_producto_1 = QComboBox(self.box_compra_1)
        self.compra_nombre_producto_1.setObjectName(u"compra_nombre_producto_1")
        self.compra_nombre_producto_1.setGeometry(QRect(220, 0, 200, 35))
        self.compra_nombre_producto_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_36 = QFrame(self.box_compra_1)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setGeometry(QRect(520, 30, 90, 2))
        self.line_36.setFrameShape(QFrame.HLine)
        self.line_36.setFrameShadow(QFrame.Sunken)
        self.line_37 = QFrame(self.box_compra_1)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setGeometry(QRect(440, 30, 60, 2))
        self.line_37.setFrameShape(QFrame.HLine)
        self.line_37.setFrameShadow(QFrame.Sunken)
        self.line_38 = QFrame(self.box_compra_1)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setGeometry(QRect(620, 30, 100, 2))
        self.line_38.setFrameShape(QFrame.HLine)
        self.line_38.setFrameShadow(QFrame.Sunken)
        self.compra_color_1 = QLineEdit(self.box_compra_1)
        self.compra_color_1.setObjectName(u"compra_color_1")
        self.compra_color_1.setGeometry(QRect(620, 5, 100, 22))
        self.box_compra_2 = QFrame(self.compras_scrolling)
        self.box_compra_2.setObjectName(u"box_compra_2")
        self.box_compra_2.setGeometry(QRect(0, 100, 880, 35))
        self.box_compra_2.setStyleSheet(u"")
        self.box_compra_2.setFrameShape(QFrame.StyledPanel)
        self.box_compra_2.setFrameShadow(QFrame.Raised)
        self.venta_precio_10 = QDoubleSpinBox(self.box_compra_2)
        self.venta_precio_10.setObjectName(u"venta_precio_10")
        self.venta_precio_10.setGeometry(QRect(440, 5, 62, 22))
        self.venta_total_10 = QDoubleSpinBox(self.box_compra_2)
        self.venta_total_10.setObjectName(u"venta_total_10")
        self.venta_total_10.setGeometry(QRect(740, 5, 75, 22))
        self.venta_unidades_10 = QSpinBox(self.box_compra_2)
        self.venta_unidades_10.setObjectName(u"venta_unidades_10")
        self.venta_unidades_10.setGeometry(QRect(520, 5, 42, 22))
        self.venta_remove_9 = QPushButton(self.box_compra_2)
        self.venta_remove_9.setObjectName(u"venta_remove_9")
        self.venta_remove_9.setGeometry(QRect(840, 0, 35, 35))
        self.venta_remove_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_39 = QFrame(self.box_compra_2)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setGeometry(QRect(740, 30, 75, 2))
        self.line_39.setFrameShape(QFrame.HLine)
        self.line_39.setFrameShadow(QFrame.Sunken)
        self.venta_categoria_producto_10 = QComboBox(self.box_compra_2)
        self.venta_categoria_producto_10.setObjectName(u"venta_categoria_producto_10")
        self.venta_categoria_producto_10.setGeometry(QRect(0, 0, 200, 35))
        self.venta_categoria_producto_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.venta_nombre_producto_10 = QComboBox(self.box_compra_2)
        self.venta_nombre_producto_10.setObjectName(u"venta_nombre_producto_10")
        self.venta_nombre_producto_10.setGeometry(QRect(220, 0, 200, 35))
        self.venta_nombre_producto_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_40 = QFrame(self.box_compra_2)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setGeometry(QRect(520, 30, 90, 2))
        self.line_40.setFrameShape(QFrame.HLine)
        self.line_40.setFrameShadow(QFrame.Sunken)
        self.line_41 = QFrame(self.box_compra_2)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setGeometry(QRect(440, 30, 60, 2))
        self.line_41.setFrameShape(QFrame.HLine)
        self.line_41.setFrameShadow(QFrame.Sunken)
        self.line_42 = QFrame(self.box_compra_2)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setGeometry(QRect(620, 30, 100, 2))
        self.line_42.setFrameShape(QFrame.HLine)
        self.line_42.setFrameShadow(QFrame.Sunken)
        self.venta_color_10 = QLineEdit(self.box_compra_2)
        self.venta_color_10.setObjectName(u"venta_color_10")
        self.venta_color_10.setGeometry(QRect(620, 5, 100, 22))
        self.box_compra_3 = QFrame(self.compras_scrolling)
        self.box_compra_3.setObjectName(u"box_compra_3")
        self.box_compra_3.setGeometry(QRect(0, 160, 880, 35))
        self.box_compra_3.setStyleSheet(u"")
        self.box_compra_3.setFrameShape(QFrame.StyledPanel)
        self.box_compra_3.setFrameShadow(QFrame.Raised)
        self.venta_precio_11 = QDoubleSpinBox(self.box_compra_3)
        self.venta_precio_11.setObjectName(u"venta_precio_11")
        self.venta_precio_11.setGeometry(QRect(440, 5, 62, 22))
        self.venta_total_11 = QDoubleSpinBox(self.box_compra_3)
        self.venta_total_11.setObjectName(u"venta_total_11")
        self.venta_total_11.setGeometry(QRect(740, 5, 75, 22))
        self.venta_unidades_11 = QSpinBox(self.box_compra_3)
        self.venta_unidades_11.setObjectName(u"venta_unidades_11")
        self.venta_unidades_11.setGeometry(QRect(520, 5, 42, 22))
        self.venta_remove_10 = QPushButton(self.box_compra_3)
        self.venta_remove_10.setObjectName(u"venta_remove_10")
        self.venta_remove_10.setGeometry(QRect(840, 0, 35, 35))
        self.venta_remove_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_43 = QFrame(self.box_compra_3)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setGeometry(QRect(740, 30, 75, 2))
        self.line_43.setFrameShape(QFrame.HLine)
        self.line_43.setFrameShadow(QFrame.Sunken)
        self.venta_categoria_producto_11 = QComboBox(self.box_compra_3)
        self.venta_categoria_producto_11.setObjectName(u"venta_categoria_producto_11")
        self.venta_categoria_producto_11.setGeometry(QRect(0, 0, 200, 35))
        self.venta_categoria_producto_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.venta_nombre_producto_11 = QComboBox(self.box_compra_3)
        self.venta_nombre_producto_11.setObjectName(u"venta_nombre_producto_11")
        self.venta_nombre_producto_11.setGeometry(QRect(220, 0, 200, 35))
        self.venta_nombre_producto_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_44 = QFrame(self.box_compra_3)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setGeometry(QRect(520, 30, 90, 2))
        self.line_44.setFrameShape(QFrame.HLine)
        self.line_44.setFrameShadow(QFrame.Sunken)
        self.line_45 = QFrame(self.box_compra_3)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setGeometry(QRect(440, 30, 60, 2))
        self.line_45.setFrameShape(QFrame.HLine)
        self.line_45.setFrameShadow(QFrame.Sunken)
        self.line_46 = QFrame(self.box_compra_3)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setGeometry(QRect(620, 30, 100, 2))
        self.line_46.setFrameShape(QFrame.HLine)
        self.line_46.setFrameShadow(QFrame.Sunken)
        self.venta_color_11 = QLineEdit(self.box_compra_3)
        self.venta_color_11.setObjectName(u"venta_color_11")
        self.venta_color_11.setGeometry(QRect(620, 5, 100, 22))
        self.box_compra_4 = QFrame(self.compras_scrolling)
        self.box_compra_4.setObjectName(u"box_compra_4")
        self.box_compra_4.setGeometry(QRect(0, 220, 880, 35))
        self.box_compra_4.setStyleSheet(u"")
        self.box_compra_4.setFrameShape(QFrame.StyledPanel)
        self.box_compra_4.setFrameShadow(QFrame.Raised)
        self.venta_precio_12 = QDoubleSpinBox(self.box_compra_4)
        self.venta_precio_12.setObjectName(u"venta_precio_12")
        self.venta_precio_12.setGeometry(QRect(440, 5, 62, 22))
        self.venta_total_12 = QDoubleSpinBox(self.box_compra_4)
        self.venta_total_12.setObjectName(u"venta_total_12")
        self.venta_total_12.setGeometry(QRect(740, 5, 75, 22))
        self.venta_unidades_12 = QSpinBox(self.box_compra_4)
        self.venta_unidades_12.setObjectName(u"venta_unidades_12")
        self.venta_unidades_12.setGeometry(QRect(520, 5, 42, 22))
        self.venta_remove_11 = QPushButton(self.box_compra_4)
        self.venta_remove_11.setObjectName(u"venta_remove_11")
        self.venta_remove_11.setGeometry(QRect(840, 0, 35, 35))
        self.venta_remove_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_47 = QFrame(self.box_compra_4)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setGeometry(QRect(740, 30, 75, 2))
        self.line_47.setFrameShape(QFrame.HLine)
        self.line_47.setFrameShadow(QFrame.Sunken)
        self.venta_categoria_producto_12 = QComboBox(self.box_compra_4)
        self.venta_categoria_producto_12.setObjectName(u"venta_categoria_producto_12")
        self.venta_categoria_producto_12.setGeometry(QRect(0, 0, 200, 35))
        self.venta_categoria_producto_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.venta_nombre_producto_12 = QComboBox(self.box_compra_4)
        self.venta_nombre_producto_12.setObjectName(u"venta_nombre_producto_12")
        self.venta_nombre_producto_12.setGeometry(QRect(220, 0, 200, 35))
        self.venta_nombre_producto_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_48 = QFrame(self.box_compra_4)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setGeometry(QRect(520, 30, 90, 2))
        self.line_48.setFrameShape(QFrame.HLine)
        self.line_48.setFrameShadow(QFrame.Sunken)
        self.line_49 = QFrame(self.box_compra_4)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setGeometry(QRect(440, 30, 60, 2))
        self.line_49.setFrameShape(QFrame.HLine)
        self.line_49.setFrameShadow(QFrame.Sunken)
        self.line_50 = QFrame(self.box_compra_4)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setGeometry(QRect(620, 30, 100, 2))
        self.line_50.setFrameShape(QFrame.HLine)
        self.line_50.setFrameShadow(QFrame.Sunken)
        self.venta_color_12 = QLineEdit(self.box_compra_4)
        self.venta_color_12.setObjectName(u"venta_color_12")
        self.venta_color_12.setGeometry(QRect(620, 5, 100, 22))

        self.verticalLayout_7.addWidget(self.compras_scrolling)

        self.compras_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.compras_scroll_area)

        self.box_compras_buttons = QFrame(self.page_compras)
        self.box_compras_buttons.setObjectName(u"box_compras_buttons")
        self.box_compras_buttons.setMinimumSize(QSize(0, 45))
        self.box_compras_buttons.setFrameShape(QFrame.StyledPanel)
        self.box_compras_buttons.setFrameShadow(QFrame.Raised)
        self.compras_generar = QPushButton(self.box_compras_buttons)
        self.compras_generar.setObjectName(u"compras_generar")
        self.compras_generar.setGeometry(QRect(10, 10, 150, 35))
        self.compras_generar.setCursor(QCursor(Qt.PointingHandCursor))
        self.compras_agregar = QPushButton(self.box_compras_buttons)
        self.compras_agregar.setObjectName(u"compras_agregar")
        self.compras_agregar.setGeometry(QRect(190, 10, 150, 35))
        self.compras_agregar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.box_compras_buttons)

        self.stackedWidget.addWidget(self.page_compras)
        self.page_productos = QWidget()
        self.page_productos.setObjectName(u"page_productos")
        self.verticalLayout_9 = QVBoxLayout(self.page_productos)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(150, 40, 150, 40)
        self.box_productos_top_buttons = QFrame(self.page_productos)
        self.box_productos_top_buttons.setObjectName(u"box_productos_top_buttons")
        self.box_productos_top_buttons.setMinimumSize(QSize(0, 30))
        self.box_productos_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.box_productos_top_buttons.setFrameShadow(QFrame.Raised)
        self.productos_ver = QPushButton(self.box_productos_top_buttons)
        self.productos_ver.setObjectName(u"productos_ver")
        self.productos_ver.setGeometry(QRect(0, 0, 150, 30))
        self.productos_ver.setCursor(QCursor(Qt.PointingHandCursor))
        self.productos_agregar = QPushButton(self.box_productos_top_buttons)
        self.productos_agregar.setObjectName(u"productos_agregar")
        self.productos_agregar.setGeometry(QRect(150, 0, 150, 30))
        self.productos_agregar.setCursor(QCursor(Qt.PointingHandCursor))
        self.productos_editar = QPushButton(self.box_productos_top_buttons)
        self.productos_editar.setObjectName(u"productos_editar")
        self.productos_editar.setGeometry(QRect(300, 0, 150, 30))
        self.productos_editar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.box_productos_top_buttons)

        self.productos_stacked = QStackedWidget(self.page_productos)
        self.productos_stacked.setObjectName(u"productos_stacked")
        self.page_productos_ver = QWidget()
        self.page_productos_ver.setObjectName(u"page_productos_ver")
        self.producto_ver_categoria = QComboBox(self.page_productos_ver)
        self.producto_ver_categoria.setObjectName(u"producto_ver_categoria")
        self.producto_ver_categoria.setGeometry(QRect(75, 40, 200, 35))
        self.producto_ver_categoria.setCursor(QCursor(Qt.PointingHandCursor))
        self.producto_ver_nombre = QComboBox(self.page_productos_ver)
        self.producto_ver_nombre.setObjectName(u"producto_ver_nombre")
        self.producto_ver_nombre.setGeometry(QRect(430, 40, 200, 35))
        self.productos_ver_proveedor = QLineEdit(self.page_productos_ver)
        self.productos_ver_proveedor.setObjectName(u"productos_ver_proveedor")
        self.productos_ver_proveedor.setGeometry(QRect(75, 116, 250, 22))
        self.label_24 = QLabel(self.page_productos_ver)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(75, 90, 150, 20))
        self.line_4 = QFrame(self.page_productos_ver)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(75, 140, 250, 2))
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(1)
        self.line_4.setFrameShape(QFrame.HLine)
        self.label_25 = QLabel(self.page_productos_ver)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(75, 160, 150, 20))
        self.line_5 = QFrame(self.page_productos_ver)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(75, 210, 250, 2))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_26 = QLabel(self.page_productos_ver)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(75, 230, 150, 20))
        self.line_6 = QFrame(self.page_productos_ver)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(75, 280, 250, 2))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.productos_ver_existencia = QSpinBox(self.page_productos_ver)
        self.productos_ver_existencia.setObjectName(u"productos_ver_existencia")
        self.productos_ver_existencia.setGeometry(QRect(75, 256, 241, 22))
        self.productos_ver_precio = QDoubleSpinBox(self.page_productos_ver)
        self.productos_ver_precio.setObjectName(u"productos_ver_precio")
        self.productos_ver_precio.setGeometry(QRect(75, 186, 241, 22))
        self.label_27 = QLabel(self.page_productos_ver)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(75, 300, 101, 20))
        self.productos_ver_resurtible = QCheckBox(self.page_productos_ver)
        self.productos_ver_resurtible.setObjectName(u"productos_ver_resurtible")
        self.productos_ver_resurtible.setGeometry(QRect(300, 300, 23, 23))
        self.label_28 = QLabel(self.page_productos_ver)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(370, 110, 150, 20))
        self.productos_ver_descripcion = QTextEdit(self.page_productos_ver)
        self.productos_ver_descripcion.setObjectName(u"productos_ver_descripcion")
        self.productos_ver_descripcion.setGeometry(QRect(373, 140, 250, 181))
        self.productos_stacked.addWidget(self.page_productos_ver)
        self.producto_ver_categoria.raise_()
        self.producto_ver_nombre.raise_()
        self.productos_ver_proveedor.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.line_5.raise_()
        self.label_26.raise_()
        self.line_6.raise_()
        self.productos_ver_existencia.raise_()
        self.productos_ver_precio.raise_()
        self.label_27.raise_()
        self.productos_ver_resurtible.raise_()
        self.label_28.raise_()
        self.productos_ver_descripcion.raise_()
        self.line_4.raise_()
        self.page_productos_agregar = QWidget()
        self.page_productos_agregar.setObjectName(u"page_productos_agregar")
        self.line_7 = QFrame(self.page_productos_agregar)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(75, 300, 250, 2))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.label_29 = QLabel(self.page_productos_agregar)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(75, 250, 150, 20))
        self.label_30 = QLabel(self.page_productos_agregar)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(370, 164, 150, 20))
        self.line_8 = QFrame(self.page_productos_agregar)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(75, 220, 250, 2))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.productos_agregar_nueva_categoria = QLineEdit(self.page_productos_agregar)
        self.productos_agregar_nueva_categoria.setObjectName(u"productos_agregar_nueva_categoria")
        self.productos_agregar_nueva_categoria.setGeometry(QRect(75, 120, 221, 22))
        self.label_31 = QLabel(self.page_productos_agregar)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(75, 170, 150, 20))
        self.label_32 = QLabel(self.page_productos_agregar)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(75, 94, 150, 20))
        self.productos_agregar_existencia = QSpinBox(self.page_productos_agregar)
        self.productos_agregar_existencia.setObjectName(u"productos_agregar_existencia")
        self.productos_agregar_existencia.setGeometry(QRect(75, 276, 241, 22))
        self.productos_agregar_descripcion = QTextEdit(self.page_productos_agregar)
        self.productos_agregar_descripcion.setObjectName(u"productos_agregar_descripcion")
        self.productos_agregar_descripcion.setGeometry(QRect(373, 194, 250, 181))
        self.productos_agregar_precio = QDoubleSpinBox(self.page_productos_agregar)
        self.productos_agregar_precio.setObjectName(u"productos_agregar_precio")
        self.productos_agregar_precio.setGeometry(QRect(75, 196, 241, 22))
        self.productos_agregar_proveedor = QComboBox(self.page_productos_agregar)
        self.productos_agregar_proveedor.setObjectName(u"productos_agregar_proveedor")
        self.productos_agregar_proveedor.setGeometry(QRect(430, 40, 200, 35))
        self.label_33 = QLabel(self.page_productos_agregar)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(75, 340, 101, 20))
        self.productos_agregar_resurtible = QCheckBox(self.page_productos_agregar)
        self.productos_agregar_resurtible.setObjectName(u"productos_agregar_resurtible")
        self.productos_agregar_resurtible.setGeometry(QRect(300, 340, 23, 23))
        self.productos_agregar_categoria = QComboBox(self.page_productos_agregar)
        self.productos_agregar_categoria.setObjectName(u"productos_agregar_categoria")
        self.productos_agregar_categoria.setGeometry(QRect(75, 40, 200, 35))
        self.productos_agregar_categoria.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_9 = QFrame(self.page_productos_agregar)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(75, 144, 220, 2))
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.productos_agregar_check_nueva_categoria = QCheckBox(self.page_productos_agregar)
        self.productos_agregar_check_nueva_categoria.setObjectName(u"productos_agregar_check_nueva_categoria")
        self.productos_agregar_check_nueva_categoria.setGeometry(QRect(310, 120, 23, 23))
        self.label_34 = QLabel(self.page_productos_agregar)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(370, 94, 150, 20))
        self.line_10 = QFrame(self.page_productos_agregar)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(370, 144, 250, 2))
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.productos_agregar_nombre = QLineEdit(self.page_productos_agregar)
        self.productos_agregar_nombre.setObjectName(u"productos_agregar_nombre")
        self.productos_agregar_nombre.setGeometry(QRect(370, 120, 251, 22))
        self.productos_stacked.addWidget(self.page_productos_agregar)
        self.page_productos_editar = QWidget()
        self.page_productos_editar.setObjectName(u"page_productos_editar")
        self.label_35 = QLabel(self.page_productos_editar)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(75, 170, 150, 20))
        self.label_36 = QLabel(self.page_productos_editar)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(370, 164, 150, 20))
        self.productos_editar_check_nuevo_nombre = QCheckBox(self.page_productos_editar)
        self.productos_editar_check_nuevo_nombre.setObjectName(u"productos_editar_check_nuevo_nombre")
        self.productos_editar_check_nuevo_nombre.setGeometry(QRect(600, 120, 23, 23))
        self.productos_editar_categoria = QComboBox(self.page_productos_editar)
        self.productos_editar_categoria.setObjectName(u"productos_editar_categoria")
        self.productos_editar_categoria.setGeometry(QRect(75, 40, 200, 35))
        self.productos_editar_categoria.setCursor(QCursor(Qt.PointingHandCursor))
        self.productos_editar_nombre = QComboBox(self.page_productos_editar)
        self.productos_editar_nombre.setObjectName(u"productos_editar_nombre")
        self.productos_editar_nombre.setGeometry(QRect(430, 40, 200, 35))
        self.line_52 = QFrame(self.page_productos_editar)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setGeometry(QRect(75, 300, 250, 2))
        self.line_52.setFrameShape(QFrame.HLine)
        self.line_52.setFrameShadow(QFrame.Sunken)
        self.productos_editar_nuevo_nombre = QLineEdit(self.page_productos_editar)
        self.productos_editar_nuevo_nombre.setObjectName(u"productos_editar_nuevo_nombre")
        self.productos_editar_nuevo_nombre.setGeometry(QRect(370, 120, 221, 22))
        self.line_53 = QFrame(self.page_productos_editar)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setGeometry(QRect(75, 220, 250, 2))
        self.line_53.setFrameShape(QFrame.HLine)
        self.line_53.setFrameShadow(QFrame.Sunken)
        self.label_38 = QLabel(self.page_productos_editar)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(75, 250, 150, 20))
        self.label_39 = QLabel(self.page_productos_editar)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(370, 94, 251, 20))
        self.productos_editar_resurtible = QCheckBox(self.page_productos_editar)
        self.productos_editar_resurtible.setObjectName(u"productos_editar_resurtible")
        self.productos_editar_resurtible.setGeometry(QRect(300, 340, 23, 23))
        self.productos_editar_precio = QDoubleSpinBox(self.page_productos_editar)
        self.productos_editar_precio.setObjectName(u"productos_editar_precio")
        self.productos_editar_precio.setGeometry(QRect(75, 196, 241, 22))
        self.productos_editar_existencia = QSpinBox(self.page_productos_editar)
        self.productos_editar_existencia.setObjectName(u"productos_editar_existencia")
        self.productos_editar_existencia.setGeometry(QRect(75, 276, 241, 22))
        self.line_54 = QFrame(self.page_productos_editar)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setGeometry(QRect(370, 144, 220, 2))
        self.line_54.setFrameShape(QFrame.HLine)
        self.line_54.setFrameShadow(QFrame.Sunken)
        self.productos_editar_descripcion = QTextEdit(self.page_productos_editar)
        self.productos_editar_descripcion.setObjectName(u"productos_editar_descripcion")
        self.productos_editar_descripcion.setGeometry(QRect(373, 194, 250, 181))
        self.label_40 = QLabel(self.page_productos_editar)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(75, 340, 101, 20))
        self.productos_editar_proveedor = QComboBox(self.page_productos_editar)
        self.productos_editar_proveedor.setObjectName(u"productos_editar_proveedor")
        self.productos_editar_proveedor.setGeometry(QRect(75, 100, 200, 35))
        self.productos_stacked.addWidget(self.page_productos_editar)

        self.verticalLayout_9.addWidget(self.productos_stacked)

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
        self.box_version.setMaximumSize(QSize(100, 16777215))
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

        self.stackedWidget.setCurrentIndex(2)


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
        self.lbl_toggle.setText(QCoreApplication.translate("MainWindows", u"Ocultar", None))
        self.btn_ventas.setText("")
        self.lbl_ventas.setText(QCoreApplication.translate("MainWindows", u"Ventas", None))
        self.btn_compras.setText("")
        self.lbl_compras.setText(QCoreApplication.translate("MainWindows", u"Compras", None))
        self.btn_productos.setText("")
        self.lbl_productos.setText(QCoreApplication.translate("MainWindows", u"Productos", None))
        self.btn_proveedores.setText("")
        self.lbl_proveedores.setText(QCoreApplication.translate("MainWindows", u"Proveedores", None))
        self.btn_tickets.setText("")
        self.lbl_tickets.setText(QCoreApplication.translate("MainWindows", u"Tickets", None))
        self.btn_recorte_caja.setText("")
        self.lbl_recorte_caja.setText(QCoreApplication.translate("MainWindows", u"Recorte de caja", None))
        self.btn_copia_seguridad.setText("")
        self.lbl_copia_seguridad.setText(QCoreApplication.translate("MainWindows", u"Copia de seguridad", None))
        self.label.setText(QCoreApplication.translate("MainWindows", u"Fecha", None))
        self.label_11.setText(QCoreApplication.translate("MainWindows", u"RFC", None))
        self.ventas_rfc_cliente.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindows", u"Precio", None))
        self.label_13.setText(QCoreApplication.translate("MainWindows", u"Unidades", None))
        self.label_14.setText(QCoreApplication.translate("MainWindows", u"Color", None))
        self.label_15.setText(QCoreApplication.translate("MainWindows", u"Total", None))
        self.label_20.setText(QCoreApplication.translate("MainWindows", u"Categoria", None))
        self.label_21.setText(QCoreApplication.translate("MainWindows", u"Nombre", None))
        self.venta_remove_1.setText("")
        self.venta_color_1.setText("")
        self.venta_remove_4.setText("")
        self.venta_color_5.setText("")
        self.venta_remove_5.setText("")
        self.venta_color_6.setText("")
        self.venta_remove_7.setText("")
        self.venta_color_8.setText("")
        self.ventas_generar.setText(QCoreApplication.translate("MainWindows", u"Generar Venta", None))
        self.ventas_agregar.setText(QCoreApplication.translate("MainWindows", u"Agregar Prducto", None))
        self.label_3.setText(QCoreApplication.translate("MainWindows", u"Fecha", None))
        self.label_16.setText(QCoreApplication.translate("MainWindows", u"Precio", None))
        self.label_17.setText(QCoreApplication.translate("MainWindows", u"Unidades", None))
        self.label_18.setText(QCoreApplication.translate("MainWindows", u"Color", None))
        self.label_19.setText(QCoreApplication.translate("MainWindows", u"Total", None))
        self.label_22.setText(QCoreApplication.translate("MainWindows", u"Categoria", None))
        self.label_23.setText(QCoreApplication.translate("MainWindows", u"Nombre", None))
        self.compra_remove_1.setText("")
        self.compra_color_1.setText("")
        self.venta_remove_9.setText("")
        self.venta_color_10.setText("")
        self.venta_remove_10.setText("")
        self.venta_color_11.setText("")
        self.venta_remove_11.setText("")
        self.venta_color_12.setText("")
        self.compras_generar.setText(QCoreApplication.translate("MainWindows", u"Generar Venta", None))
        self.compras_agregar.setText(QCoreApplication.translate("MainWindows", u"Agregar Prducto", None))
        self.productos_ver.setText(QCoreApplication.translate("MainWindows", u"Ver", None))
        self.productos_agregar.setText(QCoreApplication.translate("MainWindows", u"Agregar", None))
        self.productos_editar.setText(QCoreApplication.translate("MainWindows", u"Editar", None))
        self.productos_ver_proveedor.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindows", u"Proveedor", None))
        self.label_25.setText(QCoreApplication.translate("MainWindows", u"Precio", None))
        self.label_26.setText(QCoreApplication.translate("MainWindows", u"Existencia", None))
        self.label_27.setText(QCoreApplication.translate("MainWindows", u"Resurtible", None))
        self.productos_ver_resurtible.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindows", u"Proveedor", None))
        self.label_29.setText(QCoreApplication.translate("MainWindows", u"Existencia", None))
        self.label_30.setText(QCoreApplication.translate("MainWindows", u"Proveedor", None))
        self.productos_agregar_nueva_categoria.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindows", u"Precio", None))
        self.label_32.setText(QCoreApplication.translate("MainWindows", u"Crear nueva categoria", None))
        self.label_33.setText(QCoreApplication.translate("MainWindows", u"Resurtible", None))
        self.productos_agregar_resurtible.setText("")
        self.productos_agregar_check_nueva_categoria.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindows", u"Nombre", None))
        self.productos_agregar_nombre.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindows", u"Precio", None))
        self.label_36.setText(QCoreApplication.translate("MainWindows", u"Proveedor", None))
        self.productos_editar_check_nuevo_nombre.setText("")
        self.productos_editar_nuevo_nombre.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindows", u"Existencia", None))
        self.label_39.setText(QCoreApplication.translate("MainWindows", u"Cambiar nombre", None))
        self.productos_editar_resurtible.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindows", u"Resurtible", None))
        self.label_5.setText(QCoreApplication.translate("MainWindows", u"proveedores", None))
        self.label_6.setText(QCoreApplication.translate("MainWindows", u"tickets", None))
        self.label_7.setText(QCoreApplication.translate("MainWindows", u"recorte de caja", None))
        self.label_8.setText(QCoreApplication.translate("MainWindows", u"copia de seguridad", None))
        self.label_9.setText(QCoreApplication.translate("MainWindows", u"admin", None))
        self.label_10.setText(QCoreApplication.translate("MainWindows", u"empleado", None))
        self.label_2.setText(QCoreApplication.translate("MainWindows", u"Team Lost Souls", None))
        self.version.setText(QCoreApplication.translate("MainWindows", u"V. 1.5.3", None))
    # retranslateUi

