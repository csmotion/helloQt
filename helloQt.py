import sys
import os

# from PySide2.QtWidgets import QApplication
# os.environ['QT_PREFERRED_BINDING'] = 'PySide2'
from Qt import (QtWidgets, __binding__, __binding_version__, __qt_version__, __version__)

# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'~qgis directory\apps\Qt5\plugins'
# os.environ['PATH'] += r';~qgis directory\apps\qgis\bin;~qgis directory\apps\Qt5\bin'

# from PyQt5.QtCore import QLibraryInfo
# from PySide2.QtCore import QLibraryInfo

# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "C:\PROJECTS\Rocky Mountain Servo, LLC\SW\Python\Toy Problems\PyInstaller Qt Shim\myvenv\Lib\site-packages\PySide2\plugins"
# from pyqtgraph.Qt import QtGui

# pyinstaller -F helloQT.py --paths=C:\python37\Lib\site-packages\ --hidden-import=Qt.py --debug=imports
# pyinstaller -F -c helloQT.py --paths=C:\python37\Lib\site-packages\ --hidden-import=Qt.py --debug=imports
# pyinstaller helloQt.py helloQT.spec --windowed

# pyinstaller --onefile --hidden-import=Qt.py --hidden-import=PySide2.QtXml --hidden-import=PySide2.QtUiTools helloQt.py helloQT.spec --windowed

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