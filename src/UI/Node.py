from PluginLib.CompactQt.Qt import (
    QGraphicsObject,
    SIGNAL,
)
from UI.Elements.IOItem import IOItem
from UI.Elements.NodeRect import NodeRect
from UI.Elements.InputsOutputs import InputsOutputs


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
        self.createButtons()

    def createTitleRect(self):
        title_name = "Node"
        if self._node:
            title_name = self._node.getName()
        self.title_rect = NodeRect(self, title_name)
        self.title_rect.moved.connect(self.moved.emit)

    def getName(self):
        return self.title_rect.getName()

    def createButtons(self):
        if not self._node:
            return

        self._inputs = InputsOutputs(
            self.title_rect, InputsOutputs.INPUT, self._node.getNumberOfInputs(), self
        )
        self._inputs.clicked.connect(self.ioClicked.emit)

        self._outputs = InputsOutputs(
            self.title_rect, InputsOutputs.OUTPUT, self._node.getNumberOfOutputs(), self
        )
        self._outputs.clicked.connect(self.ioClicked.emit)

    def getNode(self):
        return self._node

    def boundingRect(self):
        return self.childrenBoundingRect()

    def paint(self, painter, option, widget=None):
        return
