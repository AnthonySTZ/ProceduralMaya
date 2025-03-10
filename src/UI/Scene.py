from PluginLib.CompactQt.Qt import QGraphicsScene, Qt, QPen, QColor, SIGNAL
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

    def buildGrid(self):
        self.createGrid(20, Qt.GlobalColor.gray, 0.15)
        self.createGrid(200, QColor(10, 10, 10), 1.2)

    def createGrid(self, size, color, thickess):
        pen = QPen(color, thickess)
        pen.setCosmetic(True)
        for x in range(0, int(self.width()), size):
            line = self.addLine(x, 0, x, int(self.height()), pen)
            line.setZValue(-50)
        for y in range(0, int(self.height()), size):
            self.addLine(0, y, int(self.width()), y, pen)
            line.setZValue(-50)

    def addNodeItem(self, node_item):
        self.addItem(node_item)
        self._node_items.append(node_item)
        self._node_scene.addNode(node_item.getNode())
        node_item.ioClicked.connect(self.ioClicked)
        node_item.nodeClicked.connect(self.selectNode)

    def selectNode(self, node_item):
        self.nodeClicked.emit(node_item.getNode())
        if self._current_selected_node is not None:
            self._current_selected_node.setSelected(False)
        self._current_selected_node = node_item
        self._current_selected_node.setSelected(True)

    def nodeScene(self):
        return self._node_scene

    def ioClicked(self, io_item):
        if self._current_io_item is None:  # First Click
            self._current_io_item = io_item
            self.createMouseConnection()
            return

        # Click on same type as current selected
        if self._current_io_item.getType() == io_item.getType():
            return

        if self.createConnection(io_item):
            self._node_scene.update()
            self.resetSelection()

    def createConnection(self, io_item):

        connection = ConnectionLine(self._node_scene)
        res = connection.createConnectionBetweenNodes(self._current_io_item, io_item)
        if res:
            self.addItem(connection)

        return res

    def createMouseConnection(self):
        self._temp_connection = ConnectionLine(self._node_scene)
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
        elif event.key() == Qt.Key.Key_Delete:
            self.deleteCurrentNode()

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

    def deleteCurrentNode(self):
        if self._current_selected_node is None:
            return
        print("Delete : " + self._current_selected_node.getNode().getName())
        self._node_scene.deleteNode(self._current_selected_node.getNode())
        self._node_items.remove(self._current_selected_node)
        self._current_selected_node.delete()

    def getNodeScene(self):
        return self._node_scene
