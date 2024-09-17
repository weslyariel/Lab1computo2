import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox

class VentanaClave(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Entrada de Clave Secreta")
        self.setGeometry(100, 100, 300, 150)
        
        # Crear etiqueta para la clave secreta
        self.clave_label = QLabel("Introduce tu clave secreta:", self)
        
        # Crear campo de entrada de texto para la clave secreta
        self.clave_input = QLineEdit(self)
        self.clave_input.setEchoMode(QLineEdit.Password)  # Ocultar caracteres
        
        # Crear botón para confirmar la clave
        self.boton_confirmar = QPushButton("Confirmar", self)
        self.boton_confirmar.clicked.connect(self.mostrar_clave)
        
        # Crear un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.clave_label)
        layout.addWidget(self.clave_input)
        layout.addWidget(self.boton_confirmar)
        
        # Asignar el layout a la ventana
        self.setLayout(layout)
    
    # Método para mostrar la clave ingresada en un cuadro de diálogo
    def mostrar_clave(self):
        clave = self.clave_input.text()
        QMessageBox.information(self, "Clave ingresada", f"Tu clave es: {clave}")

# Inicialización de la aplicación
app = QApplication(sys.argv)
ventana = VentanaClave()
ventana.show()
sys.exit(app.exec_())