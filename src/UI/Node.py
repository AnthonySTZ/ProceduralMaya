from PluginLib.CompactQt.Qt import (
    Qt,
    QBrush,
    QPen,
    QGraphicsObject,
    SIGNAL,
)
from Core.Qt.AQClickableEllipseItem import AQClickableEllipseItem
from UI.IOItem import IOItem
from UI.Elements.NodeRect import NodeRect


class Node(QGraphicsObject):

    ioClicked = SIGNAL(IOItem)
    moved = SIGNAL()

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
        # self.createButtons()

    def createTitleRect(self):
        title_name = "Node"
        if self._node:
            title_name = self._node.getName()
        self.title_rect = NodeRect(self, title_name)
        self.title_rect.moved.connect(self.moved.emit)

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
