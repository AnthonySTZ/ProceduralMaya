from PluginLib.CompactQt.Qt import QRectF, SIGNAL, QGraphicsObject, QBrush, QPen


class AQClickableEllipseItem(QGraphicsObject):
    clicked = SIGNAL(QGraphicsObject)

    def __init__(self, x, y, width, height):
        super().__init__()
        self._rect = QRectF(x, y, width, height)
        self._brush = QBrush()
        self._pen = QPen()

    def setBrush(self, brush):
        self._brush = brush
        self.update()

    def setPen(self, pen):
        self._pen = pen
        self.update()

    def boundingRect(self):
        return self._rect

    def paint(self, painter, option, widget=None):
        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(self._rect)

    def mousePressEvent(self, event):
        self.clicked.emit(self)
