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
        first_item_pos = self._first_item.centerPos()
        last_item_pos = self._last_item.centerPos()
        self.setLine(
            first_item_pos.x(),
            first_item_pos.y(),
            last_item_pos.x(),
            last_item_pos.y(),
        )
