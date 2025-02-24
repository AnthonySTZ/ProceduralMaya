from PluginLib.CompactQt.Qt import QGraphicsObject


class InputsOutputs(QGraphicsObject):
    INPUT = 0
    OUTPUT = 1

    def __init__(self, type):
        super().__init__()
        self._type = type
        self.buildUI()
