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
            try:
                self._scroll_pos = event.position()
            except:
                self._scroll_pos = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._is_scrolling:
            try:
                new_pos = event.position()
            except:
                new_pos = event.pos()
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

    def wheelEvent(self, event):
        zoom_in_factor = 1.25
        zoom_out_factor = 1 / zoom_in_factor

        # Save the scene pos
        try:
            old_pos = self.mapToScene(event.pos())
        except:
            old_pos = self.mapToScene(event.position().toPoint())  # PyQt6

        # Zoom
        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
        else:
            zoom_factor = zoom_out_factor
        self.scale(zoom_factor, zoom_factor)

        # Get the new position
        try:
            new_pos = self.mapToScene(event.pos())
        except:
            new_pos = self.mapToScene(event.position().toPoint())  # PyQt6

        # Move scene to old position
        offset = new_pos - old_pos
        self.translate(offset.x(), offset.y())
