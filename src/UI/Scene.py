from PluginLib.CompactQt.Qt import QGraphicsScene, Qt
from UI.Elements.ConnectionLine import ConnectionLine


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

        if self.createConnection(io_item):
            self.resetSelection()

    def createConnection(self, io_item):

        connection = ConnectionLine()
        res = connection.createConnectionBetweenNodes(self._current_io_item, io_item)
        if res:
            self.addItem(connection)
            print(
                "Connection between "
                + self._current_io_item.getNodeItem().getName()
                + " and "
                + io_item.getNodeItem().getName()
            )
        return res

    def createMouseConnection(self):
        self._temp_connection = ConnectionLine()
        self._temp_connection.createMovableConnectionFromOneNode(self._current_io_item)
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
