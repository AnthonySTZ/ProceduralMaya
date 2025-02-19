from PluginLib.CompactQt.Qt import QVBoxLayout, QDialog
from UI.NodesGraphicsView import NodesGraphicsView
from UI.NodesGraphicScene import NodesGraphicScene


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        self.resize(1200, 800)
        self.setWindowTitle("Maya Procedural")
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        scene = NodesGraphicScene()
        nodes_viewer = NodesGraphicsView(scene)

        vbox.addWidget(nodes_viewer)
