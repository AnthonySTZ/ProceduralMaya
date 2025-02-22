from PluginLib.CompactQt.Qt import QGraphicsLineItem


class GraphicsConnectionLine(QGraphicsLineItem):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._first_pos = None
        self._last_pos = None

    def setFirstPoint(self, pos):
        self._first_pos = pos

    def setLastPoint(self, pos):
        self._last_pos = pos

    def updateLine(self):
        if self._first_pos is None or self._last_pos is None:
            raise ValueError("Line pos should not be None")

        self.setLine(
            self._first_pos.x(),
            self._first_pos.y(),
            self._last_pos.x(),
            self._last_pos.y(),
        )
