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
"\n"
"/********************************/\n"
"#btn_toggle { image: url(:/icons/assets/icons/toggle menu.png); }\n"
"#"
                        "btn_compras { image: url(:/icons/assets/icons/compras.png); }\n"
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
""
                        "/********************************/\n"
"\n"
"\n"
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
"#page_container QLabel, #page_container QLineEdit {\n"
"font: 12pt;\n"
"background: transparent;\n"
"color: white;\n"
"}\n"
"\n"
"#ventas_agregar, #compras_agregar, #Tickets_generar_ticket, #recorte_caja_generar_ticket, #empleados_guardar_cambios,\n"
"#administrador_guardar_cambios, #administrador_nuevo_empleado_guardar_cambios {\n"
"background: #2A91FF;\n"
"border-radius: 5px;\n"
"}\n"
"#ventas_generar, #compras_generar, #productos_agregar_guardar, #productos_editar_guardar,\n"
"#proveedores_agregar_guardar, #proveedores_editar_guardar {\n"
"background: #2EAC4B;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"font: 12pt;\n"
"}\n"
"\n"
"QDateEdit {\n"
"background: transparent;\n"
"border-bottom 1px solid red;\n"
"font: 12pt;\n"
"color: #fff;\n"
"}\n"
""
                        "\n"
"QDateEdit::down-button, QDateEdit::up-button { image: none; }\n"
"\n"
"QComboBox, QListView {\n"
"background: #212634;\n"
"border-radius: 5px;\n"
"color: #fff;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down { \n"
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
"#productos_stacked > QWidget,\n"
"#proveedores_stacked > QWidget,\n"
"#administrador_stacked > QWidget {\n"
"border: 2px solid #38C3DD;\n"
"border-radius: 5px;\n"
"border-top-left-radius: 0px;\n"
"background: transparent;\n"
"}\n"
"\n"
"#box_productos_top_buttons  > QPushButton,\n"
"#box_proveedores_top_buttons > QPushButt"
                        "on,\n"
"#box_administrador_top_buttons > QPushButton {\n"
"background: transparent;\n"
"border: 2px solid #38C3DD;\n"
"border-radius: 5px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"#tickets_borrar_filtros {\n"
"background: #FF5C67;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #707070;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #38C3DD;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 0px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal "
                        "{\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 0px;\n"
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
"	background: #38C3DD;\n"
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
""
                        " }\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: none; }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal { background: none; }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { background: none; }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
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
"/* //////////////////////////////////////////////////////////"
                        "/////////////////////////////////////// */\n"
"\n"
"\n"
"QTextEdit {\n"
"background: #212634;\n"
"color: #fff;\n"
"}\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	gridline-color: #374553;\n"
"}\n"
"QTableWidget::item {\n"
"	border-color: transparent;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	color: #fff;\n"
"}\n"
"QTableWidget::item:selected {\n"
"	background-color: #202531;\n"
"}\n"
"QHeaderView::section {\n"
"	height: 20px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    border: none;\n"
"    border-right: 1px solid #374553;\n"
"	background-color: #293546;\n"
"	/*background-color: #202531;*/\n"
"	padding: 3px;\n"
"color: #fff;\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#donwload, #upload {\n"
"bord"
                        "er-radius: 75px;\n"
