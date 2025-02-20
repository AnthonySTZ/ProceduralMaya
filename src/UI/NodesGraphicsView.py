from PluginLib.CompactQt.Qt import (
    QGraphicsView,
    Qt,
    QShortcut,
    QKeySequence,
    QMenu,
    QCursor,
    QAction,
    QPainter,
    QPoint,
    QFrame,
)
from Core.Nodes.NodesInfo import NodesInfo
from UI.NodeGraphicsItem import NodeGraphicsItem


class NodesGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        self._scene = scene
        self._is_scrolling = False
        self._scroll_pos = QPoint(0, 0)
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
            item = NodeGraphicsItem(item_pos, node)
            self._scene.addItem(item)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self._is_scrolling = True
            self._scroll_pos = event.position()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._is_scrolling:
            new_pos = event.position()
            offset = new_pos - self._scroll_pos
            transform = self.transform()
            self.translate(offset.x() / transform.m11(), offset.y() / transform.m22())
            self._scroll_pos = new_pos
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self._is_scrolling:
            self._is_scrolling = False
        super().mouseReleaseEvent(event)
