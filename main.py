import sys
from PySide6.QtWidgets import *
from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from modules.login import Login
from modules.main_ui import Ui_MainWindows
from modules.db.conexion import conexion
from modules.db.crud import *


import os
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		self.ui = Ui_MainWindows()
		self.ui.setupUi(self)

		global this
		this = self.ui

		self.windows_maximized = False
		
		flags = QtCore.Qt.WindowFlags(QtCore.Qt.Dialog)
		self.setWindowFlags(flags|QtCore.Qt.FramelessWindowHint |QtCore.Qt.CustomizeWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)#fondo de la ventana transparente

		self.conn = conexion()# creo una conexion a la base de datos

		self.login = Login(self.conn)
		self.login.exec_()
		if self.login.cancel:
			sys.exit(self)

		self.init()

		this.btn_toggle.clicked.connect(self.toggle_menu)
		this.lbl_toggle.clicked.connect(self.toggle_menu)


		this.btn_ventas.clicked.connect(self.menu)
		this.lbl_ventas.clicked.connect(self.menu)
		this.btn_compras.clicked.connect(self.menu)
		this.lbl_compras.clicked.connect(self.menu)
		this.btn_productos.clicked.connect(self.menu)
		this.lbl_productos.clicked.connect(self.menu)
		this.btn_proveedores.clicked.connect(self.menu)
		this.lbl_proveedores.clicked.connect(self.menu)
		this.btn_tickets.clicked.connect(self.menu)
		this.lbl_tickets.clicked.connect(self.menu)
		this.btn_recorte_caja.clicked.connect(self.menu)
		this.lbl_recorte_caja.clicked.connect(self.menu)
		this.btn_copia_seguridad.clicked.connect(self.menu)
		this.lbl_copia_seguridad.clicked.connect(self.menu)
		this.btn_usuario.clicked.connect(self.menu)


		this.administrador_ver_tados.clicked.connect(lambda: this.administrador_stacked.setCurrentWidget(this.datos_personales))
		this.administrador_ver_empleados.clicked.connect(lambda: this.administrador_stacked.setCurrentWidget(this.ver_empleados))
		this.administrador_agregar_empleado.clicked.connect(lambda: this.administrador_stacked.setCurrentWidget(this.agregar_empleado))
		
		this.administrador_agregar_contrasenia.setEchoMode(QLineEdit.Password)

		this.administrador_nuevo_empleado_guardar_cambios.clicked.connect(self.nuevo_empleado)

		self.empleados = read_empleados(self.conn)

		this.administrador_buscar_empleado.currentIndexChanged.connect(self.update_ver_empleados)
		this.administrador_buscar_empleado.addItems([row[4] for row in self.empleados])

        # self.comboBox_employees.clear()
        # self.comboBox_employees.setCurrentIndex(idx)


		this.proveedores_ver.clicked.connect(lambda: this.proveedores_stacked.setCurrentWidget(this.page_proveedores_ver))
		this.proveedores_agregar.clicked.connect(lambda: this.proveedores_stacked.setCurrentWidget(this.page_proveedores_agregar))
		this.proveedores_editar.clicked.connect(lambda: this.proveedores_stacked.setCurrentWidget(this.page_proveedores_editar))

		this.productos_ver.clicked.connect(lambda: this.productos_stacked.setCurrentWidget(this.page_productos_ver))
		this.productos_agregar.clicked.connect(lambda: this.productos_stacked.setCurrentWidget(this.page_productos_agregar))
		this.productos_editar.clicked.connect(lambda: this.productos_stacked.setCurrentWidget(this.page_productos_editar))

		this.proveedores_agregar_guardar.clicked.connect(self.guardar_nuevo_proveedor)
		self.proveedores = read_proveedores(self.conn)

		this.proveedores_ver_proveedor.currentIndexChanged.connect(self.update_ver_proveedores)
		this.proveedores_ver_proveedor.addItems([row[2] for row in self.proveedores])
		this.proveedores_editar_nombre.currentIndexChanged.connect(self.update_editar_proveedores)
		this.proveedores_editar_nombre.addItems([row[2] for row in self.proveedores])

		this.productos_agregar_guardar.clicked.connect(self.crear_nuevo_producto)

		this.compras_proveedor.addItems([row[2] for row in self.proveedores])

		this.compras_agregar.clicked.connect(self.comprar_nuevo_producto)
		self.compras_totales = 1
		# this.proveedores_editar_guardar.clicked.connect()

		this.btn_closed.clicked.connect(self.close)
		this.btn_maximized.clicked.connect(self.show_windows)
		this.btn_minimized.clicked.connect(self.showMinimized)

		
		this.title.setText("Baños Charly - " + self.login.user[4])


	def init(self):
		#verificar si es admin o empleado
		if self.login.user[7] == 0:
			this.administrador_ver_nombre.setText(self.login.user[1])
			this.administrador_ver_apellido_p.setText(self.login.user[2])
			this.administrador_ver_apellido_m.setText(self.login.user[3])
			this.administrador_ver_salario.setValue(self.login.user[8])
			this.administrador_editar_nombre_usuario.setText(self.login.user[4])
			this.administrador_editar_correo.setText(self.login.user[5])
		else:
			this.empleados_ver_nombre.setText(self.login.user[1])
			this.empleados_ver_apellido_p.setText(self.login.user[2])
			this.empleados_ver_apellido_m.setText(self.login.user[3])
			this.empleados_ver_salario.setValue(self.login.user[8])
			this.empleados_editar_nombre_usuario.setText(self.login.user[4])
			this.empleados_editar_correo.setText(self.login.user[5])

	def toggle_menu(self):
		begin_width = this.side_bar.width()
		end_width = 200 if this.side_bar.width() == 45 else 45

		size_animation = b"maximumWidth" if this.side_bar.width() == 45 else b"minimumWidth"
		this.side_bar.setMaximumSize(end_width, this.side_bar.height())

		# ANIMATION
		self.animation = QtCore.QPropertyAnimation(this.side_bar, size_animation)
		self.animation.setDuration(1000)
		self.animation.setStartValue(begin_width)
		self.animation.setEndValue(end_width)
		self.animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
		# InOutQuart
		# InOutCubic
		# OutBounce 
		self.animation.start()
			
	def show_windows(self):
		if self.windows_maximized:
			self.showNormal()
		else:
			self.showMaximized()
		self.windows_maximized = not self.windows_maximized
	
	def menu(self):
		btn_name = self.sender().objectName()
		
		btn_name = btn_name.split("btn_")[1] if "btn" in btn_name else btn_name.split("lbl_")[1]

		select = this.stackedWidget.setCurrentWidget
		
		if btn_name == "ventas":
			select(this.page_ventas)
		elif btn_name == "compras":
			select(this.page_compras)
		elif btn_name == "productos":
			select(this.page_productos)
		elif btn_name == "tickets":
			select(this.page_tickets)
		elif btn_name == "proveedores":
			select(this.page_proveedores)
		elif btn_name == "recorte_caja":
			select(this.page_recorte_caja)
		elif btn_name == "copia_seguridad":
			select(this.page_copia_seguridad)
		elif btn_name == "usuario":
			if self.login.user[7] == 0: #admin
				select(this.page_admin)
			else:
				select(this.page_empleado)
				
		this.title.setText("Baños Charly - " + self.login.user[4] + " - " + btn_name.replace("_", " de "))

	def nuevo_empleado(self):
		nuevo_empleado = { 
			"Nombre" : this.administrador_agregar_nombre.text(),
			"Apellido_p": this.administrador_agregar_apellido_p.text(),
			"Apellido_m": this.administrador_agregar_apellido_m.text(),
			"Nombre_usuario": this.administrador_agregar_nombre_usuario.text(),
			"Email": this.administrador_agregar_correo.text(),
			"contrasenia": this.administrador_agregar_contrasenia.text(),
			"Puesto": 1,
			"Salario": this.administrador_agregar_salario.value()
		}

		create(self.conn, "Empleado", nuevo_empleado)

		this.administrador_agregar_nombre.setText("")
		this.administrador_agregar_apellido_p.setText("")
		this.administrador_agregar_apellido_m.setText("")
		this.administrador_agregar_nombre_usuario.setText("")
		this.administrador_agregar_correo.setText("")
		this.administrador_agregar_contrasenia.setText("")
		this.administrador_agregar_salario.setValue(0)

		self.empleados = read_empleados(self.conn)
		this.administrador_buscar_empleado.clear()
		this.administrador_buscar_empleado.addItems([row[4] for row in self.empleados])
		QMessageBox.about(self, "Exito", "Los datos se guardaron con exito")
		
	def update_ver_empleados(self):
		empleado = self.empleados[this.administrador_buscar_empleado.currentIndex()]
		this.administrador_ver_empleado_nombre.setText(empleado[1])
		this.administrador_ver_empleado_apellido_p.setText(empleado[2])
		this.administrador_ver_empleado_apellido_m.setText(empleado[3])
		this.administrador_ver_empleado_salario.setValue(empleado[8])
		this.administrador_ver_empleado_nombre_usuario.setText(empleado[4])
		this.administrador_ver_empleado_correo.setText(empleado[5])


	def guardar_nuevo_proveedor(self):
		nuevo_proveedor = {
			"Rfc": this.proveedor_agregar_rfc.text(),
			"Nombre": this.proveedor_agregar_nombre.text(),
			"Telefono": this.proveedor_agregar_telefono.text(),
			"Direccion": this.proveedor_agregar_direccion.text()
		}

		create(self.conn, "Proveedor", nuevo_proveedor)
		
		this.proveedor_agregar_rfc.setText(""),
		this.proveedor_agregar_nombre.setText(""),
		this.proveedor_agregar_telefono.setText(""),
		this.proveedor_agregar_direccion.setText("")
		
		self.proveedores = read_proveedores(self.conn)
		this.proveedores_ver_proveedor.clear()
		this.proveedores_ver_proveedor.addItems([row[2] for row in self.proveedores])
		QMessageBox.about(self, "Exito", "Los datos se guardaron con exito")
		
		
	def update_ver_proveedores(self):
		proveedor = self.proveedores[this.proveedores_ver_proveedor.currentIndex()]
		this.proveedores_ver_rfc.setText(proveedor[1])
		this.proveedores_ver_telefono.setText(proveedor[3])
		this.proveedores_ver_direccion.setText(proveedor[4])
		check = True if proveedor[5] == "TRUE" else False
		this.productos_ver_check_activo.setChecked(check)#esta activo

	def update_editar_proveedores(self):
		proveedor = self.proveedores[this.proveedores_editar_nombre.currentIndex()]
		this.proveedores_editar_rfc.setText(proveedor[1])
		this.proveedores_editar_telefono.setText(proveedor[3])
		this.proveedores_editar_direccion.setText(proveedor[4])
		check = True if proveedor[5] == "TRUE" else False
		this.proveedores_editar_check_activo.setChecked(check)
		this.proveedores_editar_editar_nombre.setText(proveedor[2])

	def crear_nuevo_producto(self):
		nuevo_producto = {
			"Tipo": this.productos_agregar_nueva_categoria.text(),
			"Precio": this.productos_agregar_precio.value(),
			"Existencia": this.productos_agregar_existencia.text(),
			"Resurtible": this.productos_agregar_resurtible.isChecked(),
			"Nombre": this.productos_agregar_nombre.text(),
			"Descripcion": this.productos_agregar_descripcion.toPlainText(),
		}

		
		create(self.conn, "Producto", nuevo_producto)
		QMessageBox.about(self, "Exito", "Los datos se guardaron con exito")
		


	def comprar_nuevo_producto(self):	
		self.box_compra_2 = QFrame(this.compras_scrolling)
		self.box_compra_2.setObjectName(u"box_compra_2")
		self.box_compra_2.setGeometry(QRect(0, 70, 880, 35))
		self.box_compra_2.setStyleSheet(u"background: red;")
		self.box_compra_2.setFrameShape(QFrame.StyledPanel)
		self.box_compra_2.setFrameShadow(QFrame.Raised)

		self.box_compra_1 = QFrame(this.compras_scrolling)
		self.box_compra_1.setObjectName(u"box_compra_" + str(self.compras_totales+1))
		self.box_compra_1.setGeometry(QRect(0, self.compras_totales*35+50 , 880, 35))
		self.box_compra_1.setFrameShape(QFrame.StyledPanel)
		self.box_compra_1.setFrameShadow(QFrame.Raised)
		self.box_compra_1.setStyleSheet("background: red;")
		self.compra_precio_1 = QDoubleSpinBox(self.box_compra_1)
		self.compra_precio_1.setObjectName(u"compra_precio_" + str(self.compras_totales+1))
		self.compra_precio_1.setEnabled(False)
		self.compra_precio_1.setGeometry(QRect(470, 5, 62, 22))
		self.compra_total_1 = QDoubleSpinBox(self.box_compra_1)
		self.compra_total_1.setObjectName(u"compra_total_" + str(self.compras_totales+1))
		self.compra_total_1.setEnabled(False)
		self.compra_total_1.setGeometry(QRect(740, 5, 75, 22))
		self.compra_unidades_1 = QSpinBox(self.box_compra_1)
		self.compra_unidades_1.setObjectName(u"compra_unidades_" + str(self.compras_totales+1))
		self.compra_unidades_1.setGeometry(QRect(520, 5, 42, 22))
		self.compra_remove_1 = QPushButton(self.box_compra_1)
		self.compra_remove_1.setObjectName(u"compra_remove_" + str(self.compras_totales+1))
		self.compra_remove_1.setGeometry(QRect(840, 0, 35, 35))
		self.compra_remove_1.setCursor(QCursor(Qt.PointingHandCursor))
		self.line_35 = QFrame(self.box_compra_1)
		self.line_35.setObjectName(u"line_35_" + str(self.compras_totales+1))
		self.line_35.setGeometry(QRect(740, 30, 75, 2))
		self.line_35.setFrameShape(QFrame.HLine)
		self.line_35.setFrameShadow(QFrame.Sunken)
		self.compra_categoria_producto_1 = QComboBox(self.box_compra_1)
		self.compra_categoria_producto_1.setObjectName(u"compra_categoria_producto_" + str(self.compras_totales+1))
		self.compra_categoria_producto_1.setGeometry(QRect(0, 0, 200, 35))
		self.compra_categoria_producto_1.setCursor(QCursor(Qt.PointingHandCursor))
		self.compra_nombre_producto_1 = QComboBox(self.box_compra_1)
		self.compra_nombre_producto_1.setObjectName(u"compra_nombre_producto_" + str(self.compras_totales+1))
		self.compra_nombre_producto_1.setGeometry(QRect(220, 0, 200, 35))
		self.compra_nombre_producto_1.setCursor(QCursor(Qt.PointingHandCursor))
		self.line_36 = QFrame(self.box_compra_1)
		self.line_36.setObjectName(u"line_36_" + str(self.compras_totales+1))
		self.line_36.setGeometry(QRect(520, 30, 90, 2))
		self.line_36.setFrameShape(QFrame.HLine)
		self.line_36.setFrameShadow(QFrame.Sunken)
		self.line_37 = QFrame(self.box_compra_1)
		self.line_37.setObjectName(u"line_37_" + str(self.compras_totales+1))
		self.line_37.setGeometry(QRect(440, 30, 60, 2))
		self.line_37.setFrameShape(QFrame.HLine)
		self.line_37.setFrameShadow(QFrame.Sunken)
		self.line_38 = QFrame(self.box_compra_1)
		self.line_38.setObjectName(u"line_38_" + str(self.compras_totales+1))
		self.line_38.setGeometry(QRect(620, 30, 100, 2))
		self.line_38.setFrameShape(QFrame.HLine)
		self.line_38.setFrameShadow(QFrame.Sunken)
		self.compra_color_1 = QLineEdit(self.box_compra_1)
		self.compra_color_1.setObjectName(u"compra_color_" + str(self.compras_totales+1))
		self.compra_color_1.setGeometry(QRect(620, 5, 100, 22))

		self.compras_totales += 1
		print(self.box_compra_1.size())
		print(self.compras_totales)

	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			try:
				self.old_pos_active = True
				self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
				event.accept()
			except Exception as e:
				pass

	def mouseMoveEvent(self, event):
		if event.buttons() == QtCore.Qt.LeftButton and self.old_pos_active:
			try:
				self.move(event.globalPos() - self.dragPosition)
				event.accept()
			except Exception as e:
				pass

	def mouseReleaseEvent(self, event):
		self.old_pos_active = False

	
	def closeEvent(self, event):
		self.conn.close()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

	# pyside6-uic main.ui > main_ui.py
	# pyside6-rcc resources.qrc -o resources_rc.py