"}\n"
"\n"
"#donwload {\n"
"image: url(:/icons/assets/icons/download.png);\n"
"background: #2A91FF;\n"
"}\n"
"\n"
"\n"
"#upload {\n"
"image: url(:/icons/assets/icons/upload.png);\n"
"background: #2EAC4B;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QDialog QPushButton, QDialog QPushButton:hover, QDialog QPushButton:focus {\n"
"    background: #2A91FF;\n"
"    border-radius: 5px;\n"
"	color: #fff;\n"
"	font-size: 18px;\n"
"	width: 80px;\n"
"}\n"
"QDialog {\n"
"	background-color: #212634;\n"
"}\n"
"\n"
"QDialog QLabel {\n"
"	font: 17px;\n"
"	color: #eaeaea;\n"
"}\n"
"\n"
"")
        self.main = QWidget(MainWindows)
        self.main.setObjectName(u"main")
        self.main.setLayoutDirection(Qt.LeftToRight)
        self.main.setStyleSheet(u"#line, #line_1, #line_2, #line_3, #line_4, #line_5, #line_6, #line_7, #line_8, #line_9, #line_10,\n"
"#line_11, #line_12, #line_13, #line_14, #line_15, #line_16, #line_17, #line_18, #line_19, #line_20,\n"
"#line_21, #line_22, #line_23, #line_24, #line_25, #line_26, #line_27, #line_28, #line_29, #line_30,\n"
"#line_31, #line_32, #line_33, #line_34, #line_35, #line_36, #line_37, #line_38, #line_39, #line_40,\n"
"#line_41, #line_42, #line_43, #line_44, #line_45, #line_46, #line_47, #line_48, #line_49, #line_50,\n"
"#line_51, #line_52, #line_53, #line_54, #line_55, #line_56, #line_57, #line_58, #line_59, #line_60,\n"
"#line_61, #line_62, #line_63, #line_64, #line_65, #line_66, #line_67, #line_68, #line_69, #line_70,\n"
"#line_71, #line_72, #line_73, #line_74, #line_75, #line_76, #line_77, #line_78, #line_79, #line_80,\n"
"#line_81, #line_82, #line_83, #line_84, #line_85, #line_86, #line_87, #line_88, #line_89, #line_90,\n"
"#line_91, #line_92, #line_93, #line_94, #line_95, #line_96, #line_97, #line_98, #line_99, #"
                        "line_100 {\n"
"background: #fff;\n"
"}\n"
"\n"
"#line_vertical,  #line_vertical_2, #line_vertical_3, #line_vertical_4 {\n"
"background: #374553;\n"
"}\n"
"\n"
"/*background: #374553;*/")
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1011, 376))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ventas_scrolling = QFrame(self.scrollAreaWidgetContents)
        self.ventas_scrolling.setObjectName(u"ventas_scrolling")
        self.ventas_scrolling.setMinimumSize(QSize(0, 250))
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
        self.venta_precio_1.setMaximum(1000000.000000000000000)
        self.venta_total_1 = QDoubleSpinBox(self.box_venta_1)
        self.venta_total_1.setObjectName(u"venta_total_1")
        self.venta_total_1.setEnabled(False)
        self.venta_total_1.setGeometry(QRect(740, 5, 75, 22))
        self.venta_total_1.setMaximum(10000000.000000000000000)
        self.venta_unidades_1 = QSpinBox(self.box_venta_1)
        self.venta_unidades_1.setObjectName(u"venta_unidades_1")
        self.venta_unidades_1.setGeometry(QRect(520, 5, 42, 22))
        self.venta_unidades_1.setMaximum(100000)
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
        self.ventas_table_widget = QTableWidget(self.ventas_scrolling)
        if (self.ventas_table_widget.columnCount() < 6):
            self.ventas_table_widget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.ventas_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ventas_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ventas_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ventas_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ventas_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ventas_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.ventas_table_widget.setObjectName(u"ventas_table_widget")
        self.ventas_table_widget.setGeometry(QRect(0, 90, 881, 251))

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1011, 376))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.compras_scrolling = QFrame(self.scrollAreaWidgetContents_2)
        self.compras_scrolling.setObjectName(u"compras_scrolling")
        self.compras_scrolling.setMinimumSize(QSize(0, 250))
        self.compras_scrolling.setFrameShape(QFrame.StyledPanel)
        self.compras_scrolling.setFrameShadow(QFrame.Raised)
        self.compra_header = QFrame(self.compras_scrolling)
        self.compra_header.setObjectName(u"compra_header")
        self.compra_header.setGeometry(QRect(0, 0, 880, 25))
        self.compra_header.setStyleSheet(u"")
        self.compra_header.setFrameShape(QFrame.StyledPanel)
        self.compra_header.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.compra_header)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(440, 0, 61, 20))
        self.label_17 = QLabel(self.compra_header)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(520, 0, 91, 20))
        self.label_19 = QLabel(self.compra_header)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(620, 0, 75, 20))
        self.label_22 = QLabel(self.compra_header)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 0, 201, 24))
        self.label_23 = QLabel(self.compra_header)
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
        self.compra_precio_1.setMaximum(100000.000000000000000)
        self.compra_total_1 = QDoubleSpinBox(self.box_compra_1)
        self.compra_total_1.setObjectName(u"compra_total_1")
        self.compra_total_1.setEnabled(False)
        self.compra_total_1.setGeometry(QRect(620, 5, 75, 22))
        self.compra_total_1.setMaximum(1000000000.000000000000000)
        self.compra_unidades_1 = QSpinBox(self.box_compra_1)
        self.compra_unidades_1.setObjectName(u"compra_unidades_1")
        self.compra_unidades_1.setGeometry(QRect(520, 5, 42, 22))
        self.compra_unidades_1.setMaximum(100000)
        self.line_35 = QFrame(self.box_compra_1)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setGeometry(QRect(620, 30, 75, 2))
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
        self.compras_table_widget = QTableWidget(self.compras_scrolling)
        if (self.compras_table_widget.columnCount() < 5):
            self.compras_table_widget.setColumnCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.compras_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.compras_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.compras_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.compras_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.compras_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        self.compras_table_widget.setObjectName(u"compras_table_widget")
        self.compras_table_widget.setGeometry(QRect(0, 90, 881, 251))

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
        self.verticalLayout_9.setContentsMargins(150, 30, 150, 30)
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
        self.producto_ver_nombre.setGeometry(QRect(400, 40, 230, 35))
        self.label_25 = QLabel(self.page_productos_ver)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(75, 90, 150, 20))
        self.line_5 = QFrame(self.page_productos_ver)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(75, 140, 250, 2))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_26 = QLabel(self.page_productos_ver)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(75, 180, 150, 20))
        self.line_6 = QFrame(self.page_productos_ver)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(75, 230, 250, 2))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.productos_ver_existencia = QSpinBox(self.page_productos_ver)
        self.productos_ver_existencia.setObjectName(u"productos_ver_existencia")
        self.productos_ver_existencia.setEnabled(False)
        self.productos_ver_existencia.setGeometry(QRect(75, 206, 241, 22))
        self.productos_ver_precio = QDoubleSpinBox(self.page_productos_ver)
        self.productos_ver_precio.setObjectName(u"productos_ver_precio")
        self.productos_ver_precio.setEnabled(False)
        self.productos_ver_precio.setGeometry(QRect(75, 116, 241, 22))
        self.label_27 = QLabel(self.page_productos_ver)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(75, 270, 101, 20))
        self.productos_ver_resurtible = QCheckBox(self.page_productos_ver)
        self.productos_ver_resurtible.setObjectName(u"productos_ver_resurtible")
        self.productos_ver_resurtible.setEnabled(False)
        self.productos_ver_resurtible.setGeometry(QRect(300, 270, 23, 23))
        self.label_28 = QLabel(self.page_productos_ver)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(370, 110, 150, 20))
        self.productos_ver_descripcion = QTextEdit(self.page_productos_ver)
        self.productos_ver_descripcion.setObjectName(u"productos_ver_descripcion")
        self.productos_ver_descripcion.setEnabled(False)
        self.productos_ver_descripcion.setGeometry(QRect(373, 140, 250, 181))
        self.productos_stacked.addWidget(self.page_productos_ver)
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
        self.label_30.setGeometry(QRect(370, 170, 150, 20))
        self.line_8 = QFrame(self.page_productos_agregar)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(75, 220, 250, 2))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.productos_agregar_nueva_categoria = QLineEdit(self.page_productos_agregar)
        self.productos_agregar_nueva_categoria.setObjectName(u"productos_agregar_nueva_categoria")
        self.productos_agregar_nueva_categoria.setEnabled(False)
        self.productos_agregar_nueva_categoria.setGeometry(QRect(75, 120, 221, 22))
        self.label_31 = QLabel(self.page_productos_agregar)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(75, 170, 150, 20))
        self.label_32 = QLabel(self.page_productos_agregar)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(75, 94, 221, 20))
        self.productos_agregar_existencia = QSpinBox(self.page_productos_agregar)
        self.productos_agregar_existencia.setObjectName(u"productos_agregar_existencia")
        self.productos_agregar_existencia.setGeometry(QRect(75, 276, 241, 22))
        self.productos_agregar_existencia.setMaximum(10000)
        self.productos_agregar_descripcion = QTextEdit(self.page_productos_agregar)
        self.productos_agregar_descripcion.setObjectName(u"productos_agregar_descripcion")
        self.productos_agregar_descripcion.setGeometry(QRect(373, 194, 250, 181))
        self.productos_agregar_precio = QDoubleSpinBox(self.page_productos_agregar)
        self.productos_agregar_precio.setObjectName(u"productos_agregar_precio")
        self.productos_agregar_precio.setGeometry(QRect(75, 196, 241, 22))
        self.productos_agregar_precio.setMaximum(10000.000000000000000)
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
        self.productos_agregar_guardar = QPushButton(self.page_productos_agregar)
        self.productos_agregar_guardar.setObjectName(u"productos_agregar_guardar")
        self.productos_agregar_guardar.setGeometry(QRect(300, 390, 150, 30))
        self.productos_agregar_guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.productos_stacked.addWidget(self.page_productos_agregar)
        self.page_productos_editar = QWidget()
        self.page_productos_editar.setObjectName(u"page_productos_editar")
        self.label_35 = QLabel(self.page_productos_editar)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(75, 150, 150, 20))
        self.label_36 = QLabel(self.page_productos_editar)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(370, 164, 150, 20))
        self.productos_editar_categoria = QComboBox(self.page_productos_editar)
        self.productos_editar_categoria.setObjectName(u"productos_editar_categoria")
        self.productos_editar_categoria.setGeometry(QRect(75, 40, 200, 35))
        self.productos_editar_categoria.setCursor(QCursor(Qt.PointingHandCursor))
        self.productos_editar_nombre = QComboBox(self.page_productos_editar)
        self.productos_editar_nombre.setObjectName(u"productos_editar_nombre")
        self.productos_editar_nombre.setGeometry(QRect(400, 40, 230, 35))
        self.line_52 = QFrame(self.page_productos_editar)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setGeometry(QRect(75, 290, 250, 2))
        self.line_52.setFrameShape(QFrame.HLine)
        self.line_52.setFrameShadow(QFrame.Sunken)
        self.productos_editar_nuevo_nombre = QLineEdit(self.page_productos_editar)
        self.productos_editar_nuevo_nombre.setObjectName(u"productos_editar_nuevo_nombre")
        self.productos_editar_nuevo_nombre.setGeometry(QRect(370, 120, 221, 22))
        self.line_53 = QFrame(self.page_productos_editar)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setGeometry(QRect(75, 200, 250, 2))
        self.line_53.setFrameShape(QFrame.HLine)
        self.line_53.setFrameShadow(QFrame.Sunken)
        self.label_38 = QLabel(self.page_productos_editar)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(75, 240, 150, 20))
        self.label_39 = QLabel(self.page_productos_editar)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(370, 94, 251, 20))
        self.productos_editar_resurtible = QCheckBox(self.page_productos_editar)
        self.productos_editar_resurtible.setObjectName(u"productos_editar_resurtible")
        self.productos_editar_resurtible.setGeometry(QRect(300, 340, 23, 23))
        self.productos_editar_precio = QDoubleSpinBox(self.page_productos_editar)
        self.productos_editar_precio.setObjectName(u"productos_editar_precio")
        self.productos_editar_precio.setGeometry(QRect(75, 176, 241, 22))
        self.productos_editar_existencia = QSpinBox(self.page_productos_editar)
        self.productos_editar_existencia.setObjectName(u"productos_editar_existencia")
        self.productos_editar_existencia.setGeometry(QRect(75, 266, 241, 22))
        self.line_54 = QFrame(self.page_productos_editar)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setGeometry(QRect(370, 144, 250, 2))
        self.line_54.setFrameShape(QFrame.HLine)
        self.line_54.setFrameShadow(QFrame.Sunken)
        self.productos_editar_descripcion = QTextEdit(self.page_productos_editar)
        self.productos_editar_descripcion.setObjectName(u"productos_editar_descripcion")
        self.productos_editar_descripcion.setGeometry(QRect(373, 194, 250, 181))
        self.label_40 = QLabel(self.page_productos_editar)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(75, 340, 101, 20))
        self.productos_editar_guardar = QPushButton(self.page_productos_editar)
        self.productos_editar_guardar.setObjectName(u"productos_editar_guardar")
        self.productos_editar_guardar.setGeometry(QRect(300, 390, 150, 30))
        self.productos_editar_guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.productos_stacked.addWidget(self.page_productos_editar)

        self.verticalLayout_9.addWidget(self.productos_stacked)

        self.stackedWidget.addWidget(self.page_productos)
        self.page_proveedores = QWidget()
        self.page_proveedores.setObjectName(u"page_proveedores")
        self.verticalLayout_10 = QVBoxLayout(self.page_proveedores)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(150, 40, 150, 40)
        self.box_proveedores_top_buttons = QFrame(self.page_proveedores)
        self.box_proveedores_top_buttons.setObjectName(u"box_proveedores_top_buttons")
        self.box_proveedores_top_buttons.setMinimumSize(QSize(0, 30))
        self.box_proveedores_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.box_proveedores_top_buttons.setFrameShadow(QFrame.Raised)
        self.proveedores_ver = QPushButton(self.box_proveedores_top_buttons)
        self.proveedores_ver.setObjectName(u"proveedores_ver")
        self.proveedores_ver.setGeometry(QRect(0, 0, 150, 30))
        self.proveedores_ver.setCursor(QCursor(Qt.PointingHandCursor))
        self.proveedores_agregar = QPushButton(self.box_proveedores_top_buttons)
        self.proveedores_agregar.setObjectName(u"proveedores_agregar")
        self.proveedores_agregar.setGeometry(QRect(150, 0, 150, 30))
        self.proveedores_agregar.setCursor(QCursor(Qt.PointingHandCursor))
        self.proveedores_editar = QPushButton(self.box_proveedores_top_buttons)
        self.proveedores_editar.setObjectName(u"proveedores_editar")
        self.proveedores_editar.setGeometry(QRect(300, 0, 150, 30))
        self.proveedores_editar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.box_proveedores_top_buttons)

        self.proveedores_stacked = QStackedWidget(self.page_proveedores)
        self.proveedores_stacked.setObjectName(u"proveedores_stacked")
        self.page_proveedores_ver = QWidget()
        self.page_proveedores_ver.setObjectName(u"page_proveedores_ver")
        self.proveedores_ver_proveedor = QComboBox(self.page_proveedores_ver)
        self.proveedores_ver_proveedor.setObjectName(u"proveedores_ver_proveedor")
        self.proveedores_ver_proveedor.setGeometry(QRect(75, 40, 200, 35))
        self.proveedores_ver_proveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.proveedores_ver_rfc = QLineEdit(self.page_proveedores_ver)
        self.proveedores_ver_rfc.setObjectName(u"proveedores_ver_rfc")
        self.proveedores_ver_rfc.setEnabled(False)
        self.proveedores_ver_rfc.setGeometry(QRect(75, 116, 250, 22))
        self.label_37 = QLabel(self.page_proveedores_ver)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(75, 90, 150, 20))
        self.line_15 = QFrame(self.page_proveedores_ver)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(75, 140, 250, 2))
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setLineWidth(1)
        self.line_15.setFrameShape(QFrame.HLine)
        self.label_41 = QLabel(self.page_proveedores_ver)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(75, 160, 150, 20))
        self.line_16 = QFrame(self.page_proveedores_ver)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(75, 210, 250, 2))
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)
        self.label_42 = QLabel(self.page_proveedores_ver)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(75, 230, 150, 20))
        self.line_17 = QFrame(self.page_proveedores_ver)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setGeometry(QRect(75, 280, 250, 2))
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)
        self.label_43 = QLabel(self.page_proveedores_ver)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(370, 60, 161, 20))
        self.productos_ver_check_activo = QCheckBox(self.page_proveedores_ver)
        self.productos_ver_check_activo.setObjectName(u"productos_ver_check_activo")
        self.productos_ver_check_activo.setEnabled(False)
        self.productos_ver_check_activo.setGeometry(QRect(540, 60, 23, 23))
        self.proveedores_ver_telefono = QLineEdit(self.page_proveedores_ver)
        self.proveedores_ver_telefono.setObjectName(u"proveedores_ver_telefono")
        self.proveedores_ver_telefono.setEnabled(False)
        self.proveedores_ver_telefono.setGeometry(QRect(75, 185, 250, 22))
        self.proveedores_ver_direccion = QLineEdit(self.page_proveedores_ver)
        self.proveedores_ver_direccion.setObjectName(u"proveedores_ver_direccion")
        self.proveedores_ver_direccion.setEnabled(False)
        self.proveedores_ver_direccion.setGeometry(QRect(75, 255, 250, 22))
        self.proveedores_stacked.addWidget(self.page_proveedores_ver)
        self.page_proveedores_agregar = QWidget()
        self.page_proveedores_agregar.setObjectName(u"page_proveedores_agregar")
        self.line_18 = QFrame(self.page_proveedores_agregar)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setGeometry(QRect(75, 300, 250, 2))
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)
        self.label_45 = QLabel(self.page_proveedores_agregar)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(75, 250, 150, 20))
        self.proveedor_agregar_nombre = QLineEdit(self.page_proveedores_agregar)
        self.proveedor_agregar_nombre.setObjectName(u"proveedor_agregar_nombre")
        self.proveedor_agregar_nombre.setGeometry(QRect(75, 66, 221, 22))
        self.label_48 = QLabel(self.page_proveedores_agregar)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(75, 40, 221, 20))
        self.line_28 = QFrame(self.page_proveedores_agregar)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setGeometry(QRect(75, 90, 220, 2))
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)
        self.proveedores_agregar_guardar = QPushButton(self.page_proveedores_agregar)
        self.proveedores_agregar_guardar.setObjectName(u"proveedores_agregar_guardar")
        self.proveedores_agregar_guardar.setGeometry(QRect(300, 350, 150, 30))
        self.proveedores_agregar_guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_49 = QLabel(self.page_proveedores_agregar)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(75, 110, 150, 20))
        self.proveedor_agregar_rfc = QLineEdit(self.page_proveedores_agregar)
        self.proveedor_agregar_rfc.setObjectName(u"proveedor_agregar_rfc")
        self.proveedor_agregar_rfc.setGeometry(QRect(75, 136, 221, 22))
        self.line_30 = QFrame(self.page_proveedores_agregar)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setGeometry(QRect(75, 160, 220, 2))
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)
        self.line_51 = QFrame(self.page_proveedores_agregar)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setGeometry(QRect(75, 234, 220, 2))
        self.line_51.setFrameShape(QFrame.HLine)
        self.line_51.setFrameShadow(QFrame.Sunken)
        self.label_56 = QLabel(self.page_proveedores_agregar)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(75, 184, 150, 20))
        self.proveedor_agregar_telefono = QLineEdit(self.page_proveedores_agregar)
        self.proveedor_agregar_telefono.setObjectName(u"proveedor_agregar_telefono")
        self.proveedor_agregar_telefono.setGeometry(QRect(75, 210, 221, 22))
        self.proveedor_agregar_direccion = QLineEdit(self.page_proveedores_agregar)
        self.proveedor_agregar_direccion.setObjectName(u"proveedor_agregar_direccion")
        self.proveedor_agregar_direccion.setGeometry(QRect(75, 275, 221, 22))
        self.proveedores_stacked.addWidget(self.page_proveedores_agregar)
        self.page_proveedores_editar = QWidget()
        self.page_proveedores_editar.setObjectName(u"page_proveedores_editar")
        self.label_51 = QLabel(self.page_proveedores_editar)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(75, 110, 150, 20))
        self.label_52 = QLabel(self.page_proveedores_editar)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(360, 170, 150, 20))
        self.proveedores_editar_check_activo = QCheckBox(self.page_proveedores_editar)
        self.proveedores_editar_check_activo.setObjectName(u"proveedores_editar_check_activo")
        self.proveedores_editar_check_activo.setGeometry(QRect(530, 50, 23, 23))
        self.proveedores_editar_check_activo.setCursor(QCursor(Qt.PointingHandCursor))
        self.proveedores_editar_nombre = QComboBox(self.page_proveedores_editar)
        self.proveedores_editar_nombre.setObjectName(u"proveedores_editar_nombre")
        self.proveedores_editar_nombre.setGeometry(QRect(75, 40, 200, 35))
        self.proveedores_editar_nombre.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_56 = QFrame(self.page_proveedores_editar)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setGeometry(QRect(75, 160, 250, 2))
        self.line_56.setFrameShape(QFrame.HLine)
        self.line_56.setFrameShadow(QFrame.Sunken)
        self.label_54 = QLabel(self.page_proveedores_editar)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(360, 50, 161, 20))
        self.proveedores_editar_nota = QTextEdit(self.page_proveedores_editar)
        self.proveedores_editar_nota.setObjectName(u"proveedores_editar_nota")
        self.proveedores_editar_nota.setEnabled(False)
        self.proveedores_editar_nota.setGeometry(QRect(360, 194, 200, 111))
        self.proveedores_editar_rfc = QLineEdit(self.page_proveedores_editar)
        self.proveedores_editar_rfc.setObjectName(u"proveedores_editar_rfc")
        self.proveedores_editar_rfc.setGeometry(QRect(75, 135, 250, 22))
        self.label_53 = QLabel(self.page_proveedores_editar)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(360, 105, 150, 20))
        self.proveedores_editar_editar_nombre = QLineEdit(self.page_proveedores_editar)
        self.proveedores_editar_editar_nombre.setObjectName(u"proveedores_editar_editar_nombre")
        self.proveedores_editar_editar_nombre.setGeometry(QRect(360, 130, 201, 22))
        self.line_57 = QFrame(self.page_proveedores_editar)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setGeometry(QRect(360, 155, 200, 2))
        self.line_57.setFrameShape(QFrame.HLine)
        self.line_57.setFrameShadow(QFrame.Sunken)
        self.label_55 = QLabel(self.page_proveedores_editar)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(75, 180, 150, 20))
        self.proveedores_editar_telefono = QLineEdit(self.page_proveedores_editar)
        self.proveedores_editar_telefono.setObjectName(u"proveedores_editar_telefono")
        self.proveedores_editar_telefono.setGeometry(QRect(75, 205, 250, 22))
        self.line_58 = QFrame(self.page_proveedores_editar)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setGeometry(QRect(75, 230, 250, 2))
        self.line_58.setFrameShape(QFrame.HLine)
        self.line_58.setFrameShadow(QFrame.Sunken)
        self.label_57 = QLabel(self.page_proveedores_editar)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(75, 250, 150, 20))
        self.proveedores_editar_direccion = QLineEdit(self.page_proveedores_editar)
        self.proveedores_editar_direccion.setObjectName(u"proveedores_editar_direccion")
        self.proveedores_editar_direccion.setGeometry(QRect(75, 275, 250, 22))
        self.line_59 = QFrame(self.page_proveedores_editar)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setGeometry(QRect(75, 300, 250, 2))
        self.line_59.setFrameShape(QFrame.HLine)
        self.line_59.setFrameShadow(QFrame.Sunken)
        self.proveedores_editar_guardar = QPushButton(self.page_proveedores_editar)
        self.proveedores_editar_guardar.setObjectName(u"proveedores_editar_guardar")
        self.proveedores_editar_guardar.setGeometry(QRect(310, 360, 150, 30))
        self.proveedores_editar_guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.proveedores_stacked.addWidget(self.page_proveedores_editar)

        self.verticalLayout_10.addWidget(self.proveedores_stacked)

        self.stackedWidget.addWidget(self.page_proveedores)
        self.page_tickets = QWidget()
        self.page_tickets.setObjectName(u"page_tickets")
        self.verticalLayout_11 = QVBoxLayout(self.page_tickets)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 15, 0, 0)
        self.frame_2 = QFrame(self.page_tickets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 85))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.tickets_check_filtro_folio = QRadioButton(self.frame_2)
        self.tickets_check_filtro_folio.setObjectName(u"tickets_check_filtro_folio")
        self.tickets_check_filtro_folio.setGeometry(QRect(30, 0, 23, 23))
        self.tickets_check_filtro_fecha = QRadioButton(self.frame_2)
        self.tickets_check_filtro_fecha.setObjectName(u"tickets_check_filtro_fecha")
        self.tickets_check_filtro_fecha.setGeometry(QRect(200, 0, 23, 23))
        self.tickets_check_filtro_rango_fechas = QRadioButton(self.frame_2)
        self.tickets_check_filtro_rango_fechas.setObjectName(u"tickets_check_filtro_rango_fechas")
        self.tickets_check_filtro_rango_fechas.setGeometry(QRect(370, 0, 23, 23))
        self.line_27 = QFrame(self.frame_2)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setGeometry(QRect(30, 80, 130, 2))
        self.line_27.setFrameShape(QFrame.HLine)
        self.line_27.setFrameShadow(QFrame.Sunken)
        self.tickets_filtro_fecha_f = QDateEdit(self.frame_2)
        self.tickets_filtro_fecha_f.setObjectName(u"tickets_filtro_fecha_f")
        self.tickets_filtro_fecha_f.setEnabled(False)
        self.tickets_filtro_fecha_f.setGeometry(QRect(510, 50, 130, 22))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 30, 150, 20))
        self.tickets_filtro_fecha = QDateEdit(self.frame_2)
        self.tickets_filtro_fecha.setObjectName(u"tickets_filtro_fecha")
        self.tickets_filtro_fecha.setEnabled(False)
        self.tickets_filtro_fecha.setGeometry(QRect(199, 55, 130, 22))
        self.line_29 = QFrame(self.frame_2)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setGeometry(QRect(199, 80, 110, 2))
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 34, 150, 20))
        self.tickets_filtro_folio = QLineEdit(self.frame_2)
        self.tickets_filtro_folio.setObjectName(u"tickets_filtro_folio")
        self.tickets_filtro_folio.setGeometry(QRect(30, 55, 113, 22))
        self.line_55 = QFrame(self.frame_2)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setGeometry(QRect(370, 80, 110, 2))
        self.line_55.setFrameShape(QFrame.HLine)
        self.line_55.setFrameShadow(QFrame.Sunken)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 29, 171, 20))
        self.tickets_filtro_fecha_i = QDateEdit(self.frame_2)
        self.tickets_filtro_fecha_i.setObjectName(u"tickets_filtro_fecha_i")
        self.tickets_filtro_fecha_i.setEnabled(False)
        self.tickets_filtro_fecha_i.setGeometry(QRect(370, 50, 130, 22))
        self.line_60 = QFrame(self.frame_2)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setGeometry(QRect(510, 80, 110, 2))
        self.line_60.setFrameShape(QFrame.HLine)
        self.line_60.setFrameShadow(QFrame.Sunken)
        self.label_44 = QLabel(self.frame_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(490, 50, 21, 20))
        self.tickets_borrar_filtros = QPushButton(self.frame_2)
        self.tickets_borrar_filtros.setObjectName(u"tickets_borrar_filtros")
        self.tickets_borrar_filtros.setGeometry(QRect(660, 50, 120, 30))
        self.tickets_borrar_filtros.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_tickets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tickets_table_widget = QTableWidget(self.frame_3)
        if (self.tickets_table_widget.columnCount() < 10):
            self.tickets_table_widget.setColumnCount(10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tickets_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tickets_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tickets_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tickets_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tickets_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tickets_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tickets_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tickets_table_widget.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tickets_table_widget.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tickets_table_widget.setHorizontalHeaderItem(9, __qtablewidgetitem20)
        self.tickets_table_widget.setObjectName(u"tickets_table_widget")
        self.tickets_table_widget.setRowCount(0)
        self.tickets_table_widget.setColumnCount(10)

        self.verticalLayout_12.addWidget(self.tickets_table_widget)


        self.verticalLayout_11.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.page_tickets)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.Tickets_generar_ticket = QPushButton(self.frame_4)
        self.Tickets_generar_ticket.setObjectName(u"Tickets_generar_ticket")
        self.Tickets_generar_ticket.setGeometry(QRect(450, 0, 150, 30))
        self.Tickets_generar_ticket.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_tickets)
        self.page_recorte_caja = QWidget()
        self.page_recorte_caja.setObjectName(u"page_recorte_caja")
        self.verticalLayout_14 = QVBoxLayout(self.page_recorte_caja)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_7 = QFrame(self.page_recorte_caja)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 85))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.line_61 = QFrame(self.frame_7)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setGeometry(QRect(30, 80, 130, 2))
        self.line_61.setFrameShape(QFrame.HLine)
        self.line_61.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 30, 161, 20))
        self.recorte_caja_fecha = QDateEdit(self.frame_7)
        self.recorte_caja_fecha.setObjectName(u"recorte_caja_fecha")
        self.recorte_caja_fecha.setEnabled(False)
        self.recorte_caja_fecha.setGeometry(QRect(30, 55, 131, 22))

        self.verticalLayout_14.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.page_recorte_caja)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.recorte_caja_table_widget = QTableWidget(self.frame_5)
        if (self.recorte_caja_table_widget.columnCount() < 3):
            self.recorte_caja_table_widget.setColumnCount(3)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.recorte_caja_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.recorte_caja_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.recorte_caja_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        self.recorte_caja_table_widget.setObjectName(u"recorte_caja_table_widget")
        self.recorte_caja_table_widget.setRowCount(0)
        self.recorte_caja_table_widget.setColumnCount(3)

        self.verticalLayout_13.addWidget(self.recorte_caja_table_widget)


        self.verticalLayout_14.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.page_recorte_caja)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 40))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.recorte_caja_generar_ticket = QPushButton(self.frame_6)
        self.recorte_caja_generar_ticket.setObjectName(u"recorte_caja_generar_ticket")
        self.recorte_caja_generar_ticket.setGeometry(QRect(450, 0, 150, 30))
        self.recorte_caja_generar_ticket.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_recorte_caja)
        self.page_copia_seguridad = QWidget()
        self.page_copia_seguridad.setObjectName(u"page_copia_seguridad")
        self.horizontalLayout_13 = QHBoxLayout(self.page_copia_seguridad)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_8 = QFrame(self.page_copia_seguridad)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(150, 0))
        self.frame_8.setMaximumSize(QSize(150, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.donwload = QPushButton(self.frame_8)
        self.donwload.setObjectName(u"donwload")
        self.donwload.setGeometry(QRect(0, 150, 150, 150))
        self.donwload.setMinimumSize(QSize(150, 150))
        self.donwload.setMaximumSize(QSize(150, 150))
        self.donwload.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(24, 310, 101, 24))

        self.horizontalLayout_13.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.page_copia_seguridad)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(150, 0))
        self.frame_9.setMaximumSize(QSize(150, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.upload = QPushButton(self.frame_9)
        self.upload.setObjectName(u"upload")
        self.upload.setGeometry(QRect(0, 150, 150, 150))
        self.upload.setMinimumSize(QSize(150, 150))
        self.upload.setMaximumSize(QSize(150, 150))
        self.upload.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_46 = QLabel(self.frame_9)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(0, 310, 139, 24))

        self.horizontalLayout_13.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.page_copia_seguridad)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.verticalLayout_15 = QVBoxLayout(self.page_admin)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(30, 0, 30, 20)
        self.box_administrador_top_buttons = QFrame(self.page_admin)
        self.box_administrador_top_buttons.setObjectName(u"box_administrador_top_buttons")
        self.box_administrador_top_buttons.setMinimumSize(QSize(0, 50))
        self.box_administrador_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.box_administrador_top_buttons.setFrameShadow(QFrame.Raised)
        self.administrador_ver_tados = QPushButton(self.box_administrador_top_buttons)
        self.administrador_ver_tados.setObjectName(u"administrador_ver_tados")
        self.administrador_ver_tados.setGeometry(QRect(0, 20, 150, 30))
        self.administrador_ver_tados.setCursor(QCursor(Qt.PointingHandCursor))
        self.administrador_agregar_empleado = QPushButton(self.box_administrador_top_buttons)
        self.administrador_agregar_empleado.setObjectName(u"administrador_agregar_empleado")
        self.administrador_agregar_empleado.setGeometry(QRect(150, 20, 150, 30))
        self.administrador_agregar_empleado.setCursor(QCursor(Qt.PointingHandCursor))
        self.administrador_ver_empleados = QPushButton(self.box_administrador_top_buttons)
        self.administrador_ver_empleados.setObjectName(u"administrador_ver_empleados")
        self.administrador_ver_empleados.setGeometry(QRect(300, 20, 150, 30))
        self.administrador_ver_empleados.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_15.addWidget(self.box_administrador_top_buttons)

        self.administrador_stacked = QStackedWidget(self.page_admin)
        self.administrador_stacked.setObjectName(u"administrador_stacked")
        self.datos_personales = QWidget()
        self.datos_personales.setObjectName(u"datos_personales")
        self.line_70 = QFrame(self.datos_personales)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setGeometry(QRect(220, 94, 250, 2))
        self.line_70.setFrameShape(QFrame.HLine)
        self.line_70.setFrameShadow(QFrame.Sunken)
        self.label_64 = QLabel(self.datos_personales)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(220, 44, 241, 20))
        self.administrador_ver_nombre = QLineEdit(self.datos_personales)
        self.administrador_ver_nombre.setObjectName(u"administrador_ver_nombre")
        self.administrador_ver_nombre.setGeometry(QRect(220, 70, 250, 22))
        self.label_65 = QLabel(self.datos_personales)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(220, 110, 241, 20))
        self.line_71 = QFrame(self.datos_personales)
        self.line_71.setObjectName(u"line_71")
        self.line_71.setGeometry(QRect(220, 160, 250, 2))
        self.line_71.setFrameShape(QFrame.HLine)
        self.line_71.setFrameShadow(QFrame.Sunken)
        self.administrador_ver_apellido_p = QLineEdit(self.datos_personales)
        self.administrador_ver_apellido_p.setObjectName(u"administrador_ver_apellido_p")
        self.administrador_ver_apellido_p.setGeometry(QRect(220, 136, 250, 22))
        self.label_66 = QLabel(self.datos_personales)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(220, 180, 241, 20))
        self.line_72 = QFrame(self.datos_personales)
        self.line_72.setObjectName(u"line_72")
        self.line_72.setGeometry(QRect(220, 230, 250, 2))
        self.line_72.setFrameShape(QFrame.HLine)
        self.line_72.setFrameShadow(QFrame.Sunken)
        self.administrador_ver_apellido_m = QLineEdit(self.datos_personales)
        self.administrador_ver_apellido_m.setObjectName(u"administrador_ver_apellido_m")
        self.administrador_ver_apellido_m.setGeometry(QRect(220, 206, 250, 22))
        self.label_67 = QLabel(self.datos_personales)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(220, 250, 231, 20))
        self.line_73 = QFrame(self.datos_personales)
        self.line_73.setObjectName(u"line_73")
        self.line_73.setGeometry(QRect(220, 300, 250, 2))
        self.line_73.setFrameShape(QFrame.HLine)
        self.line_73.setFrameShadow(QFrame.Sunken)
        self.administrador_ver_salario = QDoubleSpinBox(self.datos_personales)
        self.administrador_ver_salario.setObjectName(u"administrador_ver_salario")
        self.administrador_ver_salario.setEnabled(False)
        self.administrador_ver_salario.setGeometry(QRect(220, 276, 251, 22))
        self.administrador_ver_salario.setMaximum(100000.000000000000000)
        self.line_vertical_2 = QFrame(self.datos_personales)
        self.line_vertical_2.setObjectName(u"line_vertical_2")
        self.line_vertical_2.setGeometry(QRect(500, 60, 1, 240))
        self.line_vertical_2.setFrameShape(QFrame.VLine)
        self.line_vertical_2.setFrameShadow(QFrame.Sunken)
        self.label_68 = QLabel(self.datos_personales)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(530, 44, 150, 20))
        self.line_74 = QFrame(self.datos_personales)
        self.line_74.setObjectName(u"line_74")
        self.line_74.setGeometry(QRect(530, 94, 250, 2))
        self.line_74.setFrameShape(QFrame.HLine)
        self.line_74.setFrameShadow(QFrame.Sunken)
        self.administrador_editar_nombre_usuario = QLineEdit(self.datos_personales)
        self.administrador_editar_nombre_usuario.setObjectName(u"administrador_editar_nombre_usuario")
        self.administrador_editar_nombre_usuario.setGeometry(QRect(530, 70, 250, 22))
        self.label_69 = QLabel(self.datos_personales)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(530, 110, 150, 20))
        self.line_75 = QFrame(self.datos_personales)
        self.line_75.setObjectName(u"line_75")
        self.line_75.setGeometry(QRect(530, 160, 250, 2))
        self.line_75.setFrameShape(QFrame.HLine)
        self.line_75.setFrameShadow(QFrame.Sunken)
        self.administrador_editar_correo = QLineEdit(self.datos_personales)
        self.administrador_editar_correo.setObjectName(u"administrador_editar_correo")
        self.administrador_editar_correo.setGeometry(QRect(530, 136, 250, 22))
        self.label_70 = QLabel(self.datos_personales)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(530, 180, 251, 20))
        self.line_76 = QFrame(self.datos_personales)
        self.line_76.setObjectName(u"line_76")
        self.line_76.setGeometry(QRect(530, 230, 250, 2))
        self.line_76.setFrameShape(QFrame.HLine)
        self.line_76.setFrameShadow(QFrame.Sunken)
        self.administrador_contrasenia_antigua = QLineEdit(self.datos_personales)
        self.administrador_contrasenia_antigua.setObjectName(u"administrador_contrasenia_antigua")
        self.administrador_contrasenia_antigua.setGeometry(QRect(530, 206, 250, 22))
        self.label_71 = QLabel(self.datos_personales)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(530, 250, 241, 20))
        self.line_77 = QFrame(self.datos_personales)
        self.line_77.setObjectName(u"line_77")
        self.line_77.setGeometry(QRect(530, 300, 250, 2))
        self.line_77.setFrameShape(QFrame.HLine)
        self.line_77.setFrameShadow(QFrame.Sunken)
        self.administrador_cambiar_contrasenia = QLineEdit(self.datos_personales)
        self.administrador_cambiar_contrasenia.setObjectName(u"administrador_cambiar_contrasenia")
        self.administrador_cambiar_contrasenia.setGeometry(QRect(530, 276, 250, 22))
        self.administrador_guardar_cambios = QPushButton(self.datos_personales)
        self.administrador_guardar_cambios.setObjectName(u"administrador_guardar_cambios")
        self.administrador_guardar_cambios.setGeometry(QRect(430, 376, 150, 30))
        self.administrador_guardar_cambios.setCursor(QCursor(Qt.PointingHandCursor))
        self.administrador_stacked.addWidget(self.datos_personales)
        self.agregar_empleado = QWidget()
        self.agregar_empleado.setObjectName(u"agregar_empleado")
        self.label_72 = QLabel(self.agregar_empleado)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(220, 250, 231, 20))
        self.line_vertical_3 = QFrame(self.agregar_empleado)
        self.line_vertical_3.setObjectName(u"line_vertical_3")
        self.line_vertical_3.setGeometry(QRect(500, 60, 1, 240))
        self.line_vertical_3.setFrameShape(QFrame.VLine)
        self.line_vertical_3.setFrameShadow(QFrame.Sunken)
        self.administrador_agregar_contrasenia = QLineEdit(self.agregar_empleado)
        self.administrador_agregar_contrasenia.setObjectName(u"administrador_agregar_contrasenia")
        self.administrador_agregar_contrasenia.setGeometry(QRect(530, 206, 250, 22))
        self.line_78 = QFrame(self.agregar_empleado)
        self.line_78.setObjectName(u"line_78")
        self.line_78.setGeometry(QRect(220, 300, 250, 2))
        self.line_78.setFrameShape(QFrame.HLine)
        self.line_78.setFrameShadow(QFrame.Sunken)
        self.label_73 = QLabel(self.agregar_empleado)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(530, 110, 150, 20))
        self.administrador_agregar_apellido_m = QLineEdit(self.agregar_empleado)
        self.administrador_agregar_apellido_m.setObjectName(u"administrador_agregar_apellido_m")
        self.administrador_agregar_apellido_m.setGeometry(QRect(220, 206, 250, 22))
        self.line_79 = QFrame(self.agregar_empleado)
        self.line_79.setObjectName(u"line_79")
        self.line_79.setGeometry(QRect(220, 230, 250, 2))
        self.line_79.setFrameShape(QFrame.HLine)
        self.line_79.setFrameShadow(QFrame.Sunken)
        self.label_75 = QLabel(self.agregar_empleado)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(220, 110, 241, 20))
        self.line_80 = QFrame(self.agregar_empleado)
        self.line_80.setObjectName(u"line_80")
        self.line_80.setGeometry(QRect(220, 160, 250, 2))
        self.line_80.setFrameShape(QFrame.HLine)
        self.line_80.setFrameShadow(QFrame.Sunken)
        self.line_81 = QFrame(self.agregar_empleado)
        self.line_81.setObjectName(u"line_81")
        self.line_81.setGeometry(QRect(220, 94, 250, 2))
        self.line_81.setFrameShape(QFrame.HLine)
        self.line_81.setFrameShadow(QFrame.Sunken)
        self.line_82 = QFrame(self.agregar_empleado)
        self.line_82.setObjectName(u"line_82")
        self.line_82.setGeometry(QRect(530, 94, 250, 2))
        self.line_82.setFrameShape(QFrame.HLine)
        self.line_82.setFrameShadow(QFrame.Sunken)
        self.line_83 = QFrame(self.agregar_empleado)
        self.line_83.setObjectName(u"line_83")
        self.line_83.setGeometry(QRect(530, 230, 250, 2))
        self.line_83.setFrameShape(QFrame.HLine)
        self.line_83.setFrameShadow(QFrame.Sunken)
        self.administrador_agregar_apellido_p = QLineEdit(self.agregar_empleado)
        self.administrador_agregar_apellido_p.setObjectName(u"administrador_agregar_apellido_p")
        self.administrador_agregar_apellido_p.setGeometry(QRect(220, 136, 250, 22))
        self.label_76 = QLabel(self.agregar_empleado)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(220, 180, 241, 20))
        self.label_77 = QLabel(self.agregar_empleado)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(530, 44, 150, 20))
        self.administrador_agregar_salario = QDoubleSpinBox(self.agregar_empleado)
        self.administrador_agregar_salario.setObjectName(u"administrador_agregar_salario")
        self.administrador_agregar_salario.setEnabled(True)
        self.administrador_agregar_salario.setGeometry(QRect(220, 276, 251, 22))
        self.administrador_agregar_salario.setMaximum(100000.000000000000000)
        self.label_78 = QLabel(self.agregar_empleado)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(530, 180, 251, 20))
        self.label_79 = QLabel(self.agregar_empleado)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(220, 44, 241, 20))
        self.administrador_agregar_nombre = QLineEdit(self.agregar_empleado)
        self.administrador_agregar_nombre.setObjectName(u"administrador_agregar_nombre")
        self.administrador_agregar_nombre.setGeometry(QRect(220, 70, 250, 22))
        self.administrador_agregar_correo = QLineEdit(self.agregar_empleado)
        self.administrador_agregar_correo.setObjectName(u"administrador_agregar_correo")
        self.administrador_agregar_correo.setGeometry(QRect(530, 136, 250, 22))
        self.line_85 = QFrame(self.agregar_empleado)
        self.line_85.setObjectName(u"line_85")
        self.line_85.setGeometry(QRect(530, 160, 250, 2))
        self.line_85.setFrameShape(QFrame.HLine)
        self.line_85.setFrameShadow(QFrame.Sunken)
        self.administrador_nuevo_empleado_guardar_cambios = QPushButton(self.agregar_empleado)
        self.administrador_nuevo_empleado_guardar_cambios.setObjectName(u"administrador_nuevo_empleado_guardar_cambios")
        self.administrador_nuevo_empleado_guardar_cambios.setGeometry(QRect(430, 376, 150, 30))
        self.administrador_nuevo_empleado_guardar_cambios.setCursor(QCursor(Qt.PointingHandCursor))
        self.administrador_agregar_nombre_usuario = QLineEdit(self.agregar_empleado)
        self.administrador_agregar_nombre_usuario.setObjectName(u"administrador_agregar_nombre_usuario")
        self.administrador_agregar_nombre_usuario.setGeometry(QRect(530, 70, 250, 22))
        self.administrador_stacked.addWidget(self.agregar_empleado)
        self.ver_empleados = QWidget()
        self.ver_empleados.setObjectName(u"ver_empleados")
        self.administrador_ver_empleado_apellido_p = QLineEdit(self.ver_empleados)
        self.administrador_ver_empleado_apellido_p.setObjectName(u"administrador_ver_empleado_apellido_p")
        self.administrador_ver_empleado_apellido_p.setEnabled(False)
        self.administrador_ver_empleado_apellido_p.setGeometry(QRect(220, 210, 250, 22))
        self.label_80 = QLabel(self.ver_empleados)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(220, 254, 241, 20))
        self.administrador_ver_empleado_correo = QLineEdit(self.ver_empleados)
        self.administrador_ver_empleado_correo.setObjectName(u"administrador_ver_empleado_correo")
        self.administrador_ver_empleado_correo.setEnabled(False)
        self.administrador_ver_empleado_correo.setGeometry(QRect(530, 210, 250, 22))
        self.administrador_ver_empleado_apellido_m = QLineEdit(self.ver_empleados)
        self.administrador_ver_empleado_apellido_m.setObjectName(u"administrador_ver_empleado_apellido_m")
        self.administrador_ver_empleado_apellido_m.setEnabled(False)
        self.administrador_ver_empleado_apellido_m.setGeometry(QRect(220, 280, 250, 22))
        self.administrador_ver_empleado_salario = QDoubleSpinBox(self.ver_empleados)
        self.administrador_ver_empleado_salario.setObjectName(u"administrador_ver_empleado_salario")
        self.administrador_ver_empleado_salario.setEnabled(False)
        self.administrador_ver_empleado_salario.setGeometry(QRect(220, 350, 251, 22))
        self.administrador_ver_empleado_salario.setMaximum(100000.000000000000000)
        self.label_81 = QLabel(self.ver_empleados)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(220, 118, 241, 20))
        self.label_74 = QLabel(self.ver_empleados)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(530, 184, 150, 20))
        self.line_86 = QFrame(self.ver_empleados)
        self.line_86.setObjectName(u"line_86")
        self.line_86.setGeometry(QRect(530, 168, 250, 2))
        self.line_86.setFrameShape(QFrame.HLine)
        self.line_86.setFrameShadow(QFrame.Sunken)
        self.label_82 = QLabel(self.ver_empleados)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(220, 324, 231, 20))
        self.line_87 = QFrame(self.ver_empleados)
        self.line_87.setObjectName(u"line_87")
        self.line_87.setGeometry(QRect(220, 234, 250, 2))
        self.line_87.setFrameShape(QFrame.HLine)
        self.line_87.setFrameShadow(QFrame.Sunken)
        self.line_88 = QFrame(self.ver_empleados)
        self.line_88.setObjectName(u"line_88")
        self.line_88.setGeometry(QRect(220, 374, 250, 2))
        self.line_88.setFrameShape(QFrame.HLine)
        self.line_88.setFrameShadow(QFrame.Sunken)
        self.line_vertical_4 = QFrame(self.ver_empleados)
        self.line_vertical_4.setObjectName(u"line_vertical_4")
        self.line_vertical_4.setGeometry(QRect(500, 134, 1, 240))
        self.line_vertical_4.setFrameShape(QFrame.VLine)
        self.line_vertical_4.setFrameShadow(QFrame.Sunken)
        self.label_83 = QLabel(self.ver_empleados)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(530, 118, 150, 20))
        self.line_89 = QFrame(self.ver_empleados)
        self.line_89.setObjectName(u"line_89")
        self.line_89.setGeometry(QRect(220, 304, 250, 2))
        self.line_89.setFrameShape(QFrame.HLine)
        self.line_89.setFrameShadow(QFrame.Sunken)
        self.administrador_ver_empleado_nombre = QLineEdit(self.ver_empleados)
        self.administrador_ver_empleado_nombre.setObjectName(u"administrador_ver_empleado_nombre")
        self.administrador_ver_empleado_nombre.setEnabled(False)
        self.administrador_ver_empleado_nombre.setGeometry(QRect(220, 144, 250, 22))
        self.line_90 = QFrame(self.ver_empleados)
        self.line_90.setObjectName(u"line_90")
        self.line_90.setGeometry(QRect(530, 234, 250, 2))
        self.line_90.setFrameShape(QFrame.HLine)
        self.line_90.setFrameShadow(QFrame.Sunken)
        self.label_84 = QLabel(self.ver_empleados)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(220, 184, 241, 20))
        self.line_91 = QFrame(self.ver_empleados)
        self.line_91.setObjectName(u"line_91")
        self.line_91.setGeometry(QRect(220, 168, 250, 2))
        self.line_91.setFrameShape(QFrame.HLine)
        self.line_91.setFrameShadow(QFrame.Sunken)
        self.administrador_ver_empleado_nombre_usuario = QLineEdit(self.ver_empleados)
        self.administrador_ver_empleado_nombre_usuario.setObjectName(u"administrador_ver_empleado_nombre_usuario")
        self.administrador_ver_empleado_nombre_usuario.setEnabled(False)
        self.administrador_ver_empleado_nombre_usuario.setGeometry(QRect(530, 144, 250, 22))
        self.administrador_buscar_empleado = QComboBox(self.ver_empleados)
        self.administrador_buscar_empleado.setObjectName(u"administrador_buscar_empleado")
        self.administrador_buscar_empleado.setGeometry(QRect(220, 20, 300, 35))
        self.administrador_buscar_empleado.setCursor(QCursor(Qt.PointingHandCursor))
        self.administrador_stacked.addWidget(self.ver_empleados)

        self.verticalLayout_15.addWidget(self.administrador_stacked)

        self.stackedWidget.addWidget(self.page_admin)
        self.page_empleado = QWidget()
        self.page_empleado.setObjectName(u"page_empleado")
        self.horizontalLayout_14 = QHBoxLayout(self.page_empleado)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 50, 0, 0)
        self.empleados_stacked = QStackedWidget(self.page_empleado)
        self.empleados_stacked.setObjectName(u"empleados_stacked")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.line_62 = QFrame(self.page)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setGeometry(QRect(220, 98, 250, 2))
        self.line_62.setFrameShape(QFrame.HLine)
        self.line_62.setFrameShadow(QFrame.Sunken)
        self.label_47 = QLabel(self.page)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(220, 48, 241, 20))
        self.empleados_ver_nombre = QLineEdit(self.page)
        self.empleados_ver_nombre.setObjectName(u"empleados_ver_nombre")
        self.empleados_ver_nombre.setEnabled(True)
        self.empleados_ver_nombre.setGeometry(QRect(220, 74, 250, 22))
        self.label_50 = QLabel(self.page)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(220, 114, 241, 20))
        self.line_63 = QFrame(self.page)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setGeometry(QRect(220, 164, 250, 2))
        self.line_63.setFrameShape(QFrame.HLine)
        self.line_63.setFrameShadow(QFrame.Sunken)
        self.empleados_ver_apellido_p = QLineEdit(self.page)
        self.empleados_ver_apellido_p.setObjectName(u"empleados_ver_apellido_p")
        self.empleados_ver_apellido_p.setEnabled(True)
        self.empleados_ver_apellido_p.setGeometry(QRect(220, 140, 250, 22))
        self.label_58 = QLabel(self.page)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(220, 184, 241, 20))
        self.line_64 = QFrame(self.page)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setGeometry(QRect(220, 234, 250, 2))
        self.line_64.setFrameShape(QFrame.HLine)
        self.line_64.setFrameShadow(QFrame.Sunken)
        self.empleados_ver_apellido_m = QLineEdit(self.page)
        self.empleados_ver_apellido_m.setObjectName(u"empleados_ver_apellido_m")
        self.empleados_ver_apellido_m.setEnabled(True)
        self.empleados_ver_apellido_m.setGeometry(QRect(220, 210, 250, 22))
        self.label_59 = QLabel(self.page)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(220, 254, 231, 20))
        self.line_65 = QFrame(self.page)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setGeometry(QRect(220, 304, 250, 2))
        self.line_65.setFrameShape(QFrame.HLine)
        self.line_65.setFrameShadow(QFrame.Sunken)
        self.empleados_ver_salario = QDoubleSpinBox(self.page)
        self.empleados_ver_salario.setObjectName(u"empleados_ver_salario")
        self.empleados_ver_salario.setEnabled(False)
        self.empleados_ver_salario.setGeometry(QRect(220, 280, 251, 22))
        self.empleados_ver_salario.setMaximum(100000.000000000000000)
        self.line_vertical = QFrame(self.page)
        self.line_vertical.setObjectName(u"line_vertical")
        self.line_vertical.setGeometry(QRect(500, 64, 1, 240))
        self.line_vertical.setFrameShape(QFrame.VLine)
        self.line_vertical.setFrameShadow(QFrame.Sunken)
        self.label_60 = QLabel(self.page)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(530, 48, 150, 20))
        self.line_66 = QFrame(self.page)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setGeometry(QRect(530, 98, 250, 2))
        self.line_66.setFrameShape(QFrame.HLine)
        self.line_66.setFrameShadow(QFrame.Sunken)
        self.empleados_editar_nombre_usuario = QLineEdit(self.page)
        self.empleados_editar_nombre_usuario.setObjectName(u"empleados_editar_nombre_usuario")
        self.empleados_editar_nombre_usuario.setGeometry(QRect(530, 74, 250, 22))
        self.label_61 = QLabel(self.page)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(530, 114, 150, 20))
        self.line_67 = QFrame(self.page)
        self.line_67.setObjectName(u"line_67")
        self.line_67.setGeometry(QRect(530, 164, 250, 2))
        self.line_67.setFrameShape(QFrame.HLine)
        self.line_67.setFrameShadow(QFrame.Sunken)
        self.empleados_editar_correo = QLineEdit(self.page)
        self.empleados_editar_correo.setObjectName(u"empleados_editar_correo")
        self.empleados_editar_correo.setGeometry(QRect(530, 140, 250, 22))
        self.label_62 = QLabel(self.page)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(530, 184, 251, 20))
        self.line_68 = QFrame(self.page)
        self.line_68.setObjectName(u"line_68")
        self.line_68.setGeometry(QRect(530, 234, 250, 2))
        self.line_68.setFrameShape(QFrame.HLine)
        self.line_68.setFrameShadow(QFrame.Sunken)
        self.empleados_contrasenia_antigua = QLineEdit(self.page)
        self.empleados_contrasenia_antigua.setObjectName(u"empleados_contrasenia_antigua")
        self.empleados_contrasenia_antigua.setGeometry(QRect(530, 210, 250, 22))
        self.label_63 = QLabel(self.page)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(530, 254, 241, 20))
        self.line_69 = QFrame(self.page)
        self.line_69.setObjectName(u"line_69")
        self.line_69.setGeometry(QRect(530, 304, 250, 2))
        self.line_69.setFrameShape(QFrame.HLine)
        self.line_69.setFrameShadow(QFrame.Sunken)
        self.empleados_cambiar_contrasenia = QLineEdit(self.page)
        self.empleados_cambiar_contrasenia.setObjectName(u"empleados_cambiar_contrasenia")
        self.empleados_cambiar_contrasenia.setGeometry(QRect(530, 280, 250, 22))
        self.empleados_guardar_cambios = QPushButton(self.page)
        self.empleados_guardar_cambios.setObjectName(u"empleados_guardar_cambios")
        self.empleados_guardar_cambios.setGeometry(QRect(430, 380, 150, 30))
        self.empleados_guardar_cambios.setCursor(QCursor(Qt.PointingHandCursor))
        self.empleados_stacked.addWidget(self.page)

        self.horizontalLayout_14.addWidget(self.empleados_stacked)

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

        self.stackedWidget.setCurrentIndex(0)
        self.productos_stacked.setCurrentIndex(0)
        self.proveedores_stacked.setCurrentIndex(2)
        self.administrador_stacked.setCurrentIndex(0)


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
        self.lbl_recorte_caja.setText(QCoreApplication.translate("MainWindows", u"Corte de caja", None))
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
        self.venta_color_1.setText("")
        ___qtablewidgetitem = self.ventas_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindows", u"Categoria", None));
        ___qtablewidgetitem1 = self.ventas_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindows", u"Nombre", None));
        ___qtablewidgetitem2 = self.ventas_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindows", u"Precio", None));
        ___qtablewidgetitem3 = self.ventas_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindows", u"Unidades", None));
        ___qtablewidgetitem4 = self.ventas_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindows", u"Color", None));
        ___qtablewidgetitem5 = self.ventas_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindows", u"Total", None));
        self.ventas_generar.setText(QCoreApplication.translate("MainWindows", u"Generar Venta", None))
        self.ventas_agregar.setText(QCoreApplication.translate("MainWindows", u"Agregar Producto", None))
        self.label_3.setText(QCoreApplication.translate("MainWindows", u"Fecha", None))
        self.label_16.setText(QCoreApplication.translate("MainWindows", u"Precio", None))
        self.label_17.setText(QCoreApplication.translate("MainWindows", u"Unidades", None))
        self.label_19.setText(QCoreApplication.translate("MainWindows", u"Total", None))
        self.label_22.setText(QCoreApplication.translate("MainWindows", u"Categoria", None))
        self.label_23.setText(QCoreApplication.translate("MainWindows", u"Nombre", None))
        ___qtablewidgetitem6 = self.compras_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindows", u"Categoria", None));
        ___qtablewidgetitem7 = self.compras_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindows", u"Nombre", None));
        ___qtablewidgetitem8 = self.compras_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindows", u"Precio", None));
        ___qtablewidgetitem9 = self.compras_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindows", u"Unidades", None));
        ___qtablewidgetitem10 = self.compras_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindows", u"Total", None));
        self.compras_generar.setText(QCoreApplication.translate("MainWindows", u"Generar Compra", None))
        self.compras_agregar.setText(QCoreApplication.translate("MainWindows", u"Agregar Producto", None))
        self.productos_ver.setText(QCoreApplication.translate("MainWindows", u"Ver", None))
        self.productos_agregar.setText(QCoreApplication.translate("MainWindows", u"Agregar", None))
        self.productos_editar.setText(QCoreApplication.translate("MainWindows", u"Editar", None))
        self.label_25.setText(QCoreApplication.translate("MainWindows", u"Precio", None))
        self.label_26.setText(QCoreApplication.translate("MainWindows", u"Existencia", None))
        self.label_27.setText(QCoreApplication.translate("MainWindows", u"Resurtible", None))
        self.productos_ver_resurtible.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindows", u"Descripcion", None))
        self.label_29.setText(QCoreApplication.translate("MainWindows", u"Existencia", None))
        self.label_30.setText(QCoreApplication.translate("MainWindows", u"Descripcion", None))
        self.productos_agregar_nueva_categoria.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindows", u"Precio", None))
        self.label_32.setText(QCoreApplication.translate("MainWindows", u"Categoria", None))
        self.label_33.setText(QCoreApplication.translate("MainWindows", u"Resurtible", None))
        self.productos_agregar_resurtible.setText("")
        self.productos_agregar_check_nueva_categoria.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindows", u"Nombre", None))
        self.productos_agregar_nombre.setText("")
        self.productos_agregar_guardar.setText(QCoreApplication.translate("MainWindows", u"Agregar producto", None))
        self.label_35.setText(QCoreApplication.translate("MainWindows", u"Precio", None))
        self.label_36.setText(QCoreApplication.translate("MainWindows", u"Descripcion", None))
        self.productos_editar_nuevo_nombre.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindows", u"Existencia", None))
        self.label_39.setText(QCoreApplication.translate("MainWindows", u"Cambiar nombre", None))
        self.productos_editar_resurtible.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindows", u"Resurtible", None))
        self.productos_editar_guardar.setText(QCoreApplication.translate("MainWindows", u"Agregar producto", None))
        self.proveedores_ver.setText(QCoreApplication.translate("MainWindows", u"Ver", None))
        self.proveedores_agregar.setText(QCoreApplication.translate("MainWindows", u"Agregar", None))
        self.proveedores_editar.setText(QCoreApplication.translate("MainWindows", u"Editar", None))
        self.proveedores_ver_rfc.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindows", u"RFC", None))
        self.label_41.setText(QCoreApplication.translate("MainWindows", u"Telefono", None))
        self.label_42.setText(QCoreApplication.translate("MainWindows", u"Direccion", None))
        self.label_43.setText(QCoreApplication.translate("MainWindows", u"Proveedor activo", None))
        self.productos_ver_check_activo.setText("")
        self.proveedores_ver_telefono.setText("")
        self.proveedores_ver_direccion.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindows", u"Direccion", None))
        self.proveedor_agregar_nombre.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindows", u"Nombre del proveedor", None))
        self.proveedores_agregar_guardar.setText(QCoreApplication.translate("MainWindows", u"Crear Proveedor", None))
        self.label_49.setText(QCoreApplication.translate("MainWindows", u"RFC", None))
        self.proveedor_agregar_rfc.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindows", u"Telefono", None))
        self.proveedor_agregar_telefono.setText("")
        self.proveedor_agregar_direccion.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindows", u"RFC", None))
        self.label_52.setText(QCoreApplication.translate("MainWindows", u"Nota", None))
        self.proveedores_editar_check_activo.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindows", u"Proveedor activo", None))
        self.proveedores_editar_nota.setHtml(QCoreApplication.translate("MainWindows", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">Si un Proovedor no esta activo no podras verlo al momento de comprar porductos, asegurate de no descactivar la vista de un provedor activo.</span></p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("MainWindows", u"Cambiar nombre", None))
        self.label_55.setText(QCoreApplication.translate("MainWindows", u"Telefono", None))
        self.label_57.setText(QCoreApplication.translate("MainWindows", u"Direccion", None))
        self.proveedores_editar_guardar.setText(QCoreApplication.translate("MainWindows", u"Guardar cambios", None))
        self.tickets_check_filtro_folio.setText("")
        self.tickets_check_filtro_fecha.setText("")
        self.tickets_check_filtro_rango_fechas.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindows", u"folio", None))
        self.label_5.setText(QCoreApplication.translate("MainWindows", u"Fecha", None))
        self.label_6.setText(QCoreApplication.translate("MainWindows", u"Rango de fechas", None))
        self.label_44.setText(QCoreApplication.translate("MainWindows", u"a", None))
        self.tickets_borrar_filtros.setText(QCoreApplication.translate("MainWindows", u"Borrar Filtros", None))
        ___qtablewidgetitem11 = self.tickets_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindows", u"Folio", None));
        ___qtablewidgetitem12 = self.tickets_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindows", u"Fecha", None));
        ___qtablewidgetitem13 = self.tickets_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindows", u"Tipo", None));
        ___qtablewidgetitem14 = self.tickets_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindows", u"Nombre", None));
        ___qtablewidgetitem15 = self.tickets_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindows", u"Precio", None));
        ___qtablewidgetitem16 = self.tickets_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindows", u"Unidades", None));
        ___qtablewidgetitem17 = self.tickets_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindows", u"Total", None));
        ___qtablewidgetitem18 = self.tickets_table_widget.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindows", u"Color", None));
        ___qtablewidgetitem19 = self.tickets_table_widget.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindows", u"Empleado", None));
        ___qtablewidgetitem20 = self.tickets_table_widget.horizontalHeaderItem(9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindows", u"Rfc", None));
        self.Tickets_generar_ticket.setText(QCoreApplication.translate("MainWindows", u"Guardar copia", None))
        self.label_7.setText(QCoreApplication.translate("MainWindows", u"Fecha de recorte", None))
        ___qtablewidgetitem21 = self.recorte_caja_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindows", u"Folio", None));
        ___qtablewidgetitem22 = self.recorte_caja_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindows", u"Fecha", None));
        ___qtablewidgetitem23 = self.recorte_caja_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindows", u"Total", None));
        self.recorte_caja_generar_ticket.setText(QCoreApplication.translate("MainWindows", u"Guardar copia", None))
        self.donwload.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindows", u"Crear copia", None))
        self.upload.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindows", u"Restaurar copia", None))
        self.administrador_ver_tados.setText(QCoreApplication.translate("MainWindows", u"Datos personales", None))
        self.administrador_agregar_empleado.setText(QCoreApplication.translate("MainWindows", u"Agregar empleado", None))
        self.administrador_ver_empleados.setText(QCoreApplication.translate("MainWindows", u"Ver empleados", None))
        self.label_64.setText(QCoreApplication.translate("MainWindows", u"Nombre", None))
        self.administrador_ver_nombre.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindows", u"Apellido paterno", None))
        self.administrador_ver_apellido_p.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindows", u"Apellido materno", None))
        self.administrador_ver_apellido_m.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindows", u"Salario", None))
        self.label_68.setText(QCoreApplication.translate("MainWindows", u"Usuario", None))
        self.administrador_editar_nombre_usuario.setText("")
        self.label_69.setText(QCoreApplication.translate("MainWindows", u"Correo", None))
        self.administrador_editar_correo.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindows", u"Contrase\u00f1a antigua", None))
        self.administrador_contrasenia_antigua.setText("")
        self.label_71.setText(QCoreApplication.translate("MainWindows", u"Contrase\u00f1a nueva", None))
        self.administrador_cambiar_contrasenia.setText("")
        self.administrador_guardar_cambios.setText(QCoreApplication.translate("MainWindows", u"Guardar Cambios", None))
        self.label_72.setText(QCoreApplication.translate("MainWindows", u"Salario", None))
        self.administrador_agregar_contrasenia.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindows", u"Correo", None))
        self.administrador_agregar_apellido_m.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindows", u"Apellido paterno", None))
        self.administrador_agregar_apellido_p.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindows", u"Apellido materno", None))
        self.label_77.setText(QCoreApplication.translate("MainWindows", u"Usuario", None))
        self.label_78.setText(QCoreApplication.translate("MainWindows", u"Contrase\u00f1a", None))
        self.label_79.setText(QCoreApplication.translate("MainWindows", u"Nombre", None))
        self.administrador_agregar_nombre.setText("")
        self.administrador_agregar_correo.setText("")
        self.administrador_nuevo_empleado_guardar_cambios.setText(QCoreApplication.translate("MainWindows", u"Agregar empleado", None))
        self.administrador_agregar_nombre_usuario.setText("")
        self.administrador_ver_empleado_apellido_p.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindows", u"Apellido materno", None))
        self.administrador_ver_empleado_correo.setText("")
        self.administrador_ver_empleado_apellido_m.setText("")
        self.label_81.setText(QCoreApplication.translate("MainWindows", u"Nombre", None))
        self.label_74.setText(QCoreApplication.translate("MainWindows", u"Correo", None))
        self.label_82.setText(QCoreApplication.translate("MainWindows", u"Salario", None))
        self.label_83.setText(QCoreApplication.translate("MainWindows", u"Usuario", None))
        self.administrador_ver_empleado_nombre.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindows", u"Apellido paterno", None))
        self.administrador_ver_empleado_nombre_usuario.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindows", u"Nombre", None))
        self.empleados_ver_nombre.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindows", u"Apellido paterno", None))
        self.empleados_ver_apellido_p.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindows", u"Apellido materno", None))
        self.empleados_ver_apellido_m.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindows", u"Salario", None))
        self.label_60.setText(QCoreApplication.translate("MainWindows", u"Usuario", None))
        self.empleados_editar_nombre_usuario.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindows", u"Correo", None))
        self.empleados_editar_correo.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindows", u"Contrase\u00f1a antigua", None))
        self.empleados_contrasenia_antigua.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindows", u"Contrase\u00f1a nueva", None))
        self.empleados_cambiar_contrasenia.setText("")
        self.empleados_guardar_cambios.setText(QCoreApplication.translate("MainWindows", u"Guardar Cambios", None))
        self.label_2.setText(QCoreApplication.translate("MainWindows", u"Team Lost Souls", None))
        self.version.setText(QCoreApplication.translate("MainWindows", u"V. 1.5.3", None))
    # retranslateUi

