from PluginLib.CompactQt.Qt import QGraphicsObject, QRectF
from Core.Logic import logics
from Core.Qt.AQClickableEllipseItem import AQClickableEllipseItem


class InputsOutputs(QGraphicsObject):
    INPUT = 0
    OUTPUT = 1

    RADIUS = 9

    def __init__(self, type, amount, width):
        super().__init__()
        self._rect = QRectF(0, 0, width, self.RADIUS * 2)
        self._type = type
        self._amount = amount
        self._width = width
        self.buildUI()

    def buildUI(self):
        points_offsets = logics.evenly_distribute_point_on_line(
            self._width, self._amount
        )

    def boundingRect(self):
        return self._rect

    def paint(self, painter, option, widget=None):
        return
