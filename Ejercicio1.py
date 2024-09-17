import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Información Personal")
        self.setGeometry(100, 100, 300, 200)
        
        # Crear etiquetas con el nombre y la edad
        self.nombre_label = QLabel("Nombre completo: Wesly Ariel Umanzor Arias", self)
        self.edad_label = QLabel("Edad: 21 años", self)
        
        # Alinear el texto al centro
        self.nombre_label.setAlignment(Qt.AlignCenter)
        self.edad_label.setAlignment(Qt.AlignCenter)
        
        # Crear un layout vertical para colocar las etiquetas
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.edad_label)
        
        # Asignar el layout a la ventana
        self.setLayout(layout)

# Inicialización de la aplicación
app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec_())
