#hacer crud a todos las tablas


def read_admin(conn, table, usuario, contrasenia):
	query = "SELECT * FROM {} WHERE Nombre_usuario = '{}' AND contrasenia = '{}'".format(table, usuario, contrasenia)

	cursor = conn.cursor()
	cursor.execute(query)
	
	return cursor.fetchone()


def read_empleados(conn):
	query = "SELECT * FROM EMPLEADO WHERE Puesto = 1"
	cursor = conn.cursor()
	cursor.execute(query)
	return cursor.fetchall()


def read_proveedores(conn):
	query = "SELECT * FROM PROVEEDOR"
	cursor = conn.cursor()
	cursor.execute(query)
	return cursor.fetchall()

def get_categorias(conn):
	query = "SELECT Tipo FROM PRODUCTO "
	cursor = conn.cursor()
	cursor.execute(query)
	return list(dict.fromkeys([row[0] for row in cursor.fetchall()]))

def get_nombres_producto(conn, tipo):
	query = "SELECT * FROM PRODUCTO WHERE Tipo = '{}'".format(tipo)
	cursor = conn.cursor()
	cursor.execute(query)
	return [row[2] for row in cursor.fetchall()]

def get_producto(conn, tipo, nombre):
	query = "SELECT * FROM PRODUCTO WHERE Tipo = '{}' AND Nombre = '{}'".format(tipo, nombre)
	cursor = conn.cursor()
	cursor.execute(query)
	return [row for row in cursor.fetchone()]


def get_count(conn, table):
	return [row[0] for row in conn.execute("SELECT count() FROM {}".format(table))][0]


def create(conn, table, json):
	keys = list_to_string([*json.keys()])
	values = list_to_string([*json.values()], True)

	query = ('INSERT INTO {} ({}) VALUES ({})'.format(table, keys, values))
	print(query)
	conn.execute(query)
	conn.commit()

def update(conn, table, json, where=""):
	query = "UPDATE {} SET ".format(table)
	query += json_to_sql(json)
	query += where

	conn.execute(query)
	conn.commit()


def json_to_sql(json):
	string = ''
	for i, v in enumerate(json):
		if i+1 < len(json):
			string += "{} = '{}', ".format(v, json[v])
		else:
			string += "{} = '{}' ".format(v, json[v])
	return string


def list_to_string(list_convert, is_value=False):
	string = ''
	coma = "'" if is_value else ""
	for i, v in enumerate(list_convert):
		if i+1 < len(list_convert):
			string += "{}{}{}, ".format(coma, v, coma)
		else:
			string += "{}{}{}".format(coma, v, coma)
	return string
