import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 1  Seccion Practica Prueba Individual")
        #Elementos
        nombre = QLabel("Nombre Usuario")
        descripcion = QLabel("Texto descripcion Usuario")
        atributo1 = QLabel("Atributo 1")
        atributo2 = QLabel("Atributo 2")
        atributo3 = QLabel("Atributo 3")
        atributo4 = QLabel("Atributo 4")
        atributo5 = QLabel("Atributo 5")
        atributo6 = QLabel("Atributo 6")
        valor1 = QLabel("Valor 1")
        valor2 = QLabel("Valor 2")
        valor3 = QLabel("Valor 3")
        valor4 = QLabel("Valor 4")
        valor5 = QLabel("Valor 5")
        valor6 = QLabel("Valor 6")
        imagen = QLabel("Imagen")
        boton = QPushButton("Ok")
        #Contenedores
        atrib_val = QGridLayout()
        #Atributos
        atrib_val.addWidget(atributo1,0,0)
        atrib_val.addWidget(atributo2,1,0)
        atrib_val.addWidget(atributo3,2,0)
        atrib_val.addWidget(atributo4,3,0)
        atrib_val.addWidget(atributo5,4,0)
        atrib_val.addWidget(atributo6,5,0)
        #Valores
        atrib_val.addWidget(valor1,0,1)
        atrib_val.addWidget(valor2,1,1)
        atrib_val.addWidget(valor3,2,1)
        atrib_val.addWidget(valor4,3,1)
        atrib_val.addWidget(valor5,4,1)
        atrib_val.addWidget(valor6,5,1)

        imagen_desc = QVBoxLayout()
        imagen_desc.addWidget(imagen)
        imagen_desc.addWidget(descripcion)

        imagen_desc_atrib_val = QHBoxLayout()
        imagen_desc_atrib_val.addLayout(imagen_desc)
        imagen_desc_atrib_val.addLayout(atrib_val)

        contenedor_principal = QVBoxLayout()
        contenedor_principal.addWidget(nombre)
        contenedor_principal.addLayout(imagen_desc_atrib_val)
        contenedor_principal.addWidget(boton)
        
        ventana = QWidget()
        ventana.setLayout(contenedor_principal)
        self.setCentralWidget(ventana)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()