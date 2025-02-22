from PluginLib.CompactQt.Qt import QGraphicsScene
from UI.GraphicsConnectionLine import GraphicsConnectionLine


class NodesGraphicsScene(QGraphicsScene):

    INPUT = 0
    OUTPUT = 1

    def __init__(self, parent=None):
        super().__init__(parent)
        self._selecting = None
        self._io_selected = None
        self._selected_node = None
        self._current_connection = None

    def addNode(self, node):
        self.addItem(node)
        node.inputClicked.connect(lambda input: self.inputClicked(node, input))
        node.outputClicked.connect(
            lambda item: print(
                "Output index " + str(item.getUserData("index")) + " clicked"
            )
        )

    def inputClicked(self, node_item, input):
        print(node_item)
        self.ioClicked(node_item, input, self.INPUT)

    def ioClicked(self, node_item, io, iotype):
        if self._selecting == iotype:  # Cannot link io type to the same type
            self._current_connection.setParentItem(None)
            self._current_connection = None
            self._selecting = None
            return

        if self._selecting is None:  # First click on io
            self.createConnection()
            self._selecting = iotype
            self._selected_node = node_item
            self._current_connection.setFirstItem(io)
            return

        self._current_connection.setLastItem(io)

    def createConnection(self):
        self._current_connection = GraphicsConnectionLine()
        self.addItem(self._current_connection)
