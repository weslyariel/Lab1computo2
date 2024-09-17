import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox

class VentanaDatos(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Lectura de Datos")
        self.setGeometry(100, 100, 300, 200)
        
        # Crear etiquetas y campos de entrada
        self.nombre_label = QLabel("Nombre completo:", self)
        self.nombre_input = QLineEdit(self)
        
        self.cedula_label = QLabel("Número de cédula/Dui:", self)
        self.cedula_input = QLineEdit(self)
        
        # Crear botón para confirmar los datos
        self.boton_confirmar = QPushButton("Confirmar", self)
        self.boton_confirmar.clicked.connect(self.mostrar_datos)
        
        # Crear un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.cedula_label)
        layout.addWidget(self.cedula_input)
        layout.addWidget(self.boton_confirmar)
        
        # Asignar el layout a la ventana
        self.setLayout(layout)
    
    # Método para mostrar los datos ingresados en un cuadro de diálogo
    def mostrar_datos(self):
        nombre = self.nombre_input.text()
        cedula = self.cedula_input.text()
        QMessageBox.information(self, "Datos ingresados", f"Nombre: {nombre}\nCédula/Dui: {cedula}")

# Inicialización de la aplicación
app = QApplication(sys.argv)
ventana = VentanaDatos()
ventana.show()
sys.exit(app.exec_())