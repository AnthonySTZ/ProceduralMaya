import os
import sys

from dotenv import load_dotenv

load_dotenv()

plugin_path = os.path.join(os.environ["PROCEDURAL_MAYA"], "src")

sys.path.insert(0, plugin_path)

from PluginLib.CompactQt.Qt import (
    QApplication,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsObject,
    QGraphicsItem,
    QRectF,
)

from UI.GraphicsConnectionLine import GraphicsConnectionLine


class Ellipse(QGraphicsObject):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self._rect = QRectF(x, y, width, height)

    def boundingRect(self):
        return self._rect

    def paint(self, painter, option, widget=None):
        painter.drawEllipse(self._rect)


app = QApplication([])
scene = QGraphicsScene(0, 0, 1200, 800)

item1 = Ellipse(0, 0, 50, 50)
item1.setPos(50, 100)
item2 = Ellipse(0, 0, 50, 50)
item2.setPos(70, 150)

line = GraphicsConnectionLine()
line.setFirstItem(item1)
line.setLastItem(item2)
scene.addItem(item1)
scene.addItem(item2)
scene.addItem(line)
line.updateLine()


view = QGraphicsView(scene)
view.show()
app.exec()
