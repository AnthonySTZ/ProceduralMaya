from PluginLib.CompactQt.Qt import (
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QDoubleValidator,
    QObject,
    SIGNAL,
)


class Float(QObject):
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
        line_edit.textEdited.connect(lambda text: self.setValue(text))
        hbox.addWidget(line_edit)

        return widget

    def setValue(self, value):
        if value == "":
            value = 0
        self.value = float(value)
        self.valueChanged.emit()
