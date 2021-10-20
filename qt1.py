import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication
from PyQt6.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()
        #self.initUI()
        self.setWindowTitle('Absolute')
        self.setGeometry(500,300,400,300)
        styleSheet=(
           'background-color:blue'
        )
        self.setStyleSheet(styleSheet)
        self.show()


#if __name__ == '__main__':
app = QApplication([])
ex = Example()
sys.exit(app.exec())
