# helloQt
Toy problem to get PySide2, Qt.py, and QT Designer .ui files playing nice with PyInstaller

### Notes:
1. compile with pyinstaller helloQt.spec, or pyinstaller helloQtUI.spec
2. Fixed rel path issue regarding where the files are temporarily unpacked during exec, more details here: https://stackoverflow.com/questions/59719083/pyinstaller-ui-files?noredirect=1&lq=1
3. Added dynamic import of PySide2 library to allow vendored or user-supplied library for LGPL compliance: https://stackoverflow.com/questions/56615123/python-use-importlib-to-import-a-module-from-a-package-directory/56615264#56615264
