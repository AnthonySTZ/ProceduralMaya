from PluginLib.CompactQt.Qt import (
    QGraphicsView,
    Qt,
    QShortcut,
    QKeySequence,
    QMenu,
    QCursor,
    QAction,
    QPainter,
)
from Core.Nodes.NodesInfo import NodesInfo
from UI.NodeGraphicItem import NodeGraphicItem


class NodesGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        self._scene = scene
        super().__init__(scene, parent)
        self.buildUI()

    def buildUI(self):
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing | QPainter.RenderHint.TextAntialiasing
        )

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.nodesContextMenu)
        tab_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Tab), self)
        tab_shortcut.activated.connect(self.nodesContextMenu)

    def nodesContextMenu(self):
        menu = QMenu()
        nodes = NodesInfo.getNodes()
        for node in nodes:
            action = QAction(node.__name__, self)
            action.setData(node)
            menu.addAction(action)
        try:
            res = menu.exec(QCursor.pos())
        except:
            res = menu.exec_(QCursor.pos())

        if res:
            nodeType = res.data()
            node = nodeType()
            item_pos = self.mapToScene(self.mapFromGlobal(QCursor.pos()))
            item = NodeGraphicItem(item_pos, node)
            self._scene.addItem(item)
