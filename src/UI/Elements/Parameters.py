from PluginLib.CompactQt.Qt import QWidget, QHBoxLayout


class Parameters(QWidget):
    def __init__(self):
        super().__init__()
        self._node = None
        self.buildUI()

    def buildUI(self):
        self._hbox = QHBoxLayout()
        self.setLayout(self._hbox)

    def setNode(self, node):
        self._node = node

    def updateParameters(self):
        if self._node is None:
            return

        for param, value in self._node.getParameters():
            print(param)
