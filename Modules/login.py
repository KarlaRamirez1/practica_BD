from PySide6.QtWidgets import QMessageBox, QLineEdit, QDialog
from PySide6 import QtCore


from modules.login_ui import Ui_Dialog


################################################################################
class Login(QDialog):#faltan validaciones
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		global this
		this = self.ui
		        
		flags = QtCore.Qt.WindowFlags(QtCore.Qt.Dialog)
		self.setWindowFlags(flags|QtCore.Qt.FramelessWindowHint |QtCore.Qt.CustomizeWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)#fondo de la ventana transparente


		self.cancel = False
		self.btnActive = False
		self.UserType = -1

		this.btn_closed.clicked.connect(self.close)
		# this.User.setPlaceholderText("Nombre o correo")
		# this.Password.setPlaceholderText("Contraseña")
		this.Password.setEchoMode(QLineEdit.Password)
		this.btn_accept.clicked.connect(self.connect)
	
	def connect(self):
		if this.User.text() != "admin":
			QMessageBox.about(self,"Error", "Usuario Incorrecto.")
			return
		if this.Password.text() != "1234":
			QMessageBox.about(self,"Error", "Contraseña Incorrecta.")
			return
		#Recoger datos usuario.
		#self.UserType = 0
		self.btnActive = True
		self.close()
	
	def closeEvent(self, event):
		if self.btnActive == False:
			self.cancel = True

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