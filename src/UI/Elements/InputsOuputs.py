from PluginLib.CompactQt.Qt import QGraphicsObject
from Core.Qt.AQClickableEllipseItem import AQClickableEllipseItem


class InputsOutputs(QGraphicsObject):
    INPUT = 0
    OUTPUT = 1

    def __init__(self, type, amount, width):
        super().__init__()
        self._type = type
        self._amount = amount
        self._width = width
        self.buildUI()

    def buildUI(self):
        pass
