


#hacer crud a todos las tablas

def read_admin(conn, table, usuario, contrasenia):
	query = "SELECT * FROM {} WHERE Nombre_usuario = '{}' AND contrasenia = '{}'".format(table, usuario, contrasenia)

	cursor = conn.cursor()
	cursor.execute(query)
	
	return cursor.fetchone()





def get_count(conn, table):
	return [row[0] for row in conn.execute("SELECT count() FROM {}".format(table))][0]


def create(conn, table, json):
	keys = list_to_string([*json.keys()])
	values = list_to_string([*json.values()], True)

	query = ('INSERT INTO {} ({}) VALUES ({})'.format(table, keys, values))
	print(query)
	conn.execute(query)
	conn.commit()

def update(conn, table, json):
	keys = list_to_string([*json.keys()])
	values = list_to_string([*json.values()], True)

	#modificar query
	query = ('INSERT INTO {} ({}) VALUES ({})'.format(table, keys, values))
	print(query)
	conn.execute(query)
	conn.commit()

	for row in conn.execute("SELECT * FROM EMPLEADO"):
		print(row)



def list_to_string(list_convert, is_value=False):
	string = ''
	coma = "'" if is_value else ""
	for i, v in enumerate(list_convert):
		if i+1 < len(list_convert):
			string += "{}{}{}, ".format(coma, v, coma)
		else:
			string += "{}{}{}".format(coma, v, coma)
	return string
