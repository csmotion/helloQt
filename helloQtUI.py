import sys
import os

# os.environ['QT_PREFERRED_BINDING'] = 'PySide2'
from Qt import (QtCompat, QtWidgets, __binding__, __binding_version__, __qt_version__, __version__)

# pyinstaller --onefile --hidden-import=Qt.py --hidden-import=PySide2.QtXml --hidden-import=PySide2.QtUiTools helloQt.py helloQT.spec --windowed

class MainWindow(QtWidgets.QWidget):
	# Load .ui file example, using setattr/getattr approach
	# def __init__(self, ServoCommand:ServoCommand, parent=None):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)

		# Import .ui forms for the GUI using function resource_path()
		form = self.resource_path("GUI\helloQtUI.ui")

		self.baseInst = self.uiLoader(form, self)
		# self.setFocusPolicy(QtCore.Qt.StrongFocus)
		# self.keyPressEvent.connect(self.KeyPressEvent)
		# self.connectSlotsMain()

	def resource_path(self, relative_path):
		""" Get absolute path to resource, works for dev and for PyInstaller """
		try:
			# PyInstaller creates a temp folder and stores path in _MEIPASS
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath(".")

		return os.path.join(base_path, relative_path)

	def uiLoader(self, uifile, baseInst=None):
		"""
		Qt.py/PyQtGraph compatible loading of Qt Designer .ui file, loaded into baseInst

		Parameters
		----------
		uifile : .ui
			QT Designer UI file
		baseInst : _type_, optional
			_description_, by default None

		Returns
		-------
		_type_
			_description_
		"""
		ui = QtCompat.loadUi(uifile)  # Qt.py mapped function
		if not baseInst:
			return ui
		else:
			for member in dir(ui):
				if not member.startswith('__') and \
				member is not 'staticMetaObject':
					setattr(baseInst, member, getattr(ui, member))
			return ui

if __name__ == '__main__':
	print("__binding__:" + __binding__)
	print("__binding_version__:" + __binding_version__)
	print("__qt_version__:" + __qt_version__)
	print("__version__:" + __version__)

	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()

	# app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))

	window.show()
	app.exec_()