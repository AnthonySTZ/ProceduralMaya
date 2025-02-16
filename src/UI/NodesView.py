from PluginLib.CompactQt.Qt import QWidget, QHBoxLayout, QLabel


class NodesView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(hbox)
        self.setStyleSheet(
            """
            QWidget{
                background-color: #2e2e2e;
            }
            """
        )

        text = QLabel("Test Text")
        hbox.addWidget(text)
