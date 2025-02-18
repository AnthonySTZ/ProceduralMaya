from PluginLib.CompactQt.Qt import (
    QWidget,
    QHBoxLayout,
    QLabel,
    Qt,
    QMenu,
    QCursor,
    QShortcut,
    QKeySequence,
)
from Core.Nodes.NodesInfo import NodesInfo
from Core.Qt.QDataAction import QDataAction
from UI.NodeWidget import NodeWidget


class NodesView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.nodes = []
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
        tab_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Tab), self)
        tab_shortcut.activated.connect(self.nodesContextMenu)

    def nodesContextMenu(self):
        menu = QMenu()
        nodes = NodesInfo.getNodes()
        for node in nodes:
            action = QDataAction(node.__name__)
            action.setUserData(node)
            menu.addAction(action)
        try:
            res = menu.exec(QCursor.pos())
        except:
            res = menu.exec_(QCursor.pos())

        if res:
            nodeType = res.getUserData()
            node = nodeType()
            self.addNode(node, self.mapFromGlobal(QCursor.pos()))

    def addNode(self, node, position):
        new_node = NodeWidget()
        new_node.setNode(node)
        new_node.setPosition(position)

        self.nodes.append(new_node)
        print(self.nodes)
