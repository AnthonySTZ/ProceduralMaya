from PluginLib.CompactQt.Qt import QWidget, QVBoxLayout, QLabel, Qt


class Parameters(QWidget):
    def __init__(self, scene):
        super().__init__()
        self._scene = scene
        self._node = None
        self.buildUI()

    def buildUI(self):
        self._hbox = QVBoxLayout()
        self._hbox.setSpacing(0)
        self._hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._hbox)

        self.setMinimumWidth(200)
        self.setStyleSheet(
            """
            QWidget {
                background-color: #4d4d4d;
            }
            """
        )

        self._scene.nodeClicked.connect(self.setNode)

    def setNode(self, node):
        self._node = node
        self.updateParameters()

    def updateParameters(self):
        self.clearParams()

        if self._node is None:
            return

        for param, value in self._node.getParameters().items():
            label = QLabel(param)
            self._hbox.addWidget(label)

    def clearParams(self):
        for i in reversed(range(self._hbox.count())):
            self._hbox.itemAt(i).widget().setParent(None)
