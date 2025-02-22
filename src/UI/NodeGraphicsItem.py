from PluginLib.CompactQt.Qt import (
    QGraphicsItem,
    QGraphicsRectItem,
    Qt,
    QBrush,
    QGraphicsTextItem,
    QTextOption,
    QPen,
    QGraphicsObject,
    SIGNAL,
)
from Core.Qt.AQClickableEllipseItem import AQClickableEllipseItem
from UI.IOItem import IOItem


class NodeGraphicsItem(QGraphicsObject):

    ioClicked = SIGNAL(IOItem)

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
        self.title_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        brush = QBrush(Qt.GlobalColor.gray)
        self.title_rect.setBrush(brush)
        self.title_rect.setParentItem(self)

        self.title_name = QGraphicsTextItem("Node")
        self.title_name.setDefaultTextColor(Qt.GlobalColor.black)
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
        btn_width_padding = 10
        btn_height_padding = 2

        self.createInputsButtons(btn_radius, btn_width_padding, btn_height_padding)
        self.createOutputsButtons(btn_radius, btn_width_padding, btn_height_padding)

    def createInputsButtons(self, radius, width_padding, height_padding):

        num_of_inputs = self._node.getNumberOfInputs()
        input_pos_y = -height_padding - radius
        input_buttons = self.createIOButtonsAtHeight(
            radius, width_padding, input_pos_y, num_of_inputs
        )
        for button in input_buttons:
            button.clicked.connect(
                lambda _: self.ioClicked.emit(IOItem(self, button, IOItem.INPUT))
            )

    def createOutputsButtons(self, radius, width_padding, height_padding):

        num_of_outputs = self._node.getNumberOfOutputs()
        ouput_pos_y = self.title_rect.boundingRect().height() + height_padding
        output_buttons = self.createIOButtonsAtHeight(
            radius, width_padding, ouput_pos_y, num_of_outputs
        )
        for button in output_buttons:
            button.clicked.connect(
                lambda _: self.ioClicked.emit(IOItem(self, button, IOItem.OUTPUT))
            )

    def createIOButtonsAtHeight(self, radius, width_padding, height, num_of_buttons):
        width_offset = width_padding - radius
        rect_width = self.title_rect.boundingRect().width()
        width_with_padding = rect_width - width_padding

        buttons = []
        for idx in range(num_of_buttons):

            button = self.generateEllipseItemsOnLine(
                width_with_padding,
                height,
                num_of_buttons,
                idx,
                radius,
                width_offset,
            )
            button.setParentItem(self.title_rect)
            button.setUserData("index", idx)
            buttons.append(button)
        return buttons

    def generateEllipseItemsOnLine(
        self, line_width, line_height, line_points, ellispe_num, ellipse_radius, offset
    ):

        x_offset = (ellispe_num + 1) * (line_width / (line_points + 1))
        pos_x = offset + x_offset

        button = AQClickableEllipseItem(
            pos_x,
            line_height,
            ellipse_radius,
            ellipse_radius,
        )
        button.setBrush(QBrush(Qt.GlobalColor.gray))
        button.setPen(QPen(Qt.GlobalColor.black))
        return button

    def boundingRect(self):
        return self.childrenBoundingRect()

    def paint(self, painter, option, widget=None):
        return
