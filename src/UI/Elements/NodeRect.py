from PluginLib.CompactQt.Qt import (
    QBrush,
    Qt,
    QGraphicsTextItem,
    QColor,
    SIGNAL,
)
from Core.Qt.AQMovableRectItem import AQMovableRectItem
from Core.Qt.AQClickableRectItem import AQClickableRectItem
from UI.Elements.NodeIcon import NodeIcon


class NodeRect(AQMovableRectItem):
    WIDTH = 90
    HEIGHT = 25

    renderClicked = SIGNAL()

    def __init__(self, parent, node):
        super().__init__(0, 0, self.WIDTH, self.HEIGHT)
        self._node = node
        self.setParentItem(parent)
        self.buildUI()

    def buildUI(self):
        brush = QBrush(QColor(26, 28, 33))
        self.setBrush(brush)
        self.addIcon()
        self.createTitle()
        self.createRenderRect()

    def addIcon(self):
        height_padding = 2
        icon_size = self.HEIGHT - height_padding * 2
        icon_pos_x = self.WIDTH / 2 - icon_size / 2
        icon = NodeIcon(self._node.getIcon(), icon_size)
        icon.setPos(icon_pos_x, height_padding)
        icon.setParentItem(self)

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
        self._render_rect.setBrush(QBrush(QColor(26, 28, 33)))
        self._render_rect.setParentItem(self)
        self._render_rect.clicked.connect(self.renderClicked.emit)

    def setRenderActive(self, should_render):
        if should_render:
            self._render_rect.setBrush(QBrush(Qt.GlobalColor.blue))
        else:
            self._render_rect.setBrush(QBrush(QColor(26, 28, 33)))
        self._render_rect.update()

    def setName(self, name):
        self._name = name
        self.title.setPlainText(name)

    def getName(self):
        return self._name
