from PluginLib.CompactQt.Qt import QWidget, QHBoxLayout, QSize, QLabel, Qt


class NodeTitleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        rect_hbox = QHBoxLayout()
        rect_hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(rect_hbox)
        self.setFixedSize(QSize(90, 25))

        self.setStyleSheet(
            """
                QWidget {
                    background-color: #c9c9c9;
                    color: black;
                    border-radius: 7px;
                }
                QWidget:hover {
                    background-color: #e0e0e0;
                }
            """
        )
        self.nodeName = QLabel("Node Name")
        self.nodeName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rect_hbox.addWidget(self.nodeName)

    def setNodeTitle(self, title):
        self.nodeName.setText(title)
