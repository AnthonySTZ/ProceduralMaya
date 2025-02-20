from PluginLib.CompactQt.Qt import QGraphicsView, QPoint, Qt


class AQGraphicsTransformView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self._is_scrolling = False
        self._scroll_pos = QPoint(0, 0)
        self._prev_scale = 1.0

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self._is_scrolling = True
            self._scroll_pos = event.position()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._is_scrolling:
            new_pos = event.position()
            offset = new_pos - self._scroll_pos
            transform = self.transform()
            self.translate(offset.x() / transform.m11(), offset.y() / transform.m22())
            self._scroll_pos = new_pos
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self._is_scrolling:
            self._is_scrolling = False
        super().mouseReleaseEvent(event)
