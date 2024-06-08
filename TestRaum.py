# Importieren der notwendigen Module aus PyQt6 für UI-Elemente und Ereignisverarbeitung
from PyQt6.QtCore import QRect, Qt, QDateTime, QTimer
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QLabel, QPushButton

# Importieren einer benutzerdefinierten Klasse TemplateRoom, die als Basis für diesen spezifischen Raum dient
from TemplateRoom import TemplateRoom


# Definition der Klasse QrCode, die von TemplateRoom erbt
class TestRaum(TemplateRoom):
    def __init__(self, parent=None):
        # Aufruf des Konstruktors der Elternklasse, um die Basisklasseninitialisierung durchzuführen
        super(TestRaum, self).__init__(parent)

        self.init_room("weis1.png")

        self.offset_balloon_x = 608
        self.offset_balloon_y = 69
        self.offset_balloon_width = 250
        self.offset_balloon_length = 800

        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        self.hitbox_zurAula = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zurAula)

        self.hitbox_forward = QRect(1094, 200, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        self.__counter = 0

        self.hitbox_easter_egg = QRect(740, 410, 35, 35)

        self.text_line_1 = ""
        self.text_line_2 = "Hallo und herzlich willkommen,"
        self.text_line_3 = "das hier ist ein Testraum"
        self.text_line_4 = "es nervt alles neu anpassen zu müssen"
        self.text_line_5 = ""
        self.text_line_6 = "                         weiter"


    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(TestRaum, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_easter_egg.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "GLÜCKWUNSCH!!!"
            self.text_line_4 = "Du hast deine erste Kaffeetasse gefunden."
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.play_sound("TemplateRoom.mp3")

            self.update()

        if self.hitbox_zurAula.contains(mouse_pos):
            self.stop_player()

            self.new_room.emit("Aula.jpg")


        if self.hitbox_forward.contains(mouse_pos):
            if self.__counter == 0:
                self.text_line_1 = ""
                self.text_line_2 = "das hier ist ein weitere Test"
                self.text_line_3 = "und zwar test nummer 1"
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                self.__counter = 1

            elif self.__counter == 1:
                self.text_line_1 = ""
                self.text_line_2 = "das hier ist ein weitere Test"
                self.text_line_3 = "und zwar test nummer 2"
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                self.__counter = 2

            elif self.__counter == 2:
                self.text_line_1 = ""
                self.text_line_2 = "das hier ist ein weitere Test"
                self.text_line_3 = "und zwar test nummer 2"
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                self.__counter = 3

            self.update()


