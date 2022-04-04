import sys

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication

from backend import backend


class App:
    def __init__(self):
        self.ui = self.loadUiWidget('mainwindow.ui')
        self.ui.show()

    def loadUiWidget(self, uifilename, parent=None):
        loader = QUiLoader()
        uifile = QFile(uifilename)
        uifile.open(QFile.ReadOnly)
        ui = loader.load(uifile, parent)
        uifile.close()
        return ui


app = QApplication(sys.argv)
a = App()
back = backend(a.ui)
app.exec()
