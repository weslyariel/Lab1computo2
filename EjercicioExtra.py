import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox, QComboBox

class CalculadoraHuellaCarbono(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Calculadora de Huella de Carbono - Transporte")
        self.setGeometry(100, 100, 400, 200)
        
        # Crear etiqueta y campo para la distancia
        self.distancia_label = QLabel("Distancia recorrida (en km):", self)
        self.distancia_input = QLineEdit(self)
        self.distancia_input.setPlaceholderText("Introduce la distancia en kilómetros")
        
        # Crear etiqueta y selección para el tipo de transporte
        self.transporte_label = QLabel("Tipo de transporte:", self)
        self.transporte_combo = QComboBox(self)
        self.transporte_combo.addItems(["Coche", "Motocicleta", "Autobús", "Tren", "Bicicleta", "A pie"])
        
        # Crear botón para calcular
        self.boton_calcular = QPushButton("Calcular Huella de Carbono", self)
        self.boton_calcular.clicked.connect(self.calcular_huella)
        
        # Crear layout y agregar widgets
        layout = QVBoxLayout()
        layout.addWidget(self.distancia_label)
        layout.addWidget(self.distancia_input)
        layout.addWidget(self.transporte_label)
        layout.addWidget(self.transporte_combo)
        layout.addWidget(self.boton_calcular)
        
        self.setLayout(layout)
    
    def calcular_huella(self):
        try:
            distancia = float(self.distancia_input.text())
            transporte = self.transporte_combo.currentText()
            
            # Factores de emisión de CO2 por kilómetro (en kg de CO2/km)
            factores_emision = {
                "Coche": 0.21,
                "Motocicleta": 0.10,
                "Autobús": 0.06,
                "Tren": 0.04,
                "Bicicleta": 0.0,
                "A pie": 0.0
            }
            
            # Calcular huella de carbono
            huella_carbono = distancia * factores_emision[transporte]
            
            # Mostrar resultado
            QMessageBox.information(self, "Huella de Carbono", 
                                    f"Transporte: {transporte}\nDistancia: {distancia} km\nHuella de Carbono: {huella_carbono:.2f} kg de CO₂")
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, introduce un valor numérico válido para la distancia.")

# Inicialización de la aplicación
app = QApplication(sys.argv)
ventana = CalculadoraHuellaCarbono()
ventana.show()
sys.exit(app.exec_())