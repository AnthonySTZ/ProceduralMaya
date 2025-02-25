from PluginLib.CompactQt.Qt import QHBoxLayout, QDialog
from UI.View import View
from UI.Scene import Scene
from UI.Parameters import Parameters


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        self.resize(1200, 800)
        self.setWindowTitle("Maya Procedural")
        vbox = QHBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

        scene = Scene()
        scene.setSceneRect(-32000, -32000, 64000, 64000)
        nodes_viewer = View(scene)
        parameters_view = Parameters(scene)

        vbox.addWidget(nodes_viewer)
        vbox.addWidget(parameters_view)
