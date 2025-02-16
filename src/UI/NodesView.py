from PluginLib.CompactQt.Qt import QWidget, QHBoxLayout, QLabel, Qt, QMenu, QCursor
from Core.Nodes.NodesInfo import NodesInfo


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

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.nodesContextMenu)

    def nodesContextMenu(self):
        menu = QMenu()
        nodes = NodesInfo.getNodes()
        for node in nodes:
            menu.addAction(node.__name__)
        try:
            menu.exec(QCursor.pos())
        except:
            menu.exec_(QCursor.pos())
