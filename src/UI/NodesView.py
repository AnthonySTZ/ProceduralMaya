from PluginLib.CompactQt.Qt import QWidget, QHBoxLayout, QLabel


class NodesView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        hbox = QHBoxLayout()
        self.setLayout(hbox)

        text = QLabel("Test Text")
        hbox.addWidget(text)
