from PluginLib.CompactQt.Qt import QGraphicsObject


class InputOutput(QGraphicsObject):
    INPUT = 0
    OUTPUT = 1

    def __init__(self, type):
        super().__init__()
        self._type = type
