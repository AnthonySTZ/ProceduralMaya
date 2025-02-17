from PluginLib.CompactQt.Qt import QWidget, QVBoxLayout, QLabel, QHBoxLayout, Qt


class NodeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        main_vbox = QVBoxLayout()
        self.setLayout(main_vbox)

        main_rect = QWidget()
        rect_hbox = QHBoxLayout()
        main_rect.setLayout(rect_hbox)

        self.nodeName = QLabel("Node Name")
        self.nodeName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rect_hbox.addWidget(self.nodeName)

        main_vbox.addWidget(main_rect)

    def setNode(self, node):
        self.nodeName.setText(node.getName())
