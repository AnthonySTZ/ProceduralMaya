from PluginLib.CompactQt.Qt import QGraphicsScene
from UI.GraphicsConnectionLine import GraphicsConnectionLine
from UI.IOItem import IOItem


class NodesGraphicsScene(QGraphicsScene):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._current_io = None

    def addNode(self, node):
        self.addItem(node)
        node.ioClicked.connect(lambda io_item: self.ioClicked(io_item))

    def ioClicked(self, io_item):
        print(io_item.getNodeItem())
        print(io_item.getType())

        if self._current_io is None:  # First Click
            self._current_io = io_item
            return

        if (
            self._current_io.getType() == io_item.getType()
        ):  # Click on same type as current selected
            return

        # TODO: Create connection between input and output
        print(
            "Connection between "
            + io_item.getNodeItem().title_name.toPlainText()
            + " and "
            + io_item.getNodeItem().title_name.toPlainText()
        )

    def createConnection(self):
        self._current_connection = GraphicsConnectionLine()
        self.addItem(self._current_connection)
