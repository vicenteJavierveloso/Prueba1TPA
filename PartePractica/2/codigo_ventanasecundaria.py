from VentanaSecundaria import Ui_VentanaSecundaria
from PyQt6 import QtWidgets
class VentanaSecundaria(QtWidgets.QMainWindow, Ui_VentanaSecundaria):
    def __init__(self, *args, obj=None, **kwargs,):
        super(VentanaSecundaria, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        #Esconde la ventana al presionar ok
        self.pushButton.clicked.connect(self.hide)
    def cambiar_label3(self,informacion):
        self.label_3.setText(informacion)

