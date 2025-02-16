from PluginLib.CompactQt.Qt import QVBoxLayout, QDialog


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        self.setWindowTitle("Maya Procedural")
        vbox = QVBoxLayout()
        self.setLayout(vbox)
