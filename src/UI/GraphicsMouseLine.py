from PluginLib.CompactQt.Qt import QGraphicsLineItem, QPen, Qt, QPoint


class GraphicsMouseLine(QGraphicsLineItem):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._item = None
        self._mouse_pos = QPoint(0, 0)
        self.setPen(QPen(Qt.GlobalColor.white))

    def setItem(self, item):
        self._item = item
        self._item.xChanged.connect(self.updateLine)
        self._item.yChanged.connect(self.updateLine)

    def updateLine(self):
        item_pos = self._item.centerPos()
        self.setLine(
            item_pos.x(),
            item_pos.y(),
            self._mouse_pos.x(),
            self._mouse_pos.y(),
        )

    def updateMousePos(self, mouse_pos):
        self._mouse_pos = mouse_pos
        self.updateLine()
