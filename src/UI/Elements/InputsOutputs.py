from PluginLib.CompactQt.Qt import QGraphicsObject, QRectF, SIGNAL
from Core.Logic import logics
from UI.Elements.NodeRect import NodeRect
from UI.Elements.IOItem import IOItem


class InputsOutputs(QGraphicsObject):
    INPUT = 0
    OUTPUT = 1
    PADDING = 2

    RADIUS = 9

    clicked = SIGNAL(IOItem)

    def __init__(self, parent, type, amount):
        super().__init__()
        self._rect = QRectF(0, 0, NodeRect.WIDTH, self.RADIUS * 2)
        self.setParentItem(parent)
        self._type = type
        self._amount = amount
        self.buildUI()

    def buildUI(self):
        if self._amount == 0:
            return

        height = 0
        if self._type == self.INPUT:
            height = -self.PADDING - self.RADIUS
        else:
            height = NodeRect.HEIGHT + self.PADDING

        points_offsets = logics.evenly_distribute_point_on_line(
            NodeRect.WIDTH, self._amount
        )
        for index, offset in enumerate(points_offsets):
            io = IOItem(offset, height, self.RADIUS, self.RADIUS)
            io.setUserData("index", index)
            io.setParentItem(self)
            io.clicked.connect(lambda io=io: self.clicked.emit(io))

    def boundingRect(self):
        return self._rect

    def paint(self, painter, option, widget=None):
        return
