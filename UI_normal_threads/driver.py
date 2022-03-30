import sys

import PySide6
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile
from PySide6.QtCore import Slot
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from cameraWindow import CameraWindow

app = QApplication(sys.argv)

c = CameraWindow()
app.exec()
