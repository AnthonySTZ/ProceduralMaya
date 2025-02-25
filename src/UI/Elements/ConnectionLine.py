from PluginLib.CompactQt.Qt import QGraphicsLineItem, QPen, Qt
from UI.Elements.InputsOutputs import InputsOutputs


class ConnectionLine(QGraphicsLineItem):
    def __init__(self):
        super().__init__()
        self.setPen(QPen(Qt.GlobalColor.white))
        self.setZValue(-1)

    def createConnectionBetweenNodes(self, io_item_1, io_item_2):
        """
        Create a connection line between two IO of two Nodes. Update when nodes move.
        """
        if io_item_1.getType() == InputsOutputs.INPUT:
            output_node = io_item_1.getNodeItem().getNode()
            output_index = io_item_1.getUserData("index")
            input_node = io_item_2.getNodeItem().getNode()
            input_index = io_item_2.getUserData("index")
        else:
            input_node = io_item_1.getNodeItem().getNode()
            input_index = io_item_1.getUserData("index")
            output_node = io_item_2.getNodeItem().getNode()
            output_index = io_item_2.getUserData("index")

        print("Top node : " + input_node.getName() + " at index : " + str(input_index))
        print(
            "Bottom node : "
            + output_node.getName()
            + " at index : "
            + str(output_index)
        )

        self._first_item = io_item_1
        self._last_item = io_item_2
        self._first_item.getNodeItem().moved.connect(self.updateWhenNodesMove)
        self._last_item.getNodeItem().moved.connect(self.updateWhenNodesMove)
        self.updateLine(io_item_1.centerPos(), io_item_2.centerPos())

        return True

    def updateWhenNodesMove(self):
        self.updateLine(self._first_item.centerPos(), self._last_item.centerPos())

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
