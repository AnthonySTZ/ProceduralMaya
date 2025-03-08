from Core.Qt.AQClickableEllipseItem import AQClickableEllipseItem
from PluginLib.CompactQt.Qt import QBrush, QPen, Qt


class IOItem(AQClickableEllipseItem):
    def __init__(self, x, y, width, height, type, node_item):
        super().__init__(x, y, width, height)
        self.setBrush(QBrush(Qt.GlobalColor.gray))
        self.setPen(QPen(Qt.GlobalColor.black))
        self._type = type
        self.connections = []
        self._node_item = node_item

    def getType(self):
        return self._type

    def getNodeItem(self):
        return self._node_item
