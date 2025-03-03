from PluginLib.CompactQt.Qt import (
    QDialog,
    Qt,
    QListWidget,
    QVBoxLayout,
    QListWidgetItem,
    QLineEdit,
)
from Core.Nodes.NodesInfo import NodesInfo


class NodesMenu(QDialog):
    def __init__(self, position, parent=None):
        super().__init__(parent)
        self._usernode = None
        self.move(position)
        self.buildUI()

    def buildUI(self):
        self.setStyleSheet("""background-color: #545454; font-size: 10pt;""")
        self.setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint)
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

        search = QLineEdit()
        search.setPlaceholderText("Search...")
        search.textEdited.connect(self.userSearching)
        vbox.addWidget(search)

        search.setStyleSheet(
            """
            QLineEdit {
                border: 1px solid #666666;
                padding-left: 5px;
                padding-top: 2px;
                padding-bottom: 2px;
            }
            """
        )

        self.node_list = QListWidget()
        self.node_list.setSizeAdjustPolicy(
            QListWidget.SizeAdjustPolicy.AdjustToContents
        )

        vbox.addWidget(self.node_list)
        self.node_list.setStyleSheet(
            """
            QListView{
                border: 0px;
            }
            QListView::item {
                border: 0px;
                padding-left: 5px;
                padding-top: 2px;
                padding-bottom: 2px;
            }
            QListWidget::item:hover{
                background-color : #666666;
            }
            """
        )

        nodes = NodesInfo.getNodes()
        for node in nodes:
            node_item = QListWidgetItem(node.__name__, self.node_list)
            node_item.setData(Qt.ItemDataRole.UserRole, node)

        self.node_list.itemClicked.connect(self.userClicked)

        min_width = self.node_list.sizeHint().width() + 50
        self.setFixedWidth(min_width)

        search.setFocus()

    def userSearching(self, search_text):
        for i in range(self.node_list.count()):
            item = self.node_list.item(i)
            item.setHidden(True)
            if search_text.lower() in item.text().lower():
                item.setHidden(False)

    def userClicked(self, item):
        self._usernode = item.data(
            Qt.ItemDataRole.UserRole
        )()  # ()() because item store only the type
        self.close()

    def getUserNode(self):
        try:
            self.exec()
        except:
            self.exec_()

        return self._usernode
