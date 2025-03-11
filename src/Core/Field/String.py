from PluginLib.CompactQt.Qt import (
    QHBoxLayout,
    QWidget,
    SIGNAL,
)
from Core.Field.Field import Field
from Core.Qt.AQDefocusLineEdit import AQDefocusLineEdit


class String(Field):
    valueChanged = SIGNAL()

    def __init__(self, value=""):
        super().__init__()
        self.value = value

    def getUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(hbox)

        line_edit = AQDefocusLineEdit(str(self.value))
        line_edit.returnPressed.connect(lambda le=line_edit: self.userChangedValue(le))
        line_edit.defocus.connect(lambda le=line_edit: self.userChangedValue(le))
        hbox.addWidget(line_edit)

        return widget

    def userChangedValue(self, line_edit):
        self.setValue(line_edit.text())

    def setValue(self, value):
        self.value = str(value)
        self.valueChanged.emit()
