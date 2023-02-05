import os
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QTimer, QTime, Qt, QSize
from module import volume, radio

icons = ["./icons/hr3.png", "./icons/absolut_relax.png", "./icons/hr1.png", "./icons/hr4.png"]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.p = None
        self.ui = uic.loadUi('./gui/index_GUI.ui', self)
        self.default_volume = 50
        self.muted = False
        self.channel = 0
        self.icon = 0
        self.play = False

        self.init_ui()

        self.volume_btn_plus.clicked.connect(self.volume_up)
        self.volume_btn_minus.clicked.connect(self.volume_down)
        self.mute_btn.clicked.connect(self.mute)
        self.radio_btn_right.clicked.connect(self.next_channel)
        self.radio_btn_left.clicked.connect(self.prev_channel)
        self.radio_icon_btn.clicked.connect(self.stream)
        self.radio_icon_btn.setIcon(QIcon(icons[self.icon]))
        self.radio_icon_btn.setIconSize(QSize(300, 300))
        self.restart_btn.clicked.connect(radio.restart)
        self.volume_slider.valueChanged.connect(self.change_volume)

    def init_ui(self):
        self.time_label.setFont(QFont('Arial', 32))
        self.time_label.setAlignment(Qt.AlignCenter)

        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)

    def stream(self):
        if not self.play:
            radio.kill()
            radio.play(self.channel)
            self.play = True

        else:
            radio.kill()
            self.play = False

    def next_channel(self):
        self.play = False
        if self.channel == len(radio.channels) - 1:
            self.channel = 0
            self.icon = 0
            radio.kill()
            self.p = radio.play(self.channel)
            self.play = True
            self.radio_icon_btn.setIcon(QIcon(icons[self.icon]))
            self.radio_icon_btn.setIconSize(QSize(300, 300))

        else:
            self.channel += 1
            self.icon += 1
            radio.kill()
            self.p = radio.play(self.channel)
            self.play = True
            self.radio_icon_btn.setIcon(QIcon(icons[self.icon]))
            self.radio_icon_btn.setIconSize(QSize(300, 300))

    def prev_channel(self):
        self.play = False
        if self.channel == 0:
            self.channel = len(radio.channels) - 1
            self.icon = len(radio.channels) - 1
            radio.kill()
            self.p = radio.play(self.channel)
            self.play = True
            self.radio_icon_btn.setIcon(QIcon(icons[self.icon]))
            self.radio_icon_btn.setIconSize(QSize(300, 300))

        else:
            self.channel -= 1
            self.icon -= 1
            radio.kill()
            self.p = radio.play(self.channel)
            self.play = True
            self.radio_icon_btn.setIcon(QIcon(icons[self.icon]))
            self.radio_icon_btn.setIconSize(QSize(300, 300))

    def change_volume(self):
        vol = self.volume_slider.value()
        volume.set_volume(vol)

    def volume_up(self):
        volume.increase()
        current_volume = volume.get_volume()
        print(current_volume)
        self.volume_slider.setValue(current_volume)

    def volume_down(self):
        volume.decrease()
        current_volume = volume.get_volume()
        self.volume_slider.setValue(current_volume)

    def mute(self):
        if not self.muted:
            volume.mute()
            self.muted = True

        elif self.muted:
            volume.set_volume(self.default_volume)
            self.muted = False

    def show_time(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.time_label.setText(label_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MainWindow()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
