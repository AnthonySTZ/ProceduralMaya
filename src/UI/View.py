from PluginLib.CompactQt.Qt import (
    Qt,
    QShortcut,
    QKeySequence,
    QCursor,
    QPainter,
    QFrame,
)
from UI.Node import Node
from UI.Elements.NodesMenu import NodesMenu
from Core.Qt.AQGraphicsTransformView import AQGraphicsTransformView


class View(AQGraphicsTransformView):
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
        menu = NodesMenu(QCursor.pos(), self)
        user_node = menu.getUserNode()

        if user_node:
            item_pos = self.mapToScene(self.mapFromGlobal(QCursor.pos()))
            item = Node(item_pos, user_node)
            self._scene.addNodeItem(item)

    def mouseMoveEvent(self, event):
        self._scene.moveEvent(self.mapToScene(event.pos()))
        super().mouseMoveEvent(event)
