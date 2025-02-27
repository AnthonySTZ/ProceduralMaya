from PluginLib.CompactQt.Qt import (
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QDoubleValidator,
    SIGNAL,
)
from Core.Field.Field import Field


class Float(Field):
    valueChanged = SIGNAL()

    def __init__(self, value=0.0):
        super().__init__()
        self.value = value

    def getUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(hbox)

        line_edit = QLineEdit(str(self.value))
        line_edit.setValidator(QDoubleValidator())
        line_edit.returnPressed.connect(lambda le=line_edit: self.setValue(le.text()))
        hbox.addWidget(line_edit)

        return widget

    def toStr(self):
        return str(self.value)

    def setValue(self, value):
        try:
            self.value = float(value)
        except:
            self.value = 0
        self.valueChanged.emit()
