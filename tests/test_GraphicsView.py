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
    QBrush,
    QGraphicsRectItem,
    Qt,
)

main_rect = QGraphicsRectItem(0, 0, 200, 50)
child_rect = QGraphicsRectItem(0, 100, 200, 50)
brush = QBrush(Qt.GlobalColor.red)
child_rect.setBrush(brush)

child_rect.setParentItem(main_rect)

main_rect.setPos(50, 50)

app = QApplication([])
scene = QGraphicsScene(0, 0, 1200, 800)
scene.addItem(main_rect)


view = QGraphicsView(scene)
view.show()
app.exec()
