from PluginLib.CompactQt.Qt import QGraphicsScene, Qt, SIGNAL
from UI.Elements.ConnectionLine import ConnectionLine
from Core.Nodes.Scene import Scene as NodeScene
from Core.Nodes.BaseNode import BaseNode


class Scene(QGraphicsScene):

    nodeClicked = SIGNAL(BaseNode)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._node_scene = NodeScene()
        self._node_items = []
        self._current_io_item = None
        self._temp_connection = None
        self._current_selected_node = None

    def addNodeItem(self, node_item):
        self.addItem(node_item)
        self._node_items.append(node_item)
        self._node_scene.addNode(node_item.getNode())
        node_item.updateName()
        node_item.ioClicked.connect(self.ioClicked)
        node_item.nodeClicked.connect(self.selectNode)

    def selectNode(self, node_item):
        self.nodeClicked.emit(node_item.getNode())
        self._current_selected_node = node_item

    def nodeScene(self):
        return self._node_scene

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
            self._node_scene.update()
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
        if self._temp_connection:
            self._temp_connection.setParentItem(None)
        self._temp_connection = None

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.resetSelection()
        elif event.key() == Qt.Key.Key_R:
            self.renderCurrentNode()

    def renderCurrentNode(self):
        if self._current_selected_node is None:
            return

        self._current_selected_node.setRender(True)
        self.setRenderTo(self._current_selected_node)

    def setRenderTo(self, node_item):
        for node in self._node_items:
            if node_item != node:
                node.setRender(False)
        self._node_scene.setRenderNode(node_item.getNode())

    def updateCurrentRender(self):
        self._node_scene.update()
