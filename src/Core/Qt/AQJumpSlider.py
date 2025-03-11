from PluginLib.CompactQt.Qt import QSlider, Qt, SIGNAL


class AQJumpSlider(QSlider):

    userChangedValue = SIGNAL(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setRange(0, 100)
        self._is_pressed = False

    def moveToMouse(self, mouse):
        mouse.accept()
        x = mouse.pos().x()
        value = (self.maximum() - self.minimum()) * x / self.width() + self.minimum()
        self.setValue(int(value))
        self.userChangedValue.emit(int(value))

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self._is_pressed = True
            self.moveToMouse(e)

    def mouseReleaseEvent(self, ev):
        self._is_pressed = False

    def mouseMoveEvent(self, e):
        if self._is_pressed:
            self.moveToMouse(e)
