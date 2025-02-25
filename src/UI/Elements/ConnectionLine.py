from PluginLib.CompactQt.Qt import QGraphicsLineItem, QPen, Qt


class ConnectionLine(QGraphicsLineItem):
    def __init__(self):
        super().__init__()
        self.setPen(QPen(Qt.GlobalColor.white))
        self.setZValue(-1)

    def createConnectionBetweenNodes(self, io_item_1, io_item_2):
        """
        Create a connection line between two IO of two Nodes. Update when nodes move.
        """
        self._first_item = io_item_1
        self._last_item = io_item_2
        self._first_item.getNodeItem().moved.connect(self.updateWhenNodesMove)
        self._last_item.getNodeItem().moved.connect(self.updateWhenNodesMove)
        self.updateLine(io_item_1.centerPos(), io_item_2.centerPos())

    def updateWhenNodesMove(self):
        self.updateLine(self._first_item.centerPos(), self._last_item.centerPos())

    def createMovableConnectionFromOneNode(self, io_item):
        self._node_item = io_item

    def updateLine(self, pos_1, pos_2):
        self.setLine(
            pos_1.x(),
            pos_1.y(),
            pos_2.x(),
            pos_2.y(),
        )
