from PluginLib.CompactQt.Qt import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    Qt,
)


class Parameters(QWidget):
    def __init__(self, scene):
        super().__init__()
        self._scene = scene
        self._node = None
        self.buildUI()

    def buildUI(self):
        self._vbox = QVBoxLayout()
        self._vbox.setSpacing(0)
        self._vbox.setContentsMargins(0, 50, 0, 0)
        self.setLayout(self._vbox)

        self.setMinimumWidth(300)

        self._scene.nodeClicked.connect(self.setNode)

    def setNode(self, node):
        self._node = node
        self.updateParameters()

    def updateParameters(self):
        self.clearParams()

        if self._node is None:
            return

        for param, value in self._node.getParameters().items():
            param_widget = self.createParamWidget(param, value)
            self._vbox.addWidget(param_widget)

        self._vbox.addStretch()

    def createParamWidget(self, param, value):
        hbox = QHBoxLayout()
        widget = QWidget()
        widget.setLayout(hbox)

        label = QLabel(param)
        label.setFixedWidth(100)
        label.setAlignment(Qt.AlignmentFlag.AlignRight)

        line_edit = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(line_edit)

        return widget

    def clearParams(self):
        for i in reversed(range(self._vbox.count())):
            item = self._vbox.itemAt(i)
            self._vbox.removeItem(item)
