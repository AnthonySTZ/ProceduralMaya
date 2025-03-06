from PluginLib.CompactQt.Qt import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
)
from UI.Elements.ParametersWidget import ParametersWidget


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
        self._vbox.setContentsMargins(0, 8, 8, 0)
        self.setMinimumWidth(300)
        self.setLayout(self._vbox)
        self._scene.nodeClicked.connect(self.setNode)

        self.createTitle()
        self.field_table = ParametersWidget()
        self.field_table.valueChanged.connect(self._scene.updateCurrentRender)
        self._vbox.addWidget(self.field_table)
        self._vbox.addStretch()

    def setNode(self, node):
        self._node = node
        self.updateParameters()
        self._node.nameChanged.connect(self._node_name.setText)

    def updateParameters(self):
        self._node_name.setText("")
        self.field_table.clearParams()
        if self._node is None:
            return

        self._node_name.setText(self._node.getName())
        self.field_table.updateParams(self._node.getParameters())

    def createTitle(self):
        self._node_name = QLineEdit("")
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

    def changeNodeName(self, name):
        self._scene.getNodeScene().renameNode(self._node.getName(), name)
