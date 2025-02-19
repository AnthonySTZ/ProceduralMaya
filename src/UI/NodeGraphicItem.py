from PluginLib.CompactQt.Qt import (
    QGraphicsItem,
    QGraphicsRectItem,
    Qt,
    QBrush,
    QGraphicsTextItem,
    QTextOption,
)


class NodeGraphicItem(QGraphicsRectItem):
    def __init__(self, position, node, parent=None):
        self._node = node
        super().__init__(parent)
        self.buildUI()
        self.setPos(
            position.x() - self.childrenBoundingRect().width() / 2,
            position.y() - self.childrenBoundingRect().height() / 2,
        )

    def buildUI(self):
        self.createTitleRect()
        self.updateTitleName()

    def createTitleRect(self):
        title_rect = QGraphicsRectItem(0, 0, 90, 25)
        title_rect.setFlags(
            QGraphicsItem.GraphicsItemFlag.ItemIsMovable
            | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable
        )
        brush = QBrush(Qt.GlobalColor.gray)
        title_rect.setBrush(brush)
        title_rect.setParentItem(self)

        self.title_name = QGraphicsTextItem("Node")
        self.title_name.setTextWidth(90)
        center_option = QTextOption()
        center_option.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_name.document().setDefaultTextOption(center_option)
        self.title_name.setParentItem(title_rect)

    def updateTitleName(self):
        self.title_name.setPlainText(self._node.getName())
