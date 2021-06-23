from PySide6.QtWidgets import QMessageBox, QLineEdit, QDialog
from PySide6 import QtCore


from modules.login_ui import Ui_Dialog
from modules.db.crud import create, get_count, read_admin

################################################################################
class Login(QDialog):#faltan validaciones
	def __init__(self, conn):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		global this
		this = self.ui

		self.conn = conn
		self.cancel = False
		self.user = None
		        
		flags = QtCore.Qt.WindowFlags(QtCore.Qt.Dialog)
		self.setWindowFlags(flags|QtCore.Qt.FramelessWindowHint |QtCore.Qt.CustomizeWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)#fondo de la ventana transparente



		this.btn_closed.clicked.connect(self.close)
		this.Password.setEchoMode(QLineEdit.Password)
		this.btn_accept.clicked.connect(self.connect)

		this.User.setText("kelly")
		this.Password.setText("1234")

		if get_count(self.conn, "Empleado") == 0:
			QMessageBox.about(self, "Hola", "Es la primera vez que entras?\ncrea tu nombre de\nusuario y tu contraseña.")
	
	def connect(self):
		if get_count(self.conn, "Empleado") == 0:
			#crear nuevo usuario
			json2 = {  
				"Nombre_usuario": this.User.text(),
				"contrasenia": this.Password.text(),
				"Puesto": '0'
			}
			create(self.conn, "Empleado", json2)
			self.user = read_admin(self.conn, "Empleado", this.User.text(), this.Password.text())
		else:
    		#evaluar si el usuario existe
			self.user = read_admin(self.conn, "Empleado", this.User.text(), this.Password.text())
			if self.user == None:
				QMessageBox.about(self, "Error", "Usuario o contraseña incorrectos")
				return

		self.close()

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

	def closeEvent(self, event):
		if self.user == None:
			self.cancel = True
			self.conn.close()