import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication




class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.btn.clicked.connect(self.btnpress)

    def btnpress(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.drawcircles(qp)
            qp.end()
            self.draw = False

    def drawcircles(self, qp):
        qp.setBrush(Qt.yellow)
        for i in range(randrange(5, 20)):
            r = randrange(10, 100)
            qp.drawEllipse(randrange(800), randrange(600), r, r)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())