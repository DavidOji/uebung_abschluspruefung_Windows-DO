from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QMouseEvent, QPainter

# Importieren der TemplateRoom-Klasse
from TemplateRoom import TemplateRoom

# Definition der Eingang-Klasse, die von TemplateRoom erbt
class Eingang(TemplateRoom):
    def __init__(self, parent=None):
        # Aufruf des Konstruktors der Elternklasse
        super(Eingang, self).__init__(parent)
        # Deaktivieren des Exit-Buttons
        self.show_exit_button(False)

        # Initialisieren des Raumes mit dem Bild "Eingang.jpg"
        self.init_room("Eingang.jpg")

        # Setzen der Position und Größe der Sprechblase
        self.offset_balloon_x = 641
        self.offset_balloon_y = 16
        self.offset_balloon_width = 180
        self.offset_balloon_length = 800

        # Setzen der Position und Größe des Mundes zur Sprechblase
        self.set_offset_mouth(1292, 411, 50, 150)

        # Initialisieren der Hitboxen für die Türen und das Vorwärtsgehen
        self.hitbox_door_1 = QRect(15, 12, 600, 1200)
        self.append_hitbox(self.hitbox_door_1)

        self.hitbox_door_2 = QRect(2040, 94, 600, 1200)
        self.append_hitbox(self.hitbox_door_2)

        self.hitbox_forward = QRect(1135, 146, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        # Initialisieren der Hitbox für das Easter Egg
        self.__counter = 0
        self.hitbox_easter_egg = QRect(740, 410, 35, 35)

        # Setzen der Anfangstexte der Sprechblase
        self.text_line_1 = ""
        self.text_line_2 = "Hallo und herzlich willkommen,"
        self.text_line_3 = "zum Tag der offenen Tür am 16. März 2024"
        self.text_line_4 = "im SBS Herzogenaurach."
        self.text_line_5 = ""
        self.text_line_6 = "                         weiter"

    # Überschreiben des mousePressEvent, um auf Mausklicks zu reagieren
    def mousePressEvent(self, ev: QMouseEvent) -> None:
        # Aufruf der mousePressEvent-Methode der Elternklasse
        super(Eingang, self).mousePressEvent(ev)

        # Erfassen der aktuellen Mausposition
        mouse_pos = ev.pos()

        # Überprüfen, ob das Easter Egg angeklickt wurde
        if self.hitbox_easter_egg.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "GLÜCKWUNSCH!!!"
            self.text_line_4 = "Du hast deine erste Kaffeetasse gefunden."
            self.text_line_5 = ""
            self.text_line_6 = ""

            # Abspielen des Sounds
            self.play_sound("TemplateRoom.mp3")

            # Aktualisieren des Widgets
            self.update()

        # Überprüfen, ob eine der Türen angeklickt wurde
        if self.hitbox_door_1.contains(mouse_pos) or self.hitbox_door_2.contains(mouse_pos):
            self.stop_player()
            self.new_room.emit("Aula.jpg")

        # Überprüfen, ob der Vorwärts-Button angeklickt wurde
        if self.hitbox_forward.contains(mouse_pos):
            if self.__counter == 0:
                self.text_line_1 = ""
                self.text_line_2 = "Ich heiße David Ojimba"
                self.text_line_3 = "und begleite dich heute"
                self.text_line_4 = "durch unsere Schule."
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                self.__counter = 1

            elif self.__counter == 1:
                self.text_line_1 = "Hier ist unser Point & Click Adventure."
                self.text_line_2 = "Wir haben es für dich erstellt,"
                self.text_line_3 = "um dir einen Einblick in unsere"
                self.text_line_4 = "verschiedenen Fachschulen zu geben."
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                self.__counter = 2

            elif self.__counter == 2:
                self.text_line_1 = ""
                self.text_line_2 = "Die grünen Hitboxen zeigen dir an,"
                self.text_line_3 = "worauf du klicken kannst."
                self.text_line_4 = "Falls du Fragen hast melde "
                self.text_line_5 = "dich gerne bei uns."
                self.text_line_6 = "                         weiter"

                self.__counter = 3

            elif self.__counter == 3:
                self.text_line_1 = "In manchen Räumen ist eine Tasse versteckt."
                self.text_line_2 = ""
                self.text_line_3 = "Gehe von Raum zu Raum,"
                self.text_line_4 = "denn am Ende hast du die Chance"
                self.text_line_5 = "eine Kaffeetasse zu gewinnen."
                self.text_line_6 = "                         weiter"

                self.__counter = 4

            elif self.__counter == 4:
                self.text_line_1 = ""
                self.text_line_2 = ""
                self.text_line_3 = "Naaa, hast du schon"
                self.text_line_4 = "eine Tasse entdeckt?"
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                self.__counter = 5

            elif self.__counter == 5:
                self.text_line_1 = ""
                self.text_line_2 = ""
                self.text_line_3 = "Besuche jede Raum"
                self.text_line_4 = "und finde die Tassen!."
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                self.__counter = 6

            elif self.__counter == 6:
                self.text_line_1 = ""
                self.text_line_2 = ""
                self.text_line_3 = ""
                self.text_line_4 = "Viel Spaß bei der Suche!"
                self.text_line_5 = ""
                self.text_line_6 = ""

            # Aktualisieren des Widgets nach dem Ändern des Textes
            self.update()
