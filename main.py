import sys
import cv2
import numpy as np
import torch
import screeninfo
from mss import mss
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QTimer
from ultralytics import YOLO


model_path = "model/best.pt" 
model = YOLO(model_path)

class_names = model.names

screen = screeninfo.get_monitors()[0]
WIDTH, HEIGHT = screen.width, screen.height

monitor = {"top": 0, "left": 0, "width": WIDTH, "height": HEIGHT}

class OverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, WIDTH, HEIGHT)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(4)

        self.detections = []
        self.previous_positions = {}

    def update_frame(self):
        with mss() as sct:
            screenshot = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

            results = model(frame)

            self.detections = []
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = float(box.conf[0])
                    cls_id = int(box.cls[0])
                    if conf > 0.5:
                        class_name = class_names[cls_id]

                        cx = (x1 + x2) // 2
                        cy = (y1 + y2) // 2

                        self.detections.append((x1, y1, x2, y2, cx, cy, class_name))

        self.repaint()

    # 예상 진행 경로 표시
    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor(0, 255, 0))
        pen.setWidth(3)
        painter.setPen(pen)

        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        painter.setFont(font)

        new_positions = {}

        for (x1, y1, x2, y2, cx, cy, class_name) in self.detections:
            painter.drawRect(x1, y1, x2 - x1, y2 - y1)

            painter.setPen(QColor(255, 255, 255))
            painter.drawText(x1, y1 - 10, class_name)

            if class_name in self.previous_positions:
                prev_cx, prev_cy = self.previous_positions[class_name]

                dx = cx - prev_cx
                dy = cy - prev_cy

                painter.setPen(QColor(255, 0, 0))
                painter.drawLine(cx, cy, cx + dx * 10, cy + dy * 10)

            new_positions[class_name] = (cx, cy)

        self.previous_positions = new_positions


if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = OverlayWindow()
    overlay.showFullScreen()
    sys.exit(app.exec_())
