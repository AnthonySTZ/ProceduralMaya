from PluginLib.CompactQt.Qt import (
    QBrush,
    Qt,
    QGraphicsTextItem,
    QColor,
    QPen,
    SIGNAL,
)
from Core.Qt.AQMovableRectItem import AQMovableRectItem
from UI.Elements.NodeIcon import NodeIcon


class NodeRect(AQMovableRectItem):
    WIDTH = 110
    HEIGHT = 30

    renderClicked = SIGNAL()

    def __init__(self, parent, node):
        super().__init__(0, 0, self.WIDTH, self.HEIGHT)
        self._node = node
        self.setParentItem(parent)
        self.buildUI()

    def buildUI(self):
        brush = QBrush(QColor(26, 28, 33, 230))
        self.setBrush(brush)
        self.setPen(QPen(QColor(80, 80, 80), 1.5))
        self.addIcon()
        self.createTitle()

    def addIcon(self):
        height_padding = 4
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

    def setRenderActive(self, should_render):
        if should_render:
            self.setPen(QPen(QColor(36, 100, 191), 3))
        else:
            self.setPen(QPen(QColor(69, 69, 69)))
        self.update()

    def setName(self, name):
        self._name = name
        self.title.setPlainText(name)

    def getName(self):
        return self._name
