import os
import sys

from dotenv import load_dotenv

load_dotenv()

plugin_path = os.path.join(os.environ["PROCEDURAL_MAYA"], "src")

sys.path.insert(0, plugin_path)

from PluginLib.CompactQt.Qt import QApplication, QGraphicsView, QGraphicsScene, QPoint

from UI.GraphicsConnectionLine import GraphicsConnectionLine

app = QApplication([])
scene = QGraphicsScene(0, 0, 1200, 800)

line = GraphicsConnectionLine()
line.setFirstPoint(QPoint(10, 20))
line.setLastPoint(QPoint(50, 70))
scene.addItem(line)
line.updateLine()


view = QGraphicsView(scene)
view.show()
app.exec()
