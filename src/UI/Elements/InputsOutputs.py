from PluginLib.CompactQt.Qt import QGraphicsObject, QRectF, QPen, QBrush, Qt
from Core.Logic import logics
from Core.Qt.AQClickableEllipseItem import AQClickableEllipseItem
from UI.Elements.NodeRect import NodeRect


class InputsOutputs(QGraphicsObject):
    INPUT = 0
    OUTPUT = 1
    PADDING = 2

    RADIUS = 9

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
        for offset in points_offsets:
            ellipse = AQClickableEllipseItem(offset, height, self.RADIUS, self.RADIUS)
            ellipse.setBrush(QBrush(Qt.GlobalColor.gray))
            ellipse.setPen(QPen(Qt.GlobalColor.black))
            ellipse.setParentItem(self)

    def boundingRect(self):
        return self._rect

    def paint(self, painter, option, widget=None):
        return
