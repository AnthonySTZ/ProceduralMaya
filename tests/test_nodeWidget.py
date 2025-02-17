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
cube_node._num_inputs = 2
cube_node._num_outputs = 3

app = QApplication([])
window = NodeWidget()
window.setStyleSheet(
    """
            QWidget {
                background-color: #424242;
                color: #c2c2c2;
            }
            """
)
window.setNode(cube_node)
window.show()
app.exec()
