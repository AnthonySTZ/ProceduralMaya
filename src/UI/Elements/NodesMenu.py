from PluginLib.CompactQt.Qt import QMenu, QAction
from Core.Nodes.NodesInfo import NodesInfo


class NodesMenu(QMenu):
    def __init__(self, position, parent=None):
        self._parent = parent
        self._position = position
        super().__init__()
        self.buildUI()

    def buildUI(self):
        nodes = NodesInfo.getNodes()
        for node in nodes:
            action = QAction(node.__name__, self._parent)
            action.setData(node)
            self.addAction(action)

    def getUserNode(self):
        try:
            res = self.exec(self._position)
        except:
            res = self.exec_(self._position)

        if not res:
            return None

        return (
            res.data()()
        )  # res.data return only the type of the node thats why there is ()()
