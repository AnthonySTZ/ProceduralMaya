from PluginLib.CompactQt.Qt import QVBoxLayout, QDialog
from UI.NodesGraphicsView import NodesGraphicsView
from UI.NodesGraphicsScene import NodesGraphicsScene


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        self.resize(1200, 800)
        self.setWindowTitle("Maya Procedural")
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

        scene = NodesGraphicsScene()
        scene.setSceneRect(-32000, -32000, 64000, 64000)
        nodes_viewer = NodesGraphicsView(scene)

        vbox.addWidget(nodes_viewer)
