from PySide6.QtGui import *
from PySide6.QtCore import *
import cv2


class cameraThread(QThread):

    def __init__(self, ip):
        super(cameraThread, self).__init__()
        self.ip = ip

    ImageUpdate = Signal(QImage)
    ImageUpdate2 = Signal(QImage)
    ImageUpdate3 = Signal(QImage)
    ImageUpdate4 = Signal(QImage)
    ImageUpdate5 = Signal(QImage)
    ImageUpdate6 = Signal(QImage)
    ImageUpdate7 = Signal(QImage)
    ImageUpdate8 = Signal(QImage)

    def run(self):
        self.ThreadActive = True
        capture = cv2.VideoCapture(self.ip[0])
        capture2 = cv2.VideoCapture(self.ip[1])
        capture3 = cv2.VideoCapture(self.ip[2])
        capture4 = cv2.VideoCapture(self.ip[3])
        capture5 = cv2.VideoCapture(self.ip[4])
        capture6 = cv2.VideoCapture(self.ip[5])
        capture7 = cv2.VideoCapture(self.ip[6])
        capture8 = cv2.VideoCapture(self.ip[7])

        while self.ThreadActive:
            capture.grab()
            ret, frame = capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],
                                           QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(480, 515, Qt.IgnoreAspectRatio)
                self.ImageUpdate.emit(Pic)

            capture2.grab()
            ret2, frame2 = capture2.read()
            if ret2:
                Image2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                FlippedImage2 = cv2.flip(Image2, 1)
                ConvertToQtFormat2 = QImage(FlippedImage2.data, FlippedImage2.shape[1], FlippedImage2.shape[0],
                                           QImage.Format_RGB888)
                Pic2 = ConvertToQtFormat2.scaled(480, 515, Qt.IgnoreAspectRatio)
                self.ImageUpdate2.emit(Pic2)

            capture3.grab()
            ret3, frame3 = capture3.read()
            if ret3:
                Image3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGB)
                FlippedImage3 = cv2.flip(Image3, 1)
                ConvertToQtFormat3 = QImage(FlippedImage3.data, FlippedImage3.shape[1], FlippedImage3.shape[0],
                                            QImage.Format_RGB888)
                Pic3 = ConvertToQtFormat3.scaled(480, 515, Qt.IgnoreAspectRatio)
                self.ImageUpdate3.emit(Pic3)

            capture4.grab()
            ret4, frame4 = capture4.read()
            if ret4:
                Image4 = cv2.cvtColor(frame4, cv2.COLOR_BGR2RGB)
                FlippedImage4 = cv2.flip(Image4, 1)
                ConvertToQtFormat4 = QImage(FlippedImage4.data, FlippedImage4.shape[1], FlippedImage4.shape[0],
                                            QImage.Format_RGB888)
                Pic4 = ConvertToQtFormat4.scaled(480, 515, Qt.IgnoreAspectRatio)
                self.ImageUpdate4.emit(Pic4)

            capture5.grab()
            ret5, frame5 = capture5.read()
            if ret5:
                Image5 = cv2.cvtColor(frame5, cv2.COLOR_BGR2RGB)
                FlippedImage5 = cv2.flip(Image5, 1)
                ConvertToQtFormat5 = QImage(FlippedImage5.data, FlippedImage5.shape[1], FlippedImage5.shape[0],
                                            QImage.Format_RGB888)
                Pic5 = ConvertToQtFormat5.scaled(480, 515, Qt.IgnoreAspectRatio)
                self.ImageUpdate5.emit(Pic5)

            capture6.grab()
            ret6, frame6 = capture6.read()
            if ret6:
                Image6 = cv2.cvtColor(frame6, cv2.COLOR_BGR2RGB)
                FlippedImage6 = cv2.flip(Image6, 1)
                ConvertToQtFormat6 = QImage(FlippedImage6.data, FlippedImage6.shape[1], FlippedImage6.shape[0],
                                            QImage.Format_RGB888)
                Pic6 = ConvertToQtFormat6.scaled(480, 515, Qt.IgnoreAspectRatio)
                self.ImageUpdate6.emit(Pic6)

            capture7.grab()
            ret7, frame7 = capture7.read()
            if ret7:
                Image7 = cv2.cvtColor(frame7, cv2.COLOR_BGR2RGB)
                FlippedImage7 = cv2.flip(Image7, 1)
                ConvertToQtFormat7 = QImage(FlippedImage7.data, FlippedImage7.shape[1], FlippedImage7.shape[0],
                                            QImage.Format_RGB888)
                Pic7 = ConvertToQtFormat7.scaled(480, 515, Qt.IgnoreAspectRatio)
                self.ImageUpdate7.emit(Pic7)

            capture8.grab()
            ret8, frame8 = capture8.read()
            if ret8:
                Image8 = cv2.cvtColor(frame8, cv2.COLOR_BGR2RGB)
                FlippedImage8 = cv2.flip(Image8, 1)
                ConvertToQtFormat8 = QImage(FlippedImage8.data, FlippedImage8.shape[1], FlippedImage8.shape[0],
                                            QImage.Format_RGB888)
                Pic8 = ConvertToQtFormat8.scaled(480, 517, Qt.IgnoreAspectRatio)
                self.ImageUpdate8.emit(Pic8)

        capture.release()
        capture2.release()
        capture3.release()
        capture4.release()
        capture5.release()
        capture6.release()
        capture7.release()
        capture8.release()


    def stop(self):
        self.ThreadActive = False
        self.quit()