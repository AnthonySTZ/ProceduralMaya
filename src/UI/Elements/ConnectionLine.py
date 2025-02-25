from PluginLib.CompactQt.Qt import QGraphicsLineItem, QPen, Qt


class ConnectionLine(QGraphicsLineItem):
    def __init__(self):
        super().__init__()
        self.setPen(QPen(Qt.GlobalColor.white))
        self.setZValue(-1)

    def createConnectionBetweenNodes(self, io_item_1, io_item_2):
        self._first_item = io_item_1
        self._last_item = io_item_2

    def createMovableConnectionFromOneNode(self, io_item):
        self._node_item = io_item

    def updateLine(self, pos_1, pos_2):
        self.setLine(
            pos_1.x(),
            pos_1.y(),
            pos_2.x(),
            pos_2.y(),
        )
