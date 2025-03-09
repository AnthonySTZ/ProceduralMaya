from PluginLib.CompactQt.Qt import QHBoxLayout, QDialog, QSplitter
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

        splitter = QSplitter()

        scene_size = 8000

        scene = Scene()
        scene.setSceneRect(0, 0, scene_size, scene_size)
        scene.buildGrid()
        nodes_viewer = View(scene)
        parameters_view = Parameters(scene)

        splitter.addWidget(nodes_viewer)
        splitter.addWidget(parameters_view)

        vbox.addWidget(splitter)
