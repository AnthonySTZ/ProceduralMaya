from Core.Qt.AQClickableEllipseItem import AQClickableEllipseItem
from PluginLib.CompactQt.Qt import QBrush, QPen, Qt


class IOItem(AQClickableEllipseItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.setBrush(QBrush(Qt.GlobalColor.gray))
        self.setPen(QPen(Qt.GlobalColor.black))
