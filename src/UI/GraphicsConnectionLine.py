from PluginLib.CompactQt.Qt import QGraphicsLineItem


class GraphicsConnectionLine(QGraphicsLineItem):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._first_item = None
        self._last_item = None

    def setFirstItem(self, item):
        self._first_item = item
        self._first_item.xChanged.connect(self.updateLine)
        self._first_item.yChanged.connect(self.updateLine)

    def setLastItem(self, item):
        self._last_item = item
        self._last_item.xChanged.connect(self.updateLine)
        self._last_item.yChanged.connect(self.updateLine)

    def updateLine(self):
        if self._first_item is None or self._last_item is None:
            print("Line pos should not be None")
            return

        self.setLine(
            self._first_item.x(),
            self._first_item.y(),
            self._last_item.x(),
            self._last_item.y(),
        )
