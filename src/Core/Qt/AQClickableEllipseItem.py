from PluginLib.CompactQt.Qt import QRectF, SIGNAL, QGraphicsObject, QBrush, QPen


class AQClickableEllipseItem(QGraphicsObject):
    clicked = SIGNAL(QGraphicsObject)

    def __init__(self, x, y, width, height):
        super().__init__()
        self._rect = QRectF(0, 0, width, height)
        self.setPos(x, y)
        self._brush = QBrush()
        self._pen = QPen()
        self._user_data = {}

    def setUserData(self, key, value):
        self._user_data[key] = value

    def getUserData(self, key):
        return self._user_data[key]

    def setBrush(self, brush):
        self._brush = brush
        self.update()

    def setPen(self, pen):
        self._pen = pen
        self.update()

    def centerPos(self):
        center_local = self._rect.center()
        center_scene = self.mapToScene(center_local)
        return center_scene

    def boundingRect(self):
        return self._rect

    def paint(self, painter, option, widget=None):
        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(self._rect)

    def mousePressEvent(self, event):
        self.clicked.emit(self)
