import sys
from PyQt6 import QtWidgets, uic

from VentanaPrincipal import Ui_VentanaPrincipal
from codigo_ventanasecundaria import VentanaSecundaria


class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        self.pushButton.clicked.connect(self.guardar_mascota)
        self.ventana_2 = VentanaSecundaria()

    def guardar_mascota(self):
        mascota = Mascota(self.entrada_nombre.text(),self.entrada_especie.text(),self.entrada_edad.value(),self.entrada_peso.value())
        self.ventana_2.cambiar_label3(mascota.__str__())
        if self.ventana_2.isVisible():
            self.ventana_2.hide()
        else:
            self.ventana_2.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    app.exec()