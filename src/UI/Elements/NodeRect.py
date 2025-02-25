from PluginLib.CompactQt.Qt import QBrush, Qt, QGraphicsTextItem, QTextOption
from Core.Qt.AQMovableRectItem import AQMovableRectItem


class NodeRect(AQMovableRectItem):
    WIDTH = 90
    HEIGHT = 25

    def __init__(self, parent, name):
        super().__init__(0, 0, self.WIDTH, self.HEIGHT)
        self._name = name
        self.setParentItem(parent)
        self.buildUI()

    def buildUI(self):
        brush = QBrush(Qt.GlobalColor.gray)
        self.setBrush(brush)

        self.createTitle()

    def createTitle(self):
        """
        Create a title that is centered to the nodeRect.
        """

        self.title = QGraphicsTextItem(self._name)
        self.title.setDefaultTextColor(Qt.GlobalColor.black)
        self.title.setTextWidth(self.boundingRect().width())
        center_option = QTextOption()
        center_option.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.document().setDefaultTextOption(center_option)
        self.title.setParentItem(self)

    def setName(self, name):
        self._name = name
        self.title.setPlainText(name)

    def getName(self):
        return self._name
