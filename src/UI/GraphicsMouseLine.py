from PluginLib.CompactQt.Qt import QGraphicsLineItem, QPen, Qt, QPoint


class GraphicsMouseLine(QGraphicsLineItem):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._io = None
        self._mouse_pos = QPoint(0, 0)
        self.setPen(QPen(Qt.GlobalColor.white))

    def setIO(self, io):
        self._io = io
        self._io.xChanged.connect(self.updateLine)
        self._io.yChanged.connect(self.updateLine)

    def updateLine(self):
        io_pos = self._io.centerPos()
        self.setLine(
            io_pos.x(),
            io_pos.y(),
            self._mouse_pos.x(),
            self._mouse_pos.y(),
        )

    def updateMousePos(self, mouse_pos):
        self._mouse_pos = mouse_pos
        self.updateLine()
