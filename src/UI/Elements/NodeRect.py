from PluginLib.CompactQt.Qt import (
    QBrush,
    Qt,
    QGraphicsTextItem,
    QTextOption,
    QGraphicsRectItem,
    SIGNAL,
)
from Core.Qt.AQMovableRectItem import AQMovableRectItem
from Core.Qt.AQClickableRectItem import AQClickableRectItem


class NodeRect(AQMovableRectItem):
    WIDTH = 90
    HEIGHT = 25

    renderClicked = SIGNAL()

    def __init__(self, parent, name, node):
        super().__init__(0, 0, self.WIDTH, self.HEIGHT)
        self._node = node
        self._name = name
        self.setParentItem(parent)
        self.buildUI()

    def buildUI(self):
        brush = QBrush(Qt.GlobalColor.gray)
        self.setBrush(brush)

        self.createTitle()
        self.createRenderRect()

    def createTitle(self):
        self.title = QGraphicsTextItem(self._node.getName())
        self.title.setDefaultTextColor(Qt.GlobalColor.lightGray)
        self.title.setPos(self.WIDTH, 2)
        self.title.setParentItem(self)

        # update title when name changed
        self._node.nameChanged.connect(self.title.setPlainText)

        node_type = type(self._node).__name__
        self._node_type = QGraphicsTextItem(node_type)
        self._node_type.setDefaultTextColor(Qt.GlobalColor.gray)
        self._node_type.setPos(self.WIDTH, -self.HEIGHT + 8)
        self._node_type.setParentItem(self)

    def createRenderRect(self):
        render_width = 10
        self._render_rect = AQClickableRectItem(
            self.WIDTH - render_width, 0, render_width, self.HEIGHT
        )
        self._render_rect.setBrush(QBrush(Qt.GlobalColor.lightGray))
        self._render_rect.setParentItem(self)
        self._render_rect.clicked.connect(self.renderClicked.emit)

    def setRenderActive(self, should_render):
        if should_render:
            self._render_rect.setBrush(QBrush(Qt.GlobalColor.blue))
        else:
            self._render_rect.setBrush(QBrush(Qt.GlobalColor.lightGray))
        self._render_rect.update()

    def setName(self, name):
        self._name = name
        self.title.setPlainText(name)

    def getName(self):
        return self._name
