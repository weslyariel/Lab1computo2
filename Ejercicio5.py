import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox

class VentanaPersona(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Datos Personales")
        self.setGeometry(100, 100, 400, 500)
        
        # Definición de los campos
        self.campos = {
            "Nombre": "Introduce tu nombre",
            "Apellido": "Introduce tu apellido",
            "Edad": "Introduce tu edad",
            "Género": "Introduce tu género",
            "Nacionalidad": "Introduce tu nacionalidad",
            "Ocupación": "Introduce tu ocupación",
            "Teléfono": "Introduce tu número de teléfono",
            "Correo electrónico": "Introduce tu correo electrónico",
            "Dirección": "Introduce tu dirección",
            "Estado civil": "Introduce tu estado civil"
        }
        
        # Layout vertical
        layout = QVBoxLayout()
        
        # Crear los campos dinámicamente
        self.inputs = {}
        for campo, placeholder in self.campos.items():
            label = QLabel(f"{campo}:", self)
            input_field = QLineEdit(self)
            input_field.setPlaceholderText(placeholder)
            self.inputs[campo] = input_field
            layout.addWidget(label)
            layout.addWidget(input_field)
        
        # Crear botón para confirmar los datos
        self.boton_confirmar = QPushButton("Confirmar", self)
        self.boton_confirmar.clicked.connect(self.mostrar_datos)
        
        layout.addWidget(self.boton_confirmar)
        
        # Asignar el layout a la ventana
        self.setLayout(layout)
    
    # Método para mostrar los datos ingresados en un cuadro de diálogo
    def mostrar_datos(self):
        datos_persona = ""
        for campo, input_field in self.inputs.items():
            valor = input_field.text()
            datos_persona += f"{campo}: {valor}\n"
        
        QMessageBox.information(self, "Datos ingresados", datos_persona)

# Inicialización de la aplicación
app = QApplication(sys.argv)
ventana = VentanaPersona()
ventana.show()
sys.exit(app.exec_())