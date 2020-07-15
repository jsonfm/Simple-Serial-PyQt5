import sys 
from PyQt5.QtWidgets import QMainWindow,QApplication
from GUI import *
from customSerial import customSerial

class MiApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#Serial
		self.serial = customSerial()

		self.ui.BaudList.addItems(self.serial.baudratesDIC.keys())
		self.ui.BaudList.setCurrentText('9600')
		self.update_ports()
		
		#Events
		self.ui.connectBtn.clicked.connect(self.connect_serial)
		self.ui.sendBtn.clicked.connect(self.send_data)
		self.ui.updateBtn.clicked.connect(self.update_ports)
		self.ui.clearBtn.clicked.connect(self.clear_terminal)
		self.serial.data_available.connect(self.update_terminal)

	def update_terminal(self,data):
		self.ui.Terminal.append(data)

	def connect_serial(self):
		if(self.ui.connectBtn.isChecked()):
			port = self.ui.portList.currentText()
			baud = self.ui.BaudList.currentText()
			self.serial.serialPort.port = port 
			self.serial.serialPort.baudrate = baud
			self.serial.connect_serial()
			#Si se logra conectar
			if(self.serial.serialPort.is_open):
				self.ui.connectBtn.setText('DESCONECTAR')
				#print("Me conecté")

			#No se logró conectar	
			else:
				#print("No me conecte")
				self.ui.connectBtn.setChecked(False)
			
		else:
			#print("Desconectarme")
			self.serial.disconnect_serial()
			self.ui.connectBtn.setText('CONECTAR')

	def send_data(self):
		data = self.ui.input.text()
		self.serial.send_data(data)

	def update_ports(self):
		self.serial.update_ports()
		self.ui.portList.clear()
		self.ui.portList.addItems(self.serial.portList)

	def clear_terminal(self):
		self.ui.Terminal.clear()

	def closeEvent(self,e):
		self.serial.disconnect_serial()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MiApp()
	w.show()
	sys.exit(app.exec_())

