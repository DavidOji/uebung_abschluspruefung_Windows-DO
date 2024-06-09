from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent
# Importieren der TemplateRoom-Klasse
from TemplateRoom import TemplateRoom


# Definition der Aula-Klasse, die von TemplateRoom erbt
class Aula(TemplateRoom):
    def __init__(self, parent=None):
        # Aufruf des Konstruktors der Elternklasse
        super(Aula, self).__init__(parent)

        # Initialisieren des Raumes mit dem Bild "Aula.jpg"
        self.init_room("Aula.jpg")

        # Setzen der Position und Größe der Sprechblase
        self.offset_balloon_x = 1011
        self.offset_balloon_y = 46
        self.offset_balloon_width = 180
        self.offset_balloon_length = 800

        # Setzen der Position und Größe des Mundes zur Sprechblase
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length,
                              self.offset_balloon_y + self.offset_balloon_width, 0, 0)

        # Initialisieren der Hitboxen für die Verwaltung und den Testraum
        self.hitbox_zurVerwaltung = QRect(1, 1, 600, 1200)
        self.append_hitbox(self.hitbox_zurVerwaltung)

        self.hitbox_zumTestRaum = QRect(2066, 34, 600, 1200)
        self.append_hitbox(self.hitbox_zumTestRaum)

        # Setzen der Anfangstexte der Sprechblase
        self.text_line_1 = "\t\tWegweiser:"
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_4 = "Links: zur Verwaltung"
        self.text_line_5 = "Rechts: zu den Unterrichtsräumen"
        self.text_line_6 = ""

    # Überschreiben des mousePressEvent, um auf Mausklicks zu reagieren
    def mousePressEvent(self, ev: QMouseEvent) -> None:
        # Aufruf der mousePressEvent-Methode der Elternklasse
        super(Aula, self).mousePressEvent(ev)

        # Erfassen der aktuellen Mausposition
        mouse_pos = ev.pos()

        # Überprüfen, ob die Hitbox zur Verwaltung angeklickt wurde
        if self.hitbox_zurVerwaltung.contains(mouse_pos):
            # Emit ein Signal, um den Raum zu wechseln
            self.new_room.emit("weis.png")

        # Überprüfen, ob die Hitbox zum Testraum angeklickt wurde
        if self.hitbox_zumTestRaum.contains(mouse_pos):
            # Emit ein Signal, um den Raum zu wechseln
            self.new_room.emit("weis1.png")

        # Aktualisieren des Widgets nach einem Mausklick
        self.update()
