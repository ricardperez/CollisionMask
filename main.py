from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QPoint, QRectF
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem, QApplication
from main_window import Ui_MainWindow
from view.draw_widget import DrawWidget
from view import drawer
from view_controller.mouse_drag import MouseDrag

import sys


class AppWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._mouse_span = MouseDrag()

        self._draw_widget = DrawWidget(self.ui.centralwidget)
        self._draw_widget.setObjectName("draw-widget")
        self.ui.verticalLayout.addWidget(self._draw_widget)

        guidelines = drawer.GuidelinesDrawer(self._mouse_span)
        self._draw_widget.add_draw_element(guidelines)

    def mouseReleaseEvent(self, mouse_event):
        print("MouseReleaseEvent {}".format(mouse_event))
        return super().mouseReleaseEvent(mouse_event)

    def mouseMoveEvent(self, mouse_event):
        print("MouseMoveEvent {}".format(mouse_event))
        return super().mouseMoveEvent(mouse_event)

    def keyPressEvent(self, key_event):
        print("KeyPressEvent {}".format(key_event))
        return super().keyPressEvent(key_event)

    def keyReleaseEvent(self, key_event):
        print("KeyReleaseEvent {}".format(key_event))
        return super().keyReleaseEvent(key_event)


if __name__ == "__main__":
    print("Hellp World")
    app = QtWidgets.QApplication(sys.argv)
    mainWin = AppWindow()
    mainWin.show()
    sys.exit(app.exec_())


