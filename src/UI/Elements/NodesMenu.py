from PluginLib.CompactQt.Qt import (
    QDialog,
    Qt,
    QListWidget,
    QVBoxLayout,
    QListWidgetItem,
)
from Core.Nodes.NodesInfo import NodesInfo


class NodesMenu(QDialog):
    def __init__(self, position, parent=None):
        super().__init__(parent)
        self.move(position)
        self.buildUI()

    def buildUI(self):
        self.setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint)
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

        node_list = QListWidget()
        node_list.setResizeMode(QListWidget.ResizeMode.Adjust)
        vbox.addWidget(node_list)

        nodes = NodesInfo.getNodes()
        for node in nodes:
            node_item = QListWidgetItem(node.__name__, node_list)
            node_item.setData(Qt.ItemDataRole.UserRole, node)

    def getUserNode(self):
        try:
            res = self.exec()
        except:
            res = self.exec_()

        if not res:
            return None

        return (
            res.data()()
        )  # res.data return only the type of the node thats why there is ()()
