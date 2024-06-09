def paintEvent(self, a0: QPaintEvent) -> None:
    # Erstellen eines QPainter-Objekts für die Zeichenoperationen
    painter = QPainter(self)

    # Zeichnen des Hintergrundbildes auf der gesamten Oberfläche
    painter.drawPixmap(QPoint(0, 0), self.__background_pixmap)

    # Speichern des aktuellen Stifts (Pen) des Painters
    old_pen = painter.pen()
    # Erstellen eines neuen Stifts (Pen) und Setzen der Eigenschaften
    new_pen = QPen()
    new_pen.setColor(QColor("black"))
    new_pen.setWidth(5)
    painter.setPen(new_pen)

    # Speichern des aktuellen Pinsels (Brush) des Painters
    old_brush = painter.brush()
    # Erstellen eines neuen Pinsels (Brush) und Setzen der Eigenschaften
    new_brush = QBrush()
    new_brush.setColor(QColor("white"))
    new_brush.setStyle(Qt.BrushStyle.Dense2Pattern)
    painter.setBrush(new_brush)

    # Überprüfen, ob die Sprechblase angezeigt werden soll
    if self.__show_speech_bubble:
        # Zeichnen eines abgerundeten Rechtecks für die Sprechblase
        painter.drawRoundedRect(self.offset_balloon_x, self.offset_balloon_y, self.offset_balloon_length,
                                self.offset_balloon_width, 10, 10)

        # Entfernen des Umrisses der Sprechblase
        new_pen.setStyle(Qt.PenStyle.NoPen)
        painter.setPen(new_pen)

        # Zeichnen des Mundes der Figur zur Sprechblase
        painter.drawPolygon(self.mouth_to_speech)
        painter.drawRect(self.mouth_to_speech.at(1).x() + 5, self.mouth_to_speech.at(1).y() - 5,
                         self.mouth_to_speech.at(2).x() - self.mouth_to_speech.at(1).x() - 5, 5)

        # Wiederherstellen des Stils des Stifts
        new_pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(new_pen)

        # Zeichnen der Linien vom Mund zur Sprechblase
        painter.drawLine(self.mouth_to_speech.at(0), self.mouth_to_speech.at(1))
        painter.drawLine(self.mouth_to_speech.at(2), self.mouth_to_speech.at(0))

    # Überprüfen, ob der Exit-Button angezeigt werden soll
    if self.__show_exit_button:
        # Setzen der Farben und Stile für den Stift und Pinsel des Exit-Buttons
        new_pen.setColor(QColor("goldenrod"))
        new_pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(new_pen)
        new_brush.setColor(QColor("gold"))
        painter.setBrush(new_brush)

        # Zeichnen eines abgerundeten Rechtecks für den Exit-Button
        painter.drawRoundedRect(QRect(self.__offset_exit, self.__pos_x_exit, 100, self.__heigth_box), 10, 10)

    # Wiederherstellen der ursprünglichen Pinsel- und Stifteinstellungen
    painter.setBrush(old_brush)
    painter.setPen(old_pen)

    # Setzen der Schriftart und ihrer Eigenschaften für den Text
    font = QFont("Courier", 24)
    font.setBold(True)
    font.setItalic(True)
    painter.setFont(font)
    painter.setPen(QColor("black"))

    # Überprüfen, ob die Sprechblase angezeigt werden soll
    if self.__show_speech_bubble:
        # Zeichnen der Textzeilen in der Sprechblase
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 25, self.text_line_1)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 50, self.text_line_2)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 75, self.text_line_3)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 100, self.text_line_4)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 125, self.text_line_5)
        painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 150, self.text_line_6)

    # Überprüfen, ob der Exit-Button angezeigt werden soll
    if self.__show_exit_button:
        # Zeichnen des Textes auf dem Exit-Button
        painter.drawText(self.__offset_exit + 10, self.__pos_x_exit + 25, "Zurück")

    # Überprüfen, ob die Hitboxen sichtbar sein sollen
    if self.__hitbox_visible:
        # Zeichnen eines roten Kreises an der Position des letzten Mausklicks
        if self.__mouse_pos:
            painter.setPen(QColor("red"))
            painter.drawEllipse(self.__mouse_pos, 10, 10)

        # Zeichnen aller definierten Hitboxen
        for hitbox in self.__hitboxes:
            painter.setPen(QColor("greenyellow"))
            painter.drawRect(hitbox)

        # Zeichnen der Hitbox für das Easter Egg, falls vorhanden
        if self.hitbox_easter_egg:
            painter.setPen(QColor("cyan"))
            painter.drawRect(self.hitbox_easter_egg)
