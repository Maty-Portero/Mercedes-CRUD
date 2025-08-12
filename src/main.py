import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi App con PyQt y Docker")
        self.setGeometry(100, 100, 400, 300)

        label = QLabel("¡Hola desde PyQt!", self)
        label.move(150, 150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())