from PluginLib.CompactQt.Qt import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    Qt,
    QDoubleValidator,
    QIntValidator,
)

from Core.Field.Float import Float
from Core.Field.Float3 import Float3
from Core.Field.Int import Int


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
        hbox.setSpacing(10)
        widget = QWidget()
        widget.setLayout(hbox)

        label = QLabel(param)
        label.setFixedWidth(100)
        label.setAlignment(Qt.AlignmentFlag.AlignRight)

        parameters_edit = value.getUI()

        hbox.addWidget(label)
        hbox.addWidget(parameters_edit)

        return widget

    def clearParams(self):
        for i in reversed(range(self._vbox.count())):
            item = self._vbox.itemAt(i)
            self._vbox.removeItem(item)
