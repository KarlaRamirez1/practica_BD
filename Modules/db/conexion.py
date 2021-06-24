import sqlite3
import io
from os.path import exists
from PySide6.QtWidgets import QMessageBox

# db = "db/database.db"
db = "db/database.db"

#si no existe una base de datos crearla
# si no existen las tablas crearlas
def conexion():
	conn = sqlite3.connect(db)
	create_database_if_not_exists(conn)
	return conn


def create_database_if_not_exists(conn):
	tables = Tables()
	cursor = conn.cursor()
	cursor.execute(tables.producto())
	cursor.execute(tables.empleado())
	cursor.execute(tables.proveedor())
	cursor.execute(tables.ticket_compra())
	cursor.execute(tables.ticket_venta())
	cursor.execute(tables.compra())
	cursor.execute(tables.venta())

def respaldo():
    msg = QMessageBox()
    conn=sqlite3.connect(db)
    dbcom=sqlite3.connect('db/database_respaldo.db')
    
    try:
        conn.backup(dbcom)
        conn.close()
        dbcom.close()
        msg.setText("se ha creado el respaldo")
        msg.exec_()
    except sqlite3.Error as e:
        msg.setText("se ha producido un error creando el respaldo ", + e.text())
        msg.exec_()
    

def restaurar():
    msg = QMessageBox()
    conn=sqlite3.connect(db)
    bkconn=sqlite3.connect('db/database_respaldo.db')
    try:
        bkconn.backup(conn)
        conn.close()
        bkconn.close()
        msg.setText("se ha restaurado el respaldo")
        msg.exec_()
    except sqlite3.Error as e:
        msg.setText("se ha producido un error cargando el respaldo ", + e.text())
        msg.exec_()
        


class Tables:
	def __init__(self):
		pass

	def producto(self):
		return """
		CREATE TABLE IF NOT EXISTS Producto(
			Id VARCHAR(14),
			Tipo VARCHAR(200),
			Nombre VARCHAR(200),
			Precio DECIMAL(7,2),
			Descripcion VARCHAR(500),
			Existencia INT,
			Resurtible BOOLEAN,
			PRIMARY KEY(Id)
		);
		"""
	
	def empleado(self):
		return """
		CREATE TABLE IF NOT EXISTS Empleado(
			Id INTEGER PRIMARY KEY,
			Nombre VARCHAR(100),
			Apellido_p VARCHAR(100),
			Apellido_m VARCHAR(100),
			Nombre_usuario VARCHAR(100),
			Email VARCHAR(350),
			Contrasenia VARCHAR(21),
			Puesto INT,
			Salario DECIMAL(7,2),
			Activo BOOLEAN DEFAULT TRUE
		);
		"""

	def proveedor(self):
		return """
		CREATE TABLE IF NOT EXISTS Proveedor(
			Id INTEGER PRIMARY KEY,
			Rfc VARCHAR(13),
			Nombre VARCHAR(350),
			Telefono VARCHAR(13),
			direccion VARCHAR(350),
			Activo BOOLEAN DEFAULT TRUE
		);
		"""
	
	def compra(self):
		return """
		CREATE TABLE IF NOT EXISTS Compra(
			Id INTEGER PRIMARY KEY,
			Folio INT,
			Producto INT,
			Cantidad INT,
			FOREIGN KEY(Folio)REFERENCES Ticket_compra(Folio),
			FOREIGN KEY(Producto)REFERENCES Producto(Id)
		);
		"""
	
	def ticket_compra(self):
		return """
		CREATE TABLE IF NOT EXISTS Ticket_compra(
			Folio INTEGER PRIMARY KEY,
			Fecha DATE,
			Id_empleado int,
			Id_proveedor int,
			FOREIGN KEY(Id_empleado)REFERENCES Empleado(Id),
			FOREIGN KEY(Id_proveedor)REFERENCES Proveedor(RFC)
		);
		"""
	
	def venta(self):
		return """
		CREATE TABLE IF NOT EXISTS Venta(
			Id INTEGER PRIMARY KEY,
			Folio INT,
			Producto INT,
			Color VARCHAR(150),
			Cantidad INT,
			FOREIGN KEY(Folio)REFERENCES Ticket_venta(Folio),
			FOREIGN KEY(Producto)REFERENCES Producto(Id)
		);
		"""

	def ticket_venta(self):
		return """
		CREATE TABLE IF NOT EXISTS Ticket_venta(
			Folio INTEGER PRIMARY KEY,
			Fecha DATE,
			Id_empleado int,
			RFC_Cliente VARCHAR(13),
			FOREIGN KEY(Id_empleado)REFERENCES Empleado(Id)
		);
		"""
