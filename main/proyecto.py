import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "ProyectoTitulo"
        self.setWindowTitle(self.title)
    
        # Crear el QStackedWidget para manejar diferentes pantallas
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.setGeometry(100, 100, 800, 600)

        # Variable para almacenar la referencia del botón blanco
        self.boton_blanco = None

        # Pantalla inicial
        self.setup_inicial()

        # Pantalla de juego
        self.setup_juego()

        # Crear la barra de menú
        self.construir_menu()

    def setup_inicial(self):
        # Esta es la pantalla inicial con el texto '¡BUSCAMINAS!'
        self.nombre_l = QLabel('''Instrucciones''')
        font = QFont('Times', 20)
        self.nombre_l.setFont(font)

        # Layout para la pantalla inicial
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_l, alignment=Qt.AlignCenter)

        # Crear un widget para la pantalla inicial
        self.inicial_widget = QWidget()
        self.inicial_widget.setLayout(layout)

        # Añadir la pantalla inicial al stacked widget
        self.stacked_widget.addWidget(self.inicial_widget)

    def setup_juego(self):
        # Esta es la pantalla de juego que contiene la matriz de botones
        # Crear la matriz de botones (2x2)
        self.boton_matriz = [[QPushButton('') for _ in range(2)] for _ in range(2)]

        # Estilo predeterminado para todos los botones
        for i in range(2):
            for j in range(2):
                self.boton_matriz[i][j].setFixedHeight(70)  # Botones más pequeños
                self.boton_matriz[i][j].setFixedWidth(70)   # Botones más pequeños
                self.boton_matriz[i][j].setStyleSheet('background-color: black; color: white;')
                self.boton_matriz[i][j].setEnabled(False)  # Desactivar la interacción de los botones

        # Crear un layout de cuadrícula para la pantalla de juego
        grid_layout = QGridLayout()

        # Añadir los botones a la cuadrícula usando la matriz
        for i in range(2):
            for j in range(2):
                grid_layout.addWidget(self.boton_matriz[i][j], i + 1, j)
        
        # Botón "Start" que ejecutará la función cambiar_color
        self.start_button = QPushButton("Start")
        self.start_button.setStyleSheet('background-color: green; color: white;')  # Botón Start verde
        self.start_button.clicked.connect(self.iniciar_cambio_color)
        grid_layout.addWidget(self.start_button, 3, 0, 1, 2)  # Colocamos el botón Start en la fila 3

        # Establecer márgenes y espacios entre los elementos de la cuadrícula
        grid_layout.setHorizontalSpacing(5)  # Espacio horizontal entre botones
        grid_layout.setVerticalSpacing(5)    # Espacio vertical entre botones
        grid_layout.setContentsMargins(10, 10, 10, 10)  # Márgenes alrededor de la cuadrícula

        # Crear un widget para la pantalla de juego
        self.juego_widget = QWidget()
        self.juego_widget.setLayout(grid_layout)

        # Añadir la pantalla de juego al stacked widget
        self.stacked_widget.addWidget(self.juego_widget)

        # Colocar un botón blanco aleatorio desde el inicio
        self.colocar_boton_blanco()

    def construir_menu(self):
        # Crear la barra de menú
        self.menu = self.menuBar()
        self.menu_archivo = self.menu.addMenu("&Modo")

        # Agregar acción para "Juego"
        self.menu_archivo.addAction("&Juego", self.mostrar_juego, 'Ctrl+j')

        # Agregar acción para "Instrucciones" (volver a la pantalla inicial)
        self.menu_archivo.addAction("&Instrucciones", self.mostrar_inicial, 'Ctrl+i')

        # Agregar acción de "Salir"
        self.menu_archivo.addAction("&Salir", self.close, 'Ctrl+s')

    def mostrar_juego(self):
        # Cambiar a la pantalla de juego (pantalla 1 en stacked widget)
        self.stacked_widget.setCurrentWidget(self.juego_widget)

    def mostrar_inicial(self):
        # Cambiar a la pantalla inicial (pantalla 0 en stacked widget)
        self.stacked_widget.setCurrentWidget(self.inicial_widget)

    # Función para cambiar el color de todos los botones (menos el blanco) al mismo color aleatorio
    def cambiar_colores_todos(self):
        # Generar un color aleatorio para todos los botones
        color_random = randint(1, 3)
        color = ""
        if color_random == 1:
            color = 'red'
        elif color_random == 2:
            color = 'blue'
        else:
            color = 'green'

        # Cambiar el color de todos los botones menos el botón blanco
        for i in range(2):
            for j in range(2):
                if self.boton_matriz[i][j] != self.boton_blanco:
                    self.boton_matriz[i][j].setStyleSheet(f'background-color: {color}; color: white;')

    # Función llamada cuando el botón Start es presionado
    def iniciar_cambio_color(self):
        # Inicia el cambio de color de todos los botones menos el blanco después de 5 segundos
        QTimer.singleShot(5000, self.cambiar_colores_todos)  # 5000 ms = 5 segundos

    def acomodo(self):
        # Restablecer todos los botones
        for i in range(2):
            for j in range(2):
                self.boton_matriz[i][j].setEnabled(True)
                self.boton_matriz[i][j].setStyleSheet('background-color: black; color: white;')  # Predeterminado negro

        # Colocar un nuevo botón blanco aleatorio después de reset
        self.colocar_boton_blanco()

    def colocar_boton_blanco(self):
        # Si ya existe un botón blanco, lo volvemos a poner en negro
        if self.boton_blanco:
            self.boton_blanco.setStyleSheet('background-color: black; color: white;')

        # Elegimos una posición aleatoria para el botón blanco
        i, j = randint(0, 1), randint(0, 1)

        # Cambiar el botón en esa posición a blanco
        self.boton_blanco = self.boton_matriz[i][j]
        self.boton_blanco.setStyleSheet('background-color: white; color: black;')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
