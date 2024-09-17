import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox

class VentanaMascotas(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Datos de Mascotas")
        self.setGeometry(100, 100, 400, 400)
        
        # Crear etiquetas y campos de entrada para cada mascota
        self.crear_campos_mascota("1", "Primera Mascota:")
        self.crear_campos_mascota("2", "Segunda Mascota:")
        self.crear_campos_mascota("3", "Tercera Mascota:")
        
        # Crear botón para confirmar los datos
        self.boton_confirmar = QPushButton("Confirmar", self)
        self.boton_confirmar.clicked.connect(self.mostrar_datos)
        
        # Crear un layout vertical
        layout = QVBoxLayout()
        
        # Añadir todos los elementos al layout
        layout.addWidget(self.label_mascota1)
        layout.addWidget(self.nombre_input1)
        layout.addWidget(self.especie_input1)
        layout.addWidget(self.edad_input1)

        layout.addWidget(self.label_mascota2)
        layout.addWidget(self.nombre_input2)
        layout.addWidget(self.especie_input2)
        layout.addWidget(self.edad_input2)

        layout.addWidget(self.label_mascota3)
        layout.addWidget(self.nombre_input3)
        layout.addWidget(self.especie_input3)
        layout.addWidget(self.edad_input3)
        
        layout.addWidget(self.boton_confirmar)
        
        # Asignar el layout a la ventana
        self.setLayout(layout)
    
    def crear_campos_mascota(self, num, titulo):
        # Crear etiquetas y campos de entrada para cada mascota
        setattr(self, f"label_mascota{num}", QLabel(titulo, self))
        
        setattr(self, f"nombre_input{num}", QLineEdit(self))
        getattr(self, f"nombre_input{num}").setPlaceholderText("Nombre de la mascota")
        
        setattr(self, f"especie_input{num}", QLineEdit(self))
        getattr(self, f"especie_input{num}").setPlaceholderText("Especie de la mascota")
        
        setattr(self, f"edad_input{num}", QLineEdit(self))
        getattr(self, f"edad_input{num}").setPlaceholderText("Edad de la mascota")
    
    # Método para mostrar los datos ingresados en un cuadro de diálogo
    def mostrar_datos(self):
        datos_mascotas = ""
        for i in range(1, 4):
            nombre = getattr(self, f"nombre_input{i}").text()
            especie = getattr(self, f"especie_input{i}").text()
            edad = getattr(self, f"edad_input{i}").text()
            datos_mascotas += f"Mascota {i}:\nNombre: {nombre}, Especie: {especie}, Edad: {edad} años\n\n"
        
        QMessageBox.information(self, "Datos de las Mascotas", datos_mascotas)

# Inicialización de la aplicación
app = QApplication(sys.argv)
ventana = VentanaMascotas()
ventana.show()
sys.exit(app.exec_())