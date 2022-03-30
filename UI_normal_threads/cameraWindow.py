import time

import PySide6
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile
from PySide6.QtCore import Slot
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from cameraThread import cameraThread


class CameraWindow(QWidget):
    def __init__(self):
        super(CameraWindow, self).__init__()
        loader = QUiLoader()
        uifile = QFile('cameras_window.ui')
        uifile.open(QFile.ReadOnly)
        self.ui = loader.load(uifile, None)
        uifile.close()
        self.ui.setWindowFlags(PySide6.QtCore.Qt.FramelessWindowHint)
        self.ui.showMaximized()

        self.label_1 = self.ui.findChild(QLabel, 'label_1')
        self.label_2 = self.ui.findChild(QLabel, 'label_2')
        self.label_3 = self.ui.findChild(QLabel, 'label_3')
        self.label_4 = self.ui.findChild(QLabel, 'label_4')
        self.label_5 = self.ui.findChild(QLabel, 'label_5')
        self.label_6 = self.ui.findChild(QLabel, 'label_6')
        self.label_7 = self.ui.findChild(QLabel, 'label_7')
        self.label_8 = self.ui.findChild(QLabel, 'label_8')
        self.exit_button = self.ui.findChild(QAction, 'actionExit')

        # self.url_list = ['rtsp://192.168.1.10:8554/test1', 'rtsp://192.168.1.10:8554/test2', 'rtsp://192.168.1.10:8554/test3', 'rtsp://192.168.1.10:8554/test4', 'rtsp://192.168.1.10:8554/test5', 'rtsp://192.168.1.10:8554/test6', 'rtsp://192.168.1.10:8554/test7', 'rtsp://192.168.1.10:8554/test8']
        self.url_list = ['/home/islam/Downloads/sample.mp4', '/home/islam/Downloads/sample.mp4', 0, '/home/islam/Downloads/sample.mp4',
                         '/home/islam/Downloads/sample.mp4', '/home/islam/Downloads/sample.mp4', '/home/islam/Downloads/sample.mp4', '/home/islam/Downloads/sample.mp4']
        self.camera1 = cameraThread(self.url_list)

        self.camera1.ImageUpdate.connect(self.ImageUpdateSlot1)
        self.camera1.ImageUpdate2.connect(self.ImageUpdateSlot2)
        self.camera1.ImageUpdate3.connect(self.ImageUpdateSlot3)
        self.camera1.ImageUpdate4.connect(self.ImageUpdateSlot4)
        self.camera1.ImageUpdate5.connect(self.ImageUpdateSlot5)
        self.camera1.ImageUpdate6.connect(self.ImageUpdateSlot6)
        self.camera1.ImageUpdate7.connect(self.ImageUpdateSlot7)
        self.camera1.ImageUpdate8.connect(self.ImageUpdateSlot8)
        self.exit_button.triggered.connect(self.exitSlot)

        self.camera1.start()

    def ImageUpdateSlot1(self, Image):
        self.label_1.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot2(self, Image):
        self.label_2.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot3(self, Image):
        self.label_3.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot4(self, Image):
        self.label_4.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot5(self, Image):
        self.label_5.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot6(self, Image):
        self.label_6.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot7(self, Image):
        self.label_7.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot8(self, Image):
        self.label_8.setPixmap(QPixmap.fromImage(Image))

    def exitSlot(self):
        # stopping the thread
        self.camera1.stop()
        # delay to wait the thread to close
        time.sleep(0.25)
        # closing the ui
        self.ui.close()
