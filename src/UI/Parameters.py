from PluginLib.CompactQt.Qt import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    Qt,
)


class Parameters(QWidget):
    def __init__(self, scene):
        super().__init__()
        self._scene = scene
        self._node = None
        self.buildUI()

    def buildUI(self):
        self.setStyleSheet(
            """
            font-size: 9pt;
            """
        )
        self._vbox = QVBoxLayout()
        self._vbox.setSpacing(0)
        self._vbox.setContentsMargins(0, 5, 0, 0)
        self.setLayout(self._vbox)

        self.setMinimumWidth(300)

        self._scene.nodeClicked.connect(self.setNode)

    def setNode(self, node):
        self._node = node
        self.updateParameters()
        self._node.nameChanged.connect(self._node_name.setText)

    def updateParameters(self):
        self.clearParams()

        if self._node is None:
            return

        self._node_name = QLineEdit(self._node.getName())
        self._node_name.returnPressed.connect(
            lambda node_name=self._node_name: self.changeNodeName(node_name.text())
        )
        self._node_name.setStyleSheet(
            """
            QLineEdit {
                padding: 4px;
            }            
            """
        )
        self._vbox.addWidget(self._node_name)

        for param, value in self._node.getParameters().items():
            param_widget = self.createParamWidget(param, value)
            self._vbox.addWidget(param_widget)

        self._vbox.addStretch()

    def createParamWidget(self, param, value):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 5, 0, 0)
        hbox.setSpacing(10)
        widget = QWidget()
        widget.setStyleSheet(
            """
            QLineEdit {
                padding: 4px;
            }            
            """
        )
        widget.setLayout(hbox)

        label = QLabel(param)
        label.setFixedWidth(100)
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter)

        parameters_edit = value.getUI()
        value.valueChanged.connect(self._scene.updateCurrentRender)

        hbox.addWidget(label)
        hbox.addWidget(parameters_edit)

        return widget

    def changeNodeName(self, name):
        self._scene.getNodeScene().renameNode(self._node.getName(), name)

    def clearParams(self):
        for i in reversed(range(self._vbox.count())):
            item = self._vbox.itemAt(i)
            if item.spacerItem():
                self._vbox.removeItem(item)
            else:
                item.widget().setParent(None)
