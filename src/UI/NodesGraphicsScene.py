from PluginLib.CompactQt.Qt import QGraphicsScene


class NodesGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

    def addNode(self, node):
        self.addItem(node)
        node.inputClicked.connect(
            lambda item: print(
                "Input index " + str(item.getUserData("index")) + " clicked"
            )
        )
        node.outputClicked.connect(
            lambda item: print(
                "Output index " + str(item.getUserData("index")) + " clicked"
            )
        )
