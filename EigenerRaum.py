from PyQt6.QtCore import QRect, Qt, QDateTime, QTimer
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QLabel, QPushButton

from TemplateRoom import TemplateRoom

class EigenerRaum(TemplateRoom):
    def __init__(self, parent=None):
        super(EigenerRaum, self).__init__(parent)

        self.init_room("weis.png")

        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        self.hitbox_zurAula = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zurAula)

        self.text_line_1 = "\t\t cock ass:"
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_4 = "moin moin"
        self.text_line_5 = "und hallo"
        self.text_line_6 = ""

        self.datetime_label = QLabel(self)
        self.datetime_label.setGeometry(622, 642, 180, 40)  # Position und Größe des Labels
        self.datetime_label.setStyleSheet("background-color: lightgray; color: black; font-size: 16px;")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Timer wird alle 1000 Millisekunden (1 Sekunde) ausgelöst

        self.update_datetime()

    def update_datetime(self):
        # Aktuelles Datum und Uhrzeit abrufen und im Label anzeigen
        current_datetime = QDateTime.currentDateTime().toString("dd.MM.yyyy hh:mm:ss")
        self.datetime_label.setText(current_datetime)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(EigenerRaum, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_zurAula.contains(mouse_pos):
            self.new_room.emit("Aula.jpg")
            self.play_sound("TemplateRoom.mp3")

        self.update()