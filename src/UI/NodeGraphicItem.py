from PluginLib.CompactQt.Qt import (
    QGraphicsItem,
    QGraphicsRectItem,
    Qt,
    QBrush,
    QGraphicsTextItem,
    QTextOption,
    QGraphicsEllipseItem,
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
        self.createButtons()

    def createTitleRect(self):
        self.title_rect = QGraphicsRectItem(0, 0, 90, 25)
        self.title_rect.setFlags(
            QGraphicsItem.GraphicsItemFlag.ItemIsMovable
            | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable
        )
        brush = QBrush(Qt.GlobalColor.gray)
        self.title_rect.setBrush(brush)
        self.title_rect.setParentItem(self)

        self.title_name = QGraphicsTextItem("Node")
        self.title_name.setTextWidth(self.title_rect.boundingRect().width())
        center_option = QTextOption()
        center_option.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_name.document().setDefaultTextOption(center_option)
        self.title_name.setParentItem(self.title_rect)

    def updateTitleName(self):
        if not self._node:
            return

        self.title_name.setPlainText(self._node.getName())

    def createButtons(self):
        if not self._node:
            return

        btn_radius = 9
        btn_height_padding = 2
        btn_width_padding = 10

        width_offset = btn_width_padding - btn_radius
        rect_width = self.title_rect.boundingRect().width()
        width_with_padding = rect_width - btn_width_padding

        inputs_nb = self._node.getNumberOfInputs()
        for idx in range(inputs_nb):

            x_offset = (idx + 1) * (width_with_padding / (inputs_nb + 1))
            pos_x = width_offset + x_offset
            pos_y = -btn_height_padding - btn_radius
            button = QGraphicsEllipseItem(
                pos_x,
                pos_y,
                btn_radius,
                btn_radius,
            )
            brush = QBrush(Qt.GlobalColor.gray)
            button.setBrush(brush)
            button.setParentItem(self.title_rect)
