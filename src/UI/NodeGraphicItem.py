from PluginLib.CompactQt.Qt import QGraphicsItem, QGraphicsRectItem


class NodeGraphicScene(QGraphicsItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        title_rect = QGraphicsRectItem(0, 0, 90, 25)
        title_rect.setParentItem(self)
