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
        node.ioClicked.connect(lambda io_item: self.ioClicked(io_item))

    def ioClicked(self, io_item):
        print(io_item.getNodeItem())
        print(io_item.getType())

    def createConnection(self):
        self._current_connection = GraphicsConnectionLine()
        self.addItem(self._current_connection)
