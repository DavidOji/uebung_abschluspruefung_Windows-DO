from PyQt6.QtCore import QPoint, QRect, pyqtSignal, pyqtSlot, QSize, Qt, QUrl
from PyQt6.QtGui import QPixmap, QMouseEvent, QPaintEvent, QPainter, QColor, QFont, QPolygon, QPen, QBrush
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import QLabel

# Definition der TemplateRoom-Klasse, die von QLabel erbt
class TemplateRoom(QLabel):
    # Definition von Signalen
    leave_room = pyqtSignal(str)
    new_room = pyqtSignal(str)
    found_easter_egg = pyqtSignal(str)

    def __init__(self, parent=None):
        # Aufruf des Konstruktors der Elternklasse
        super(TemplateRoom, self).__init__(parent)
        self.__room_name = None
        self.__background_pixmap = None

        # Initialisieren der Attribute
        self.__show_exit_button = True
        self.__show_speech_bubble = True
        self.__size = QSize(1440, 900)
        self.__offset_exit = 20
        self.__heigth_box = 30
        self.__hitboxes = list()
        self.__hitbox_visible = False

        self.text_line_1 = None
        self.text_line_2 = None
        self.text_line_3 = None
        self.text_line_4 = None
        self.text_line_5 = None
        self.text_line_6 = None

        self.__mouse_pos = QPoint()
        self.offset_balloon_length = 500
        self.offset_balloon_width = 150

        self.hitbox_exit = QRect()
        self.append_hitbox(self.hitbox_exit)
        self.hitbox_easter_egg = QRect(0, 0, 0, 0)
        self.mouth_to_speech = QPolygon()

        # Setzen des Cursors und Aktivieren der Mausverfolgung
        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.CrossCursor)

        # Initialisieren des MediaPlayers und AudioOutput
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)

    # Überschreiben des resizeEvent, um die Pixmap zu aktualisieren
    def resizeEvent(self, event):
        self.update_pixmap()
        super().resizeEvent(event)

    # Methode zum Aktualisieren der Pixmap basierend auf der Größe
    def update_pixmap(self):
        if self.__background_pixmap:
            self.scaled_pixmap = self.__background_pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                                                 Qt.TransformationMode.SmoothTransformation)
        self.update()

    # Überschreiben des paintEvent, um eigene Zeichenoperationen durchzuführen
    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        if self.scaled_pixmap:
            painter.drawPixmap(self.rect(), self.scaled_pixmap)

        # Speichern der alten Stifte und Pinsel
        old_pen = painter.pen()
        new_pen = QPen()
        new_pen.setColor(QColor("black"))
        new_pen.setWidth(5)
        painter.setPen(new_pen)

        old_brush = painter.brush()
        new_brush = QBrush()
        new_brush.setColor(QColor("white"))
        new_brush.setStyle(Qt.BrushStyle.Dense2Pattern)
        painter.setBrush(new_brush)

        # Zeichnen der Sprechblase, falls aktiviert
        if self.__show_speech_bubble:
            painter.drawRoundedRect(self.offset_balloon_x, self.offset_balloon_y, self.offset_balloon_length,
                                    self.offset_balloon_width, 10, 10)

            new_pen.setStyle(Qt.PenStyle.NoPen)
            painter.setPen(new_pen)

            painter.drawPolygon(self.mouth_to_speech)
            painter.drawRect(self.mouth_to_speech.at(1).x() + 5, self.mouth_to_speech.at(1).y() - 5,
                             self.mouth_to_speech.at(2).x() - self.mouth_to_speech.at(1).x() - 5, 5)

            new_pen.setStyle(Qt.PenStyle.SolidLine)
            painter.setPen(new_pen)

            painter.drawLine(self.mouth_to_speech.at(0), self.mouth_to_speech.at(1))
            painter.drawLine(self.mouth_to_speech.at(2), self.mouth_to_speech.at(0))

        # Zeichnen des Exit-Buttons, falls aktiviert
        if self.__show_exit_button:
            new_pen.setColor(QColor("goldenrod"))
            new_pen.setStyle(Qt.PenStyle.SolidLine)
            painter.setPen(new_pen)
            new_brush.setColor(QColor("gold"))
            painter.setBrush(new_brush)

            painter.drawRoundedRect(QRect(45, 1316, 130, self.__heigth_box), 10, 10)

        # Wiederherstellen der alten Pinsel und Stifte
        painter.setBrush(old_brush)
        painter.setPen(old_pen)

        font = QFont("Courier", 24)
        font.setBold(True)
        font.setItalic(True)
        painter.setFont(font)
        painter.setPen(QColor("black"))

        # Zeichnen des Texts in der Sprechblase, falls aktiviert
        if self.__show_speech_bubble:
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 25, self.text_line_1)
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 50, self.text_line_2)
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 75, self.text_line_3)
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 100, self.text_line_4)
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 125, self.text_line_5)
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 150, self.text_line_6)

        # Zeichnen des Texts auf dem Exit-Button, falls aktiviert
        if self.__show_exit_button:
            painter.drawText(49, 1344, "Zurück")

        # Zeichnen der Hitboxen und der Mausposition, falls sichtbar
        if self.__hitbox_visible:
            if self.__mouse_pos:
                painter.setPen(QColor("red"))
                painter.drawEllipse(self.__mouse_pos, 10, 10)

            for hitbox in self.__hitboxes:
                painter.setPen(QColor("greenyellow"))
                painter.drawRect(hitbox)

            if self.hitbox_easter_egg:
                painter.setPen(QColor("cyan"))
                painter.drawRect(self.hitbox_easter_egg)

    # Überschreiben des mouseMoveEvent, um den Cursor je nach Hitbox zu ändern
    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        for hitbox in self.__hitboxes:
            if hitbox.contains(ev.pos()):
                if self.cursor().shape() != Qt.CursorShape.PointingHandCursor:
                    self.setCursor(Qt.CursorShape.PointingHandCursor)
                return

        if self.hitbox_easter_egg.contains(ev.pos()):
            if self.cursor().shape() != Qt.CursorShape.PointingHandCursor:
                self.setCursor(Qt.CursorShape.PointingHandCursor)
            return

        if self.cursor().shape() != Qt.CursorShape.CrossCursor:
            self.setCursor(Qt.CursorShape.CrossCursor)

    # Überschreiben des mousePressEvent, um auf Mausklicks zu reagieren
    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.__mouse_pos = ev.pos()

        print(ev.pos())

        if self.hitbox_exit.contains(self.__mouse_pos):
            self.stop_player()
            self.leave_room.emit(self.__room_name)
        elif self.hitbox_easter_egg.contains(self.__mouse_pos):
            self.found_easter_egg.emit(self.__room_name)

        self.update()

    # Slot zum Setzen der Sichtbarkeit der Hitboxen
    @pyqtSlot(bool)
    def setHitBoxVisible(self, visible: bool):
        self.__hitbox_visible = visible
        self.update()

    # Initialisieren des Raumes
    def init_room(self, room_name):
        self.__room_name = room_name
        self.__background_pixmap = QPixmap(self.__room_name).scaled(self.__size.width(), self.__size.height())
        self.__pos_x_exit = self.__size.height() - self.__offset_exit - self.__heigth_box - 30
        self.hitbox_exit = QRect(51, 1319, 100, 30)

    # Methode zum Hinzufügen von Hitboxen
    def append_hitbox(self, hitbox):
        self.__hitboxes.append(hitbox)

    # Setzen der Position und Größe des Mundes zur Sprechblase
    def set_offset_mouth(self, x, y, offset_x, width):
        self.mouth_to_speech.clear()
        self.mouth_to_speech.append(QPoint(x, y))
        self.mouth_to_speech.append(QPoint(self.offset_balloon_x + self.offset_balloon_width + offset_x,
                                           self.offset_balloon_y + self.offset_balloon_width))
        self.mouth_to_speech.append(QPoint(self.offset_balloon_x + self.offset_balloon_width + offset_x + width,
                                           self.offset_balloon_y + self.offset_balloon_width))

    # Anzeigen des Exit-Buttons
    def show_exit_button(self, visible):
        self.__show_exit_button = visible

    # Anzeigen der Sprechblase
    def show_speech_bubble(self, visible):
        self.__show_speech_bubble = visible

    # Abspielen eines Sounds
    def play_sound(self, source_path):
        if not self.player.isPlaying():
            self.player.setSource(QUrl.fromLocalFile(source_path))
            self.audioOutput.setVolume(50)
            self.player.play()

    # Stoppen des Players
    def stop_player(self):
        if self.player.isPlaying():
            self.player.stop()
