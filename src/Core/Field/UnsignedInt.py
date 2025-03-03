from PluginLib.CompactQt.Qt import (
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QIntValidator,
    SIGNAL,
)
from Core.Field.Int import Int


class UnsignedInt(Int):
    valueChanged = SIGNAL()

    def __init__(self, value=0):
        super().__init__(value)

    def setValue(self, value):
        try:
            self.value = abs(int(value))
        except:
            self.value = 0
        self.valueChanged.emit()
