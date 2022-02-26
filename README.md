# helloQt
Toy problem to get PySide2, Qt.py, and QT Designer .ui files playing nice with PyInstaller

### Notes:
1. compile with pyinstaller helloQt.spec, or pyinstaller helloQtUI.spec
2. Seems like a rel path issue regarding where the files are temporarily unpacked during exec, more details here: https://stackoverflow.com/questions/59719083/pyinstaller-ui-files?noredirect=1&lq=1
3. Still need to figure out how to allow PySide2 swap for LGPL compliance, but a good option exists here: https://stackoverflow.com/questions/56615123/python-use-importlib-to-import-a-module-from-a-package-directory/56615264#56615264
