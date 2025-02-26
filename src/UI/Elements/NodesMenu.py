from PluginLib.CompactQt.Qt import QMenu, QAction
from Core.Nodes.NodesInfo import NodesInfo


class NodesMenu(QMenu):
    def __init__(self, parent=None):
        self._parent = parent
        super().__init__()
        self.buildUI()

    def buildUI(self):
        nodes = NodesInfo.getNodes()
        for node in nodes:
            action = QAction(node.__name__, self._parent)
            action.setData(node)
            self.addAction(action)
