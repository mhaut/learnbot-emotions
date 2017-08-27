from PyQt4.QtCore import Qt
import Faces
import sys
from PyQt4.QtGui import QWidget, QApplication, QHBoxLayout


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.initUI()
        self.graphic = Faces.Face()
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.graphic)
        self.graphic.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff )
        self.graphic.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mainLayout.setMargin(0)
        self.mainLayout.setSpacing(0)
    def initUI(self):
        self.setGeometry(0, 0, 480, 320)
        self.setStyleSheet("background: black")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()
def main():
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
