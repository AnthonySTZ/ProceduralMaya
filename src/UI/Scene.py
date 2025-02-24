from PluginLib.CompactQt.Qt import QGraphicsScene, Qt
from UI.GraphicsMouseLine import GraphicsMouseLine
from UI.GraphicsConnectionLine import GraphicsConnectionLine


class Scene(QGraphicsScene):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._current_io_item = None
        self._temp_connection = None

    def addNode(self, node):
        self.addItem(node)
        node.ioClicked.connect(self.ioClicked)

    def ioClicked(self, io_item):
        if self._current_io_item is None:  # First Click
            self._current_io_item = io_item
            self.createMouseConnection()
            return

        if (
            self._current_io_item.getType() == io_item.getType()
        ):  # Click on same type as current selected
            print("Same type clicked !")
            return

        # TODO: Create connection between input and output
        self.createConnection(io_item)
        self.resetSelection()

    def createConnection(self, io_item):
        print(
            "Connection between "
            + self._current_io_item.getNodeItem().title_name.toPlainText()
            + " and "
            + io_item.getNodeItem().title_name.toPlainText()
        )

        connection = GraphicsConnectionLine()
        connection.setFirstItem(self._current_io_item)
        connection.setLastItem(io_item)
        connection.updateLine()
        self.addItem(connection)

    def createMouseConnection(self):
        self._temp_connection = GraphicsMouseLine()
        self._temp_connection.setItem(self._current_io_item)
        self.addItem(self._temp_connection)

    def moveEvent(self, mouse_pos):
        if self._temp_connection:
            self._temp_connection.updateMousePos(mouse_pos)

    def resetSelection(self):
        self._current_io_item = None
        self._temp_connection.setParentItem(None)
        self._temp_connection = None

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.resetSelection()
