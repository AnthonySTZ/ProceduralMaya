from PluginLib.CompactQt.Qt import QGraphicsObject, QRectF, SIGNAL
from Core.Logic import logics
from UI.Elements.NodeRect import NodeRect
from UI.Elements.IOItem import IOItem


class InputsOutputs(QGraphicsObject):
    INPUT = 0
    OUTPUT = 1
    PADDING = 2
    PADDING_WIDTH = 10

    RADIUS = 9

    clicked = SIGNAL(IOItem)

    def __init__(self, parent, type, amount, node_item):
        super().__init__()
        self._rect = QRectF(
            0, 0, NodeRect.WIDTH - self.PADDING_WIDTH * 2, self.RADIUS * 2
        )
        self.setParentItem(parent)
        self._type = type
        self._amount = amount
        self._node_item = node_item
        self._ios = []
        self.buildUI()

    def buildUI(self):
        if self._amount == 0:
            return

        height = self.calcHeightByType()

        points_pos_x = self.calcPointsHorizontalPosition()
        for index, pos_x in enumerate(points_pos_x):
            io = self.createIOItem(self.PADDING_WIDTH + pos_x, height)
            io.setUserData("index", index)
            io.setParentItem(self)
            io.clicked.connect(lambda io=io: self.clicked.emit(io))
            self._ios.append(io)

    def createIOItem(self, x, y):
        return IOItem(x, y, self.RADIUS, self.RADIUS, self._type, self._node_item)

    def calcHeightByType(self):
        if self._type == self.INPUT:
            return -self.PADDING - self.RADIUS

        return NodeRect.HEIGHT + self.PADDING

    def calcPointsHorizontalPosition(self):
        line_with = NodeRect.WIDTH - self.PADDING_WIDTH * 2 - self.RADIUS
        return logics.evenly_distribute_point_on_line(line_with, self._amount)

    def getIOs(self):
        return self._ios

    def boundingRect(self):
        return self._rect

    def paint(self, painter, option, widget=None):
        return
