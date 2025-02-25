from PluginLib.CompactQt.Qt import QGraphicsLineItem, QPen, Qt
from UI.Elements.InputsOutputs import InputsOutputs


class ConnectionLine(QGraphicsLineItem):
    def __init__(self):
        super().__init__()
        self.setPen(QPen(Qt.GlobalColor.white))
        self.setZValue(-1)
        self._node_item = None

    def createConnectionBetweenNodes(self, io_item_1, io_item_2):
        """
        Create a connection line between two IO of two Nodes. Update when nodes move.
        """

        self.defineInputAndOutputNodes(io_item_1, io_item_2)

        # Input of the outputNode already connected
        if self._output_node.input(self._output_index) is not None:
            return False

        self._output_node.setInput(
            self._output_index, self._input_node, self._input_index
        )

        self.showConnectionInfos()
        self._input_io.getNodeItem().moved.connect(self.updateWhenNodesMove)
        self._output_io.getNodeItem().moved.connect(self.updateWhenNodesMove)
        self.updateLine(io_item_1.centerPos(), io_item_2.centerPos())

        return True

    def defineInputAndOutputNodes(self, io_item_1, io_item_2):
        if io_item_1.getType() == InputsOutputs.INPUT:
            self._input_io = io_item_2
            self._output_io = io_item_1
        else:
            self._input_io = io_item_1
            self._output_io = io_item_2

        self._input_node = self._input_io.getNodeItem().getNode()
        self._input_index = self._input_io.getUserData("index")
        self._output_node = self._output_io.getNodeItem().getNode()
        self._output_index = self._output_io.getUserData("index")

    def showConnectionInfos(self):

        print(
            "Top node : "
            + self._input_node.getName()
            + " at index : "
            + str(self._input_index)
        )
        print(
            "Bottom node : "
            + self._output_node.getName()
            + " at index : "
            + str(self._output_index)
        )

    def updateWhenNodesMove(self):
        self.updateLine(self._input_io.centerPos(), self._output_io.centerPos())

    def createMovableConnectionFromOneNode(self, io_item):
        self._node_item = io_item

    def updateMousePos(self, mouse_pos):
        if self._node_item:
            self._mouse_pos = mouse_pos
            self.updateLine(self._node_item.centerPos(), mouse_pos)

    def updateLine(self, pos_1, pos_2):
        self.setLine(
            pos_1.x(),
            pos_1.y(),
            pos_2.x(),
            pos_2.y(),
        )

    def deleteConnection(self):
        print("Delete Connection")
        self._output_node.setInput(self._output_index, None)
        self.setParentItem(None)

    def mousePressEvent(self, event):
        if self._node_item is not None:
            return

        if event.button() == Qt.MouseButton.LeftButton:
            self.deleteConnection()
