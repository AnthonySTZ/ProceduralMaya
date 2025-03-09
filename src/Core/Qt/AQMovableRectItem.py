from PluginLib.CompactQt.Qt import (
    QPen,
    SIGNAL,
    QBrush,
    QRectF,
    QGraphicsObject,
    QGraphicsItem,
    QPainter,
    QPainterPath,
)


class AQMovableRectItem(QGraphicsObject):
    moved = SIGNAL()
    clicked = SIGNAL()

    def __init__(self, x, y, width, height):
        super().__init__()
        self._rect = QRectF(0, 0, width, height)
        self.setPos(x, y)
        self._brush = QBrush()
        self._pen = QPen()
        self._user_data = {}
        self.setFlags(
            QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges
            | QGraphicsItem.GraphicsItemFlag.ItemIsMovable
        )

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

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        painter.setPen(self._pen)
        painter.setBrush(self._brush)

        path.addRoundedRect(self._rect, 4, 4)
        painter.setClipPath(path)
        painter.fillPath(path, painter.brush())
        painter.strokePath(path, painter.pen())

    def itemChange(self, change, value):
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionChange:
            self.moved.emit()
        return super().itemChange(change, value)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)
