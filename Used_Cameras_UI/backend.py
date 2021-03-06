import os
import signal
import subprocess

import cv2
import numpy as np
from PySide6.QtWidgets import *
import multiprocessing as mp


class backend:
    def __init__(self, ui):
        self.ui = ui
        self.isOpen = [0] * 8
        self.pid = [0] * 8
        # self.url_list = ['rtsp://192.168.1.10:8554/test1', 'rtsp://192.168.1.10:8554/test2',
        #                  'rtsp://192.168.1.10:8554/test3', 'rtsp://192.168.1.10:8554/test4',
        #                  'rtsp://192.168.1.10:8554/test5', 'rtsp://192.168.1.10:8554/test6',
        #                  'rtsp://192.168.1.10:8554/test7', 'rtsp://192.168.1.10:8554/test8']

        self.url_list = ['/dev/video0', '/home/islam/Downloads/sample.mp4',
                         '/home/islam/Downloads/sample.mp4', '/home/islam/Downloads/sample.mp4',
                         '/home/islam/Downloads/sample.mp4','/home/islam/Downloads/sample.mp4',
                         '/home/islam/Downloads/sample.mp4','/home/islam/Downloads/sample.mp4']

        self.camerasCheckBox = []
        self.confirm_button = self.ui.findChild(QPushButton, 'confirm')
        self.exit_button = self.ui.findChild(QPushButton, 'exit')
        self.reset_button = self.ui.findChild(QPushButton, 'reset')
        self.select_all_button = self.ui.findChild(QPushButton, 'select_all')

        for i in range(8):
            self.camerasCheckBox.append(self.ui.findChild(QCheckBox, 'camera_' + str(i + 1)))

        self.exit_button.clicked.connect(self.exit)
        self.confirm_button.clicked.connect(self.updateCameras)
        self.reset_button.clicked.connect(self.reset)
        self.select_all_button.clicked.connect(self.select)


    def exit(self):
        self.ui.close()

    def updateCameras(self):
        x = 10
        y = 10
        for i in range(8):
            if self.camerasCheckBox[i].isChecked() and self.isOpen[i] == 0:
                p = subprocess.Popen(["python3", "cam.py", str(self.url_list[i]), str(x), str(y)])
                self.pid[i] = p.pid
                self.isOpen[i] = 1
            if not self.camerasCheckBox[i].isChecked() and self.isOpen[i] == 1:
                os.kill(self.pid[i], signal.SIGTERM)
                self.isOpen[i] = 0
            if i == 3:
                y = 350
                x = 10
            else:
                x += 400

    def reset(self):
        for box in self.camerasCheckBox:
            box.setChecked(False)

    def select(self):
        for box in self.camerasCheckBox:
            box.setChecked(True)
