import sys
from random import randrange

from ui import Ui_mainwin
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Program(QMainWindow, Ui_mainwin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        for i in range(randrange(5, 20)):
            qp.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
            r = randrange(10, 150)
            qp.drawEllipse(randrange(self.width()), randrange(self.height()), r, r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec_())