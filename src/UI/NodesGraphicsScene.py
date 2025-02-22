from PluginLib.CompactQt.Qt import QGraphicsScene
from UI.GraphicsConnectionLine import GraphicsConnectionLine


class NodesGraphicsScene(QGraphicsScene):

    INPUT = 0
    OUTPUT = 1

    def __init__(self, parent=None):
        super().__init__(parent)
        self._selecting = None
        self._io_selected = None

    def addNode(self, node):
        self.addItem(node)
        node.inputClicked.connect(self.inputClicked)
        node.outputClicked.connect(
            lambda item: print(
                "Output index " + str(item.getUserData("index")) + " clicked"
            )
        )

    def inputClicked(self, input):
        if self._selecting == self.INPUT:  # Cannot link input to another input
            self._selecting = None
            return

        if self._selecting is None:  # First click on an input
            self._selecting = self.INPUT
            self._io_selected = input
            print("Selected Input")
            return
