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
import random
import xlwt
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
		
		self.id_producto = 1

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

		this.administrador_guardar_cambios.clicked.connect(self.administrador_update)
		
		this.administrador_agregar_contrasenia.setEchoMode(QLineEdit.Password)
		this.administrador_cambiar_contrasenia.setEchoMode(QLineEdit.Password)
		this.administrador_contrasenia_antigua.setEchoMode(QLineEdit.Password)
		this.empleados_contrasenia_antigua.setEchoMode(QLineEdit.Password)
		this.empleados_cambiar_contrasenia.setEchoMode(QLineEdit.Password)

		this.administrador_nuevo_empleado_guardar_cambios.clicked.connect(self.nuevo_empleado)

		this.empleados_guardar_cambios.clicked.connect(self.empleado_update)

		self.empleados = read_empleados(self.conn)

		this.administrador_buscar_empleado.currentIndexChanged.connect(self.update_ver_empleados)
		this.administrador_buscar_empleado.addItems([row[4] for row in self.empleados])


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

		this.proveedores_editar_guardar.clicked.connect(self.change_editar_proveedores)

		self.categoria_producto = get_categorias(self.conn)

		this.productos_agregar_categoria.addItems(self.categoria_producto)
		this.productos_agregar_guardar.clicked.connect(self.crear_nuevo_producto)
		this.producto_ver_categoria.addItems(self.categoria_producto)
		this.producto_ver_categoria.currentIndexChanged.connect(self.update_ver_nombre_producto)
		this.producto_ver_nombre.currentIndexChanged.connect(self.ver_producto)

		this.productos_agregar_check_nueva_categoria.stateChanged.connect(self.activar_categoria)

		this.productos_editar_categoria.addItems(self.categoria_producto)
		this.productos_editar_categoria.currentIndexChanged.connect(self.update_editar_nombre_producto)
		this.productos_editar_nombre.currentIndexChanged.connect(self.editar_producto)
		this.productos_editar_guardar.clicked.connect(self.update_producto)


		this.compras_proveedor.addItems([row[2] for row in self.proveedores])

		this.btn_closed.clicked.connect(self.close)
		this.btn_maximized.clicked.connect(self.show_windows)
		this.btn_minimized.clicked.connect(self.showMinimized)

		
		this.title.setText("Baños Charly - " + self.login.user[4])


		this.recorte_caja_fecha.setDate(QtCore.QDate.currentDate())
		this.ventas_fecha.setDate(QtCore.QDate.currentDate())
		this.compras_fecha.setDate(QtCore.QDate.currentDate())


		this.compra_categoria_producto_1.addItems(self.categoria_producto)
		this.compra_categoria_producto_1.currentIndexChanged.connect(self.update_nombre_producto_compras)
		this.compra_nombre_producto_1.currentIndexChanged.connect(self.editar_producto_compras)
		# this.productos_editar_guardar.clicked.connect(self.update_producto)

		self.total_productos_compras = []
		this.compra_unidades_1.valueChanged.connect(self.update_precio_total_compra)
		this.compras_agregar.clicked.connect(self.agregar_producto_compra)
		this.compras_generar.clicked.connect(self.comprar_nuevo_producto)
		this.compras_table_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  
		this.compras_table_widget.customContextMenuRequested.connect(self.table_compras) # +++
		this.compras_table_widget.viewport().installEventFilter(self)
		

		this.venta_categoria_producto_1.addItems(self.categoria_producto)
		this.venta_categoria_producto_1.currentIndexChanged.connect(self.update_nombre_producto_ventas)
		this.venta_nombre_producto_1.currentIndexChanged.connect(self.editar_producto_ventas)

		self.total_productos_ventas = []
		this.venta_unidades_1.valueChanged.connect(self.update_precio_total_venta)
		this.ventas_agregar.clicked.connect(self.agregar_producto_venta)
		this.ventas_generar.clicked.connect(self.venta_nuevo_producto)
		this.ventas_table_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  
		this.ventas_table_widget.customContextMenuRequested.connect(self.table_ventas) # +++
		this.ventas_table_widget.viewport().installEventFilter(self)


		this.ventas_table_widget.horizontalHeader().setStretchLastSection(True)
		this.compras_table_widget.horizontalHeader().setStretchLastSection(True)
		this.tickets_table_widget.horizontalHeader().setStretchLastSection(True)
		this.recorte_caja_table_widget.horizontalHeader().setStretchLastSection(True)

		this.Tickets_generar_ticket.clicked.connect(self.crear_ticket_xlsx)
		this.recorte_caja_generar_ticket.clicked.connect(self.crear_corte_caja_xlsx)
		self.corte_caja = []
		self.tickets = []



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
		self.animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
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
			self.update_tickets()
		elif btn_name == "proveedores":
			select(this.page_proveedores)
		elif btn_name == "recorte_caja":
			select(this.page_recorte_caja)
			self.update_corte_caja()
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

	def administrador_update(self):
		update_admin = { 
			"Nombre" : this.administrador_ver_nombre.text(),
			"Apellido_p": this.administrador_ver_apellido_p.text(),
			"Apellido_m": this.administrador_ver_apellido_m.text(),
			"Nombre_usuario": this.administrador_editar_nombre_usuario.text(),
			"Email": this.administrador_editar_correo.text()
		}
		passw = self.login.user[6]
		if this.administrador_contrasenia_antigua.text() == '' and this.administrador_cambiar_contrasenia.text() != '':
			QMessageBox.about(self, "Error", "Debes colocar tu contraseña antigua")
			return
		
			
		if this.administrador_contrasenia_antigua.text() != '':
			if this.administrador_contrasenia_antigua.text() != self.login.user[6]:
				QMessageBox.about(self, "Error", "La contraseña es incorrecta")
				return
			if this.administrador_cambiar_contrasenia.text() == '':
				QMessageBox.about(self, "Error", "Tu nueva contraseña no puede estar vacia")
				return
			update_admin['Contrasenia'] = this.administrador_cambiar_contrasenia.text()
			passw = this.administrador_cambiar_contrasenia.text()
			this.administrador_contrasenia_antigua.setText('')
			# self.login.user[6] = this.administrador_cambiar_contrasenia.text()
			this.administrador_cambiar_contrasenia.setText('')

		update(self.conn, 'Empleado', update_admin, "WHERE nombre_usuario = '{}'".format(self.login.user[4]))
		
		self.login.user = read_admin(self.conn, "Empleado", this.administrador_editar_nombre_usuario.text(), passw)
		QMessageBox.about(self, "Exito", "Los datos se guardaron con exito")

	def empleado_update(self):
		update_admin = { 
			"Nombre" : this.empleados_ver_nombre.text(),
			"Apellido_p": this.empleados_ver_apellido_p.text(),
			"Apellido_m": this.empleados_ver_apellido_m.text(),
			"Nombre_usuario": this.empleados_editar_nombre_usuario.text(),
			"Email": this.empleados_editar_correo.text()
		}
		passw = self.login.user[6]
		if this.empleados_contrasenia_antigua.text() == '' and this.empleados_cambiar_contrasenia.text() != '':
			QMessageBox.about(self, "Error", "Debes colocar tu contraseña antigua")
			return

		if this.empleados_contrasenia_antigua.text() != '':
			if this.empleados_contrasenia_antigua.text() != self.login.user[6]:
				QMessageBox.about(self, "Error", "La contraseña es incorrecta")
				return
			if this.empleados_cambiar_contrasenia.text() == '':
				QMessageBox.about(self, "Error", "Tu nueva contraseña no puede estar vacia")
				return
			update_admin['Contrasenia'] = this.empleados_cambiar_contrasenia.text()
			passw = this.empleados_cambiar_contrasenia.text()
			this.empleados_contrasenia_antigua.setText('')
			this.empleados_cambiar_contrasenia.setText('')

		update(self.conn, 'Empleado', update_admin, "WHERE nombre_usuario = '{}'".format(self.login.user[4]))
		self.login.user = read_admin(self.conn, "Empleado", this.empleados_editar_nombre_usuario.text(), passw)
		QMessageBox.about(self, "Exito", "Los datos se guardaron con exito")

	def update_ver_nombre_producto(self):
		productos = get_nombres_producto(self.conn, this.producto_ver_categoria.currentText())	
		this.producto_ver_nombre.clear()
		this.producto_ver_nombre.addItems(productos)

	def update_editar_nombre_producto(self):
		productos = get_nombres_producto(self.conn, this.productos_editar_categoria.currentText())	
		this.productos_editar_nombre.clear()
		this.productos_editar_nombre.addItems(productos)

	def ver_producto(self):
		producto = get_producto(self.conn, this.producto_ver_categoria.currentText(), this.producto_ver_nombre.currentText())
		this.productos_ver_precio.setValue(producto[3])
		this.productos_ver_existencia.setValue(producto[5])
		this.productos_ver_descripcion.setPlainText(producto[4])
		this.productos_ver_resurtible.setChecked( True if producto[6] == "TRUE" else False)
		
	def editar_producto(self):
		producto = get_producto(self.conn, this.productos_editar_categoria.currentText(), this.productos_editar_nombre.currentText())

		this.productos_editar_nuevo_nombre.setText(producto[2])
		this.productos_editar_precio.setValue(producto[3])
		this.productos_editar_existencia.setValue(producto[5])
		this.productos_editar_descripcion.setPlainText(producto[4])
		this.productos_editar_resurtible.setChecked( True if producto[6] == "TRUE" else False)
		
	def update_producto(self):
		update_producto = {
			"Nombre": this.productos_editar_nuevo_nombre.text(),
			"Precio": this.productos_editar_precio.value(),
			"Descripcion": this.productos_editar_descripcion.toPlainText(),
			"Existencia": this.productos_editar_existencia.value(),
			"Resurtible": "TRUE" if this.productos_editar_resurtible.isChecked() else "FALSE"
		}

		update(self.conn, "Producto", update_producto, "WHERE Tipo = '{}' AND Nombre = '{}'".format(this.productos_editar_categoria.currentText(), this.productos_editar_nombre.currentText()))
		
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
		
		this.proveedores_editar_nombre.clear()
		this.proveedores_editar_nombre.addItems([row[2] for row in self.proveedores])
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

	def change_editar_proveedores(self):
		check = "TRUE" if this.proveedores_editar_check_activo.isChecked() else "FALSE"
		update_proveedor = {
			"Rfc": this.proveedores_editar_rfc.text(),
			"Nombre": this.proveedores_editar_editar_nombre.text(),
			"Telefono": this.proveedores_editar_telefono.text(),
			"Direccion": this.proveedores_editar_direccion.text(),
			"Activo": check
		}
		
		update(self.conn, 'Proveedor', update_proveedor, "WHERE iD = '{}'".format(this.proveedores_editar_nombre.currentIndex()+1))
		
		self.proveedores = read_proveedores(self.conn)
		this.proveedores_ver_proveedor.clear()
		this.proveedores_ver_proveedor.addItems([row[2] for row in self.proveedores])
		this.proveedores_editar_nombre.clear()
		this.proveedores_editar_nombre.addItems([row[2] for row in self.proveedores])

		QMessageBox.about(self, "Exito", "Los datos se guardaron con exito")
				
	def crear_nuevo_producto(self):
		nuevo_producto = {
			"Id": this.productos_agregar_categoria.currentText()[0:2] + "-" + this.productos_agregar_nombre.text()[0:2] + "-" + str(random.randrange(1,9999)),
			"Tipo": this.productos_agregar_categoria.currentText(),
			"Precio": this.productos_agregar_precio.value(),
			"Existencia": this.productos_agregar_existencia.text(),
			"Resurtible": "TRUE" if this.productos_agregar_resurtible.isChecked() else "FALSE",
			"Nombre": this.productos_agregar_nombre.text(),
			"Descripcion": this.productos_agregar_descripcion.toPlainText(),
		}
		if this.productos_agregar_check_nueva_categoria.isChecked():
			nuevo_producto["Tipo"] = this.productos_agregar_nueva_categoria.text()

		create(self.conn, "Producto", nuevo_producto)
		self.categoria_producto = get_categorias(self.conn)
		this.productos_agregar_categoria.clear()
		this.productos_agregar_categoria.addItems(self.categoria_producto)
		this.producto_ver_categoria.clear()
		this.producto_ver_categoria.addItems(self.categoria_producto)
		
		QMessageBox.about(self, "Exito", "Los datos se guardaron con exito")
		
	def activar_categoria(self):
		if this.productos_agregar_check_nueva_categoria.isChecked():
			this.productos_agregar_nueva_categoria.setEnabled(True)
			this.productos_agregar_nueva_categoria.setStyleSheet("color: #fff;")
			this.productos_agregar_categoria.setEnabled(False)
			this.productos_agregar_categoria.setStyleSheet("color: #aaa;")
		else:
			this.productos_agregar_nueva_categoria.setEnabled(False)
			this.productos_agregar_nueva_categoria.setStyleSheet("color: #aaa;")
			this.productos_agregar_categoria.setEnabled(True)
			this.productos_agregar_categoria.setStyleSheet("color: #fff;")
			

	def update_nombre_producto_compras(self):
		productos = get_nombres_producto(self.conn, this.compra_categoria_producto_1.currentText())	
		this.compra_nombre_producto_1.clear()
		this.compra_nombre_producto_1.addItems(productos)
		
	def editar_producto_compras(self):
		producto = get_producto(self.conn, this.compra_categoria_producto_1.currentText(), this.compra_nombre_producto_1.currentText())
		this.compra_precio_1.setValue(producto[3])
		self.update_precio_total_venta()

	def update_precio_total_compra(self):
		this.compra_total_1.setValue(this.compra_precio_1.value() * this.compra_unidades_1.value())

	def agregar_producto_compra(self):
		get_producto = {
			"Categoria" : this.compra_categoria_producto_1.currentText(),
			"Nombre": this.compra_nombre_producto_1.currentText(),
			"Precio": this.compra_precio_1.value(),
			"Unidades": this.compra_unidades_1.value(),
			"Total": this.compra_total_1.value()
		}
		for key in get_producto:
			if get_producto[key] == '' or get_producto[key] == 0:
				QMessageBox.about(self, "Error", "No pueden haber campos vacios")
				return
		
		self.total_productos_compras.append(get_producto)

		this.compra_unidades_1.setValue(0)
		this.compra_total_1.setValue(0)
		#actualizar la tabla
		self.table_compras()

	def table_compras(self):
		this.compras_table_widget.setRowCount(len(self.total_productos_compras))

		for column, row in enumerate(self.total_productos_compras):
			this.compras_table_widget.setItem(column, 0, QTableWidgetItem(row["Categoria"]))
			this.compras_table_widget.setItem(column, 1, QTableWidgetItem(row["Nombre"]))
			this.compras_table_widget.setItem(column, 2, QTableWidgetItem(str(row["Precio"])))
			this.compras_table_widget.setItem(column, 3, QTableWidgetItem(str(row["Unidades"])))
			this.compras_table_widget.setItem(column, 4, QTableWidgetItem(str(row["Total"])))

	def comprar_nuevo_producto(self):
		if len(self.total_productos_compras) == 0:
			QMessageBox.about(self, "Error", "No hay nada que comprar")
			return
		# generar un folio
		folio = {
			"Fecha": QtCore.QDate.currentDate().toString('yyyy/MM/dd'),
			"Id_empleado": self.login.user[0],
			"Id_proveedor": this.compras_proveedor.currentIndex()
		}
		id_folio = create(self.conn, "Ticket_compra", folio)
		# comenzar a generar las compras

		for row in self.total_productos_compras:
			id_producto = get_producto(self.conn, row["Categoria"], row["Nombre"])[0]
			compra = {
				"Folio": id_folio,
				"Producto" : id_producto,
				"Cantidad": row["Unidades"]
			}
			create(self.conn, "Compra", compra)
		QMessageBox.about(self, "Exito", "La compra se genero con exito")
		self.total_productos_compras = []
		self.table_compras()


	def update_nombre_producto_ventas(self):
		productos = get_nombres_producto(self.conn, this.venta_categoria_producto_1.currentText())	
		this.venta_nombre_producto_1.clear()
		this.venta_nombre_producto_1.addItems(productos)

	def editar_producto_ventas(self):
		producto = get_producto(self.conn, this.venta_categoria_producto_1.currentText(), this.venta_nombre_producto_1.currentText())
		this.venta_precio_1.setValue(producto[3])
		self.update_precio_total_venta()

	def update_precio_total_venta(self):
		this.venta_total_1.setValue(this.venta_precio_1.value() * this.venta_unidades_1.value())

	def agregar_producto_venta(self):
		get_producto = {
			"Categoria" : this.venta_categoria_producto_1.currentText(),
			"Nombre": this.venta_nombre_producto_1.currentText(),
			"Precio": this.venta_precio_1.value(),
			"Unidades": this.venta_unidades_1.value(),
			"Color": this.venta_color_1.text(),
			"Total": this.venta_total_1.value()
		}
		for key in get_producto:
			if get_producto[key] == '' or get_producto[key] == 0:
				QMessageBox.about(self, "Error", "No pueden haber campos vacios")
				return
		
		self.total_productos_ventas.append(get_producto)

		this.venta_unidades_1.setValue(0)
		this.venta_color_1.setText("")
		this.venta_total_1.setValue(0)
		#actualizar la tabla
		self.table_ventas()

	def table_ventas(self):
		this.ventas_table_widget.setRowCount(len(self.total_productos_ventas))

		for column, row in enumerate(self.total_productos_ventas):
			this.ventas_table_widget.setItem(column, 0, QTableWidgetItem(row["Categoria"]))
			this.ventas_table_widget.setItem(column, 1, QTableWidgetItem(row["Nombre"]))
			this.ventas_table_widget.setItem(column, 2, QTableWidgetItem(str(row["Precio"])))
			this.ventas_table_widget.setItem(column, 3, QTableWidgetItem(str(row["Unidades"])))
			this.ventas_table_widget.setItem(column, 4, QTableWidgetItem(row["Color"]))
			this.ventas_table_widget.setItem(column, 5, QTableWidgetItem(str(row["Total"])))

	def venta_nuevo_producto(self):
		if len(self.total_productos_ventas) == 0:
			QMessageBox.about(self, "Error", "No hay nada que vender")
			return
		# generar un folio
		folio = {
			"Fecha": QtCore.QDate.currentDate().toString('yyyy/MM/dd'),
			"Id_empleado": self.login.user[0],
			"RFC_Cliente": this.ventas_rfc_cliente.text()
		}
		id_folio = create(self.conn, "Ticket_venta", folio)
		# comenzar a generar las ventaas

		for row in self.total_productos_ventas:
			id_producto = get_producto(self.conn, row["Categoria"], row["Nombre"])[0]
			venta = {
				"Folio": id_folio,
				"Producto" : id_producto,
				"Color": row["Color"],
				"Cantidad": row["Unidades"]
			}
			create(self.conn, "Venta", venta)
		QMessageBox.about(self, "Exito", "La venta se genero con exito")
		self.total_productos_ventas = []
		this.ventas_rfc_cliente.setText("")
		self.table_ventas()




	def update_corte_caja(self):
		#obtener ventas
		total_ventas_hoy = get_ventas_hoy(self.conn, QtCore.QDate.currentDate().toString('yyyy/MM/dd'))
		#obtener precio por venta
		
		tickets = []

		for venta in total_ventas_hoy:
			total = 0
			for ticket in venta:
				id = ticket[2]
				producto = get_producto_by_id(self.conn, id)

				folio = ticket[1]
				unidades = ticket[4]
				precio = producto[3]
				subtotal = unidades * precio
				total += subtotal

			#Folio, fecha, total
			tickets.append({
				"Folio": folio,
				"Fecha": QtCore.QDate.currentDate().toString('yyyy/MM/dd'),
				"Total": total
			})

		self.corte_caja = tickets
		this.recorte_caja_table_widget.setRowCount(len(tickets))
		for column, ticket in enumerate(tickets):
			this.recorte_caja_table_widget.setItem(column, 0, QTableWidgetItem(str(ticket["Folio"])))
			this.recorte_caja_table_widget.setItem(column, 1, QTableWidgetItem(ticket["Fecha"]))
			this.recorte_caja_table_widget.setItem(column, 2, QTableWidgetItem(str(ticket["Total"])))






	def update_tickets(self):
		#obtener ventas
		total_ventas_hoy = get_ventas_hoy(self.conn, QtCore.QDate.currentDate().toString('yyyy/MM/dd'))
		#obtener precio por venta
		
		tickets = []

		for venta in total_ventas_hoy:
			total = 0
			for ticket in venta:
				id = ticket[2]
				producto = get_producto_by_id(self.conn, id)
				folio = ticket[1]
				color = ticket[3]
				unidades = ticket[4]

				datos_ticket = get_ticket(self.conn, folio)
				fecha = datos_ticket[1]
				empleado = get_empleado_by_id(self.conn, datos_ticket[2])[0]
				rfc = datos_ticket[3]
				categoria = producto[1]
				nombre = producto[2]
				categoria = producto[1]
				precio = producto[3]
				subtotal = unidades * precio

				total += subtotal
				t = {
					"Folio": folio,
					"Fecha": fecha,
					"Categoria": categoria,
					"Nombre": nombre,
					"Precio": precio,
					"Unidades": unidades,
					"Total": subtotal,
					"Color": color,
					"Empleado": empleado,
					"RFC": rfc
				}
				tickets.append(t)
			#Folio, fecha, Categoria, Nombre, Precio, Unidades, Total, Color, Empleado, RFC
			tickets.append({
				"Folio": folio,
				"Fecha": "",
				"Categoria": "",
				"Nombre": "",
				"Precio": "",
				"Unidades": "",
				"Total": total,
				"Color": "",
				"Empleado": "",
				"RFC": ""
			})

		self.tickets = tickets
		
		this.tickets_table_widget.setRowCount(len(tickets))
		for column, ticket in enumerate(tickets):
			this.tickets_table_widget.setItem(column, 0, QTableWidgetItem(str(ticket["Folio"])))
			this.tickets_table_widget.setItem(column, 1, QTableWidgetItem(ticket["Fecha"]))
			this.tickets_table_widget.setItem(column, 2, QTableWidgetItem(str(ticket["Categoria"])))
			this.tickets_table_widget.setItem(column, 3, QTableWidgetItem(str(ticket["Nombre"])))
			this.tickets_table_widget.setItem(column, 4, QTableWidgetItem(str(ticket["Precio"])))
			this.tickets_table_widget.setItem(column, 5, QTableWidgetItem(str(ticket["Unidades"])))
			this.tickets_table_widget.setItem(column, 6, QTableWidgetItem(str(ticket["Total"])))
			this.tickets_table_widget.setItem(column, 7, QTableWidgetItem(str(ticket["Color"])))
			this.tickets_table_widget.setItem(column, 8, QTableWidgetItem(str(ticket["Empleado"])))
			this.tickets_table_widget.setItem(column, 9, QTableWidgetItem(str(ticket["RFC"])))





	def crear_ticket_xlsx(self):
		#generar archivo .xls
		padre = os.environ['HOMEPATH']
		directory = QFileDialog.getSaveFileName(self, "Seleccione destino", padre,"Archivo de Excel (*.xls)")

		if directory[0] == '':
			QMessageBox.about(self,"Error","No se ha podido guardar el archivo ")
			return

		data = []
		data.insert(0, ["Folio", "Fecha", "Categoria", "Nombre", "Precio", "Unidades", "Total", "Color", "Empleado", "RFC"])# header
		#convertir dict a list
		for i in self.tickets:
			data.append(list(i.values()))
		
		workbook = xlwt.Workbook()
		sheet = workbook.add_sheet('tickets')
		
		for x, row in enumerate(data):
			for y, value in enumerate(row):
				sheet.write(x, y, value)
		
		workbook.save(directory[0])
		
		QMessageBox.about(self,"Finalizado con existo","el archivo se ha guardado con exito.")


	def crear_corte_caja_xlsx(self):
		#generar archivo .xls
		padre = os.environ['HOMEPATH']
		directory = QFileDialog.getSaveFileName(self, "Seleccione destino", padre,"Archivo de Excel (*.xls)")

		if directory[0] == '':
			QMessageBox.about(self,"Error","No se ha podido guardar el archivo ")
			return

		data = []
		data.insert(0, ["Folio", "Fecha", "Total"])# header
		#convertir dict a list
		for i in self.corte_caja:
			data.append(list(i.values()))
		
		workbook = xlwt.Workbook()
		sheet = workbook.add_sheet('tickets')
		
		for x, row in enumerate(data):
			for y, value in enumerate(row):
				sheet.write(x, y, value)
		
		workbook.save(directory[0])
		
		QMessageBox.about(self,"Finalizado con existo","el archivo se ha guardado con exito.")

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