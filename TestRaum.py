# Importieren der notwendigen Module aus PyQt6 für UI-Elemente und Ereignisverarbeitung
from PyQt6.QtCore import QRect, Qt, QDateTime, QTimer
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QLabel, QPushButton

# Importieren einer benutzerdefinierten Klasse TemplateRoom, die als Basis für diesen spezifischen Raum dient
from TemplateRoom import TemplateRoom


# Definition der Klasse TestRaum, die von TemplateRoom erbt
class TestRaum(TemplateRoom):
    def __init__(self, parent=None):
        # Aufruf des Konstruktors der Elternklasse, um die Basisklasseninitialisierung durchzuführen
        super(TestRaum, self).__init__(parent)

        # Initialisierung des Raums mit einem Hintergrundbild
        self.init_room("weis1.png")

        # Festlegen der Position und Größe der Sprechblase
        self.offset_balloon_x = 608
        self.offset_balloon_y = 69
        self.offset_balloon_width = 250
        self.offset_balloon_length = 800

        # Setzen des Offsets für den Mund der Figur in der Sprechblase
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        # Definieren und Hinzufügen der Hitbox zur Aula (Bereich, der auf Klicks reagiert)
        self.hitbox_zurAula = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zurAula)

        # Definieren und Hinzufügen der Hitbox zum Weiterschalten
        self.hitbox_forward = QRect(1094, 200, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        # Initialisierung eines Zählers für den Fortschritt im Text
        self.__counter = 0

        # Definieren der Hitbox für das Easter Egg
        self.hitbox_easter_egg = QRect(740, 410, 35, 35)

        # Initialisierung der Textzeilen
        self.text_line_1 = ""
        self.text_line_2 = "Hallo und herzlich willkommen,"
        self.text_line_3 = "das hier ist ein Testraum"
        self.text_line_4 = "es nervt alles neu anpassen zu müssen"
        self.text_line_5 = ""
        self.text_line_6 = "                         weiter"

    # Überschreiben der Methode, die auf Mausklicks reagiert
    def mousePressEvent(self, ev: QMouseEvent) -> None:
        # Aufruf der Elternklassenmethode
        super(TestRaum, self).mousePressEvent(ev)

        # Ermitteln der Position des Mausklicks
        mouse_pos = ev.pos()

        # Überprüfen, ob die Hitbox für das Easter Egg getroffen wurde
        if self.hitbox_easter_egg.contains(mouse_pos):
            # Setzen der neuen Textzeilen bei Treffer des Easter Eggs
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "GLÜCKWUNSCH!!!"
            self.text_line_4 = "Du hast deine erste Kaffeetasse gefunden."
            self.text_line_5 = ""
            self.text_line_6 = ""

            # Abspielen eines Sounds
            self.play_sound("TemplateRoom.mp3")

            # Aktualisieren des UI
            self.update()

        # Überprüfen, ob die Hitbox zur Aula getroffen wurde
        if self.hitbox_zurAula.contains(mouse_pos):
            # Stoppen des Players (z.B. Musik, Video)
            self.stop_player()

            # Emitten eines Signals, um den Raum zu wechseln
            self.new_room.emit("Aula.jpg")

        # Überprüfen, ob die Hitbox zum Weiterschalten getroffen wurde
        if self.hitbox_forward.contains(mouse_pos):
            # Ändern des Textes basierend auf dem Zählerstand
            if self.__counter == 0:
                self.text_line_1 = ""
                self.text_line_2 = "das hier ist ein weiterer Test"
                self.text_line_3 = "und zwar test nummer 1"
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                # Erhöhen des Zählers
                self.__counter = 1

            elif self.__counter == 1:
                self.text_line_1 = ""
                self.text_line_2 = "das hier ist ein weiterer Test"
                self.text_line_3 = "und zwar test nummer 2"
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                self.__counter = 2

            elif self.__counter == 2:
                self.text_line_1 = ""
                self.text_line_2 = "das hier ist ein weiterer Test"
                self.text_line_3 = "und zwar test nummer 2"
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                self.__counter = 3

            # Aktualisieren des UI
            self.update()
