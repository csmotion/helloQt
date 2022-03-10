import sys
import os

# pyinstaller --onefile --hidden-import=Qt.py --hidden-import=PySide2.QtXml --hidden-import=PySide2.QtUiTools helloQt.py helloQT.spec --windowed
# pyinstaller helloQtUI.spec

# Dynamically import PySide2 for LGPL license: https://stackoverflow.com/questions/56615123/python-use-importlib-to-import-a-module-from-a-package-directory/56615264#56615264
if os.path.isdir('./PySide2/'):
	print('Importing local PySide2')
	IMPORTED_FROM = "user supplied import!"

	MODULE_PATH = "./PySide2/__init__.py"
	MODULE_NAME = "PySide2"

	import importlib.util
	spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
	module = importlib.util.module_from_spec(spec)
	sys.modules[spec.name] = module
	spec.loader.exec_module(module)
	PySide2 = module
else:
	print('Importing system PySide2')
	IMPORTED_FROM = "vendor supplied import!"
	
	import PySide2
	print(PySide2.__version__)

# os.environ['QT_PREFERRED_BINDING'] = 'PySide2'
from Qt import (QtCompat, QtWidgets, __binding__, __binding_version__, __qt_version__, __version__)

class MainWindow(QtWidgets.QWidget):
	# Load .ui file example, using setattr/getattr approach
	# def __init__(self, ServoCommand:ServoCommand, parent=None):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)

		# Import .ui forms for the GUI using function resource_path()
		form = self.resource_path("GUI\helloQtUI.ui")
		self.uiLoader(form, self)

		self.lineEdit.setText(IMPORTED_FROM)

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