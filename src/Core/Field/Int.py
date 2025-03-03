from PluginLib.CompactQt.Qt import (
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QIntValidator,
    SIGNAL,
)
from Core.Field.Field import Field


class Int(Field):
    valueChanged = SIGNAL()

    def __init__(self, value=0, signed=True):
        super().__init__()
        self.value = value
        self.signed = signed

    def getUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(hbox)

        line_edit = QLineEdit(str(self.value))
        line_edit.setValidator(QIntValidator())
        line_edit.returnPressed.connect(lambda le=line_edit: self.setValue(le.text()))
        hbox.addWidget(line_edit)

        return widget

    def toStr(self):
        return str(self.value)

    def setValue(self, value):
        try:
            self.value = int(value)
            if self.signed:
                self.value = abs(value)
        except:
            self.value = 0
        self.valueChanged.emit()
