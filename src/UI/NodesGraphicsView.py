from PluginLib.CompactQt.Qt import (
    QGraphicsView,
    Qt,
    QShortcut,
    QKeySequence,
    QMenu,
    QCursor,
)
from Core.Nodes.NodesInfo import NodesInfo
from Core.Qt.QDataAction import QDataAction


class NodesGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        self._scene = scene
        super().__init__(scene, parent)
        self.buildUI()

    def buildUI(self):
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.nodesContextMenu)
        tab_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Tab), self)
        tab_shortcut.activated.connect(self.nodesContextMenu)

    def nodesContextMenu(self):
        menu = QMenu()
        nodes = NodesInfo.getNodes()
        for node in nodes:
            action = QDataAction(node.__name__, self)
            action.setUserData(node)
            menu.addAction(action)
        try:
            res = menu.exec(QCursor.pos())
        except:
            res = menu.exec_(QCursor.pos())

        if res:
            nodeType = res.getUserData()
            node = nodeType()
            print(node)  # TODO: add Node to the scene
