from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent
from TemplateRoom import TemplateRoom


class Aula(TemplateRoom):
    def __init__(self, parent=None):
        super(Aula, self).__init__(parent)

        self.init_room("Aula.jpg")

        self.offset_balloon_x = 1011
        self.offset_balloon_y = 46
        self.offset_balloon_width = 180
        self.offset_balloon_length = 800

        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        self.hitbox_zurVerwaltung = QRect(1, 1, 600, 1200)
        self.append_hitbox(self.hitbox_zurVerwaltung)

        self.hitbox_zumTestRaum = QRect(2066, 34, 600, 1200)
        self.append_hitbox(self.hitbox_zumTestRaum)


        self.text_line_1 = "\t\tWegweiser:"
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_4 = "Links: zur Verwaltung"
        self.text_line_5 = "Rechts: zu den Unterrichtsräumen"
        self.text_line_6 = ""

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Aula, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_zurVerwaltung.contains(mouse_pos):
            self.new_room.emit("weis.png")

        if self.hitbox_zumTestRaum.contains(mouse_pos):
            self.new_room.emit("weis1.png")

        self.update()