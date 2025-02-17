import os
import sys

from dotenv import load_dotenv

load_dotenv()

plugin_path = os.path.join(os.environ["PROCEDURAL_MAYA"], "src")

sys.path.insert(0, plugin_path)

from Core.Nodes.NodesInfo import NodesInfo
from UI.NodeWidget import NodeWidget
from PluginLib.CompactQt.Qt import QApplication

cube_node = NodesInfo.getNodes()[0]()

app = QApplication([])
window = NodeWidget()
window.setNode(cube_node)
window.show()
app.exec()
