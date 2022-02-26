import sys
import os

from Qt import (QtWidgets, __binding__, __binding_version__, __qt_version__, __version__)

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100, 100, 200, 200)
    b.move(50, 20)
    w.setWindowTitle("PyQt")
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    print("__binding__:" + __binding__)
    print("__binding_version__:" + __binding_version__)
    print("__qt_version__:" + __qt_version__)
    print("__version__:" + __version__)

    window()
