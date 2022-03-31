import subprocess
from PySide6.QtWidgets import *
import multiprocessing as mp


class backend:
    def __init__(self, ui):
        self.ui = ui
        self.isOpen = [0] * 8
        # self.url_list = ['rtsp://192.168.1.10:8554/test1', 'rtsp://192.168.1.10:8554/test2',
        #                  'rtsp://192.168.1.10:8554/test3', 'rtsp://192.168.1.10:8554/test4',
        #                  'rtsp://192.168.1.10:8554/test5', 'rtsp://192.168.1.10:8554/test6',
        #                  'rtsp://192.168.1.10:8554/test7', 'rtsp://192.168.1.10:8554/test8']

        self.url_list = ['/home/islam/Downloads/sample.mp4', '/home/islam/Downloads/sample.mp4', 0,
                         '/home/islam/Downloads/sample.mp4', '/home/islam/Downloads/sample.mp4',
                         '/home/islam/Downloads/sample.mp4', '/home/islam/Downloads/sample.mp4',
                         '/home/islam/Downloads/sample.mp4']
        self.camerasCheckBox = []
        self.confirm_button = self.ui.findChild(QPushButton, 'confirm')
        self.exit_button = self.ui.findChild(QPushButton, 'exit')

        for i in range(8):
            self.camerasCheckBox.append(self.ui.findChild(QCheckBox, 'camera_' + str(i + 1)))

        self.exit_button.clicked.connect(self.exit)
        self.confirm_button.clicked.connect(self.updateCameras)

    def exit(self):
        self.ui.close()

    def updateCameras(self):
        for i in range(8):
            if self.camerasCheckBox[i].isChecked() and self.isOpen[i] == 0:
                subprocess.Popen(["python3", "cam.py", str(self.url_list[i])])
                self.isOpen[i] = 1
            if not self.camerasCheckBox[i].isChecked():
                self.isOpen[i] = 0
