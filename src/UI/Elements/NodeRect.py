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

    def __init__(self, parent, name):
        super().__init__(0, 0, self.WIDTH, self.HEIGHT)
        self._name = name
        self.setParentItem(parent)
        self.buildUI()

    def buildUI(self):
        brush = QBrush(Qt.GlobalColor.gray)
        self.setBrush(brush)

        self.createTitle()
        self.createRenderRect()

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
