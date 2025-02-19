from PluginLib.CompactQt.Qt import QGraphicsItem


class NodesGraphicScene(QGraphicsItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        pass
