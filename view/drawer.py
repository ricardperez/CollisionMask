from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5 import QtCore
from PyQt5.Qt import QRectF

class Drawer(object):
    def paint_event(self, draw_widget, paint_event):
        raise Exception("paint_event() must be overridden")


class GuidelinesDrawer(Drawer):
    def __init__(self, drag_mouse):
        super().__init__()
        self._drag_mouse = drag_mouse

    def paint_event(self, draw_widget, paint_event):
        painter = QPainter()
        painter.begin(draw_widget)
        pen = QPen(QtCore.Qt.black, 3)
        painter.setPen(pen)

        offset = self._drag_mouse.total_offset()

        width = paint_event.rect().width()
        height = paint_event.rect().height()
        half_width = width * 0.5 + offset.x()
        half_height = height * 0.5 + offset.y()

        painter.drawLine(half_width, 0, half_width, height)
        painter.drawLine(0, half_height, width, half_height)

        painter.setPen(QPen(QtCore.Qt.black, 1))
        separation = 25
        n_vertical_left = int(half_width / separation)
        for i in range(1, n_vertical_left+1):
            x = half_width - separation * i
            painter.drawLine(x, 0, x, height)
        n_vertical_right = int((width - half_width) / separation)
        for i in range(1, n_vertical_right+1):
            x = half_width + separation * i
            painter.drawLine(x, 0, x, height)

        n_horizontal_top = int(half_height / separation)
        for i in range(1, n_horizontal_top+1):
            y = half_height - separation * i
            painter.drawLine(0, y, width, y)
        n_horizontal_bottom = int((height - half_height) / separation)
        for i in range(1, n_horizontal_bottom+1):
            y = half_height + separation * i
            painter.drawLine(0, y, width, y)
        painter.end()


class SelectionDrawer(Drawer):
    def __init__(self, transformations, mouse_drag):
        super().__init__()
        self._transformations = transformations
        self._mouse_drag = mouse_drag

    def paint_event(self, draw_widget, paint_event):
        if self._mouse_drag.is_started():
            painter = QPainter()
            painter.begin(draw_widget)
            pen = QPen(QtCore.Qt.white, 1)
            painter.setPen(pen)
            rect = self._transformations.rect_to_screen(QRectF(self._mouse_drag.start_position(), self._mouse_drag.end_position()))
            painter.drawRect(rect)
            painter.fillRect(rect, QColor(255, 255, 255, 85))
            painter.end()

