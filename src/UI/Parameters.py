from PluginLib.CompactQt.Qt import QWidget, QVBoxLayout, QLabel


class Parameters(QWidget):
    def __init__(self):
        super().__init__()
        self._node = None
        self.buildUI()

    def buildUI(self):
        self._hbox = QVBoxLayout()
        self.setLayout(self._hbox)

    def setNode(self, node):
        self._node = node

    def updateParameters(self):
        self.clearParams()

        if self._node is None:
            return

        for param, value in self._node.getParameters():
            label = QLabel(param)
            self._hbox.addWidget(label)

    def clearParams(self):
        for child in self._hbox.children():
            child.setParent(None)
