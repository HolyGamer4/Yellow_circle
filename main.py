import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


class Main(QMainWindow):
    def __init__(self):
        self.flag = False
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            for i in range(random.randint(1, 15)):
                x = random.randint(1, 800)
                y = random.randint(1, 600)
                a = random.randint(1, 100)
                painter.drawEllipse(x, y, a, a)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())