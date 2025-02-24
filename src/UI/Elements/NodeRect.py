from PluginLib.CompactQt.Qt import QBrush, Qt
from Core.Qt.AQMovableRectItem import AQMovableRectItem


class NodeRect(AQMovableRectItem):
    WIDTH = 90
    HEIGHT = 25

    def __init__(self, parent):
        super().__init__(0, 0, self.WIDTH, self.HEIGHT)
        self.setParentItem(parent)
        self.buildUI()

    def buildUI(self):
        brush = QBrush(Qt.GlobalColor.gray)
        self.setBrush(brush)
