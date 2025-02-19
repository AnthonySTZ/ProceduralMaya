from PluginLib.CompactQt.Qt import (
    QWidget,
    QAction,
    Qt,
    QMenu,
    QCursor,
    QShortcut,
    QKeySequence,
)
from Core.Nodes.NodesInfo import NodesInfo
from UI.NodeWidget import NodeWidget


class NodesView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.nodes = []
        self._is_linking = False
        self.buildUI()

    def buildUI(self):
        self.setStyleSheet(
            """
            QWidget{
                background-color: #2e2e2e;
            }
            """
        )

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.nodesContextMenu)
        tab_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Tab), self)
        tab_shortcut.activated.connect(self.nodesContextMenu)

    def nodesContextMenu(self):
        menu = QMenu()
        nodes = NodesInfo.getNodes()
        for node in nodes:
            action = QAction(node.__name__, self)
            action.setData(node)
            menu.addAction(action)
        try:
            res = menu.exec(QCursor.pos())
        except:
            res = menu.exec_(QCursor.pos())

        if res:
            nodeType = res.data()
            node = nodeType()
            self.addNode(node, self.mapFromGlobal(QCursor.pos()))

    def addNode(self, node, position):
        new_node = NodeWidget()
        new_node.setNode(node)
        new_node.setPosition(position)

        new_node.setParent(self)
        new_node.show()
        new_node.inputClicked.connect(self.inputClicked)
        new_node.outputClicked.connect(self.outputClicked)
        self.nodes.append(new_node)

    def inputClicked(self, input_btn, input_id):
        print(input_btn)
        print(" Input " + str(input_id) + " clicked !")

        if not self._is_linking:
            self._is_linking = True
        else:
            self._is_linking = False
            # TODO: Create Connection between nodes

    def outputClicked(self, output_btn, output_id):
        print(output_btn)
        print(" Output " + str(output_id) + " clicked !")

        if not self._is_linking:
            self._is_linking = True
        else:
            self._is_linking = False
            # TODO: Create Connection between nodes
