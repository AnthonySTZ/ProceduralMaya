from PluginLib.CompactQt.Qt import (
    QObject,
    SIGNAL,
)


class Field(QObject):

    valueChanged = SIGNAL()

    def __init__(self):
        super().__init__()

    def getUI(self):
        raise NotImplementedError("getUI not implemented")
