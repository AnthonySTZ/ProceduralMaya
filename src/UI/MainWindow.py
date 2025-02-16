from PluginLib.CompactQt.Qt import QVBoxLayout, QDialog
from UI.NodesView import NodesView


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        self.resize(1200, 800)
        self.setWindowTitle("Maya Procedural")
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        nodes_viewer = NodesView()

        vbox.addWidget(nodes_viewer)
