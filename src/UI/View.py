from PluginLib.CompactQt.Qt import (
    Qt,
    QShortcut,
    QKeySequence,
    QMenu,
    QCursor,
    QAction,
    QPainter,
    QFrame,
)
from Core.Nodes.NodesInfo import NodesInfo
from UI.Node import Node
from Core.Qt.AQGraphicsTransformView import AQGraphicsTransformView


class View(AQGraphicsTransformView):
    def __init__(self, scene, parent=None):
        self._scene = scene
        super().__init__(scene, parent)
        self.buildUI()

    def buildUI(self):
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing | QPainter.RenderHint.TextAntialiasing
        )
        self.setFrameStyle(QFrame.Shape.NoFrame)
        self.setTransformationAnchor(self.ViewportAnchor.NoAnchor)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

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
            item = Node(item_pos, node)
            self._scene.addNode(item)

    def mouseMoveEvent(self, event):
        self._scene.moveEvent(self.mapToScene(event.pos()))
        super().mouseMoveEvent(event)
