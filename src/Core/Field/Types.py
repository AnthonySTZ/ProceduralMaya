from PluginLib.CompactQt.Qt import (
    QHBoxLayout,
    QWidget,
    QComboBox,
    QObject,
    SIGNAL,
)


class Types(QObject):
    valueChanged = SIGNAL()

    def __init__(self, current=0, types={}):
        super().__init__()
        self.types = types
        self.current_type = current

    def getUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(hbox)

        combo = QComboBox()
        for key, value in self.types.items():
            combo.addItem(key, value)
        combo.setCurrentText(self.current_type)
        combo.textActivated.connect(lambda text: self.setValue(text))
        hbox.addWidget(combo)

        return widget

    def setValue(self, text):
        self.current_type = text
        self.valueChanged.emit()

    def getValue(self):
        return self.types[self.current_type]
