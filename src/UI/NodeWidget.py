from PluginLib.CompactQt.Qt import QWidget, QVBoxLayout, QLabel, QHBoxLayout, Qt, QPoint

from Core.Qt.QRoundButton import QRoundButton


class NodeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._position = QPoint(0, 0)
        self.buildUI()

    def buildUI(self):
        self.setStyleSheet(
            """
                    QWidget {
                        background-color: transparent;
                    }
                    """
        )
        main_vbox = QVBoxLayout()
        main_vbox.setContentsMargins(0, 0, 0, 0)
        main_vbox.setSpacing(3)
        self.setLayout(main_vbox)

        self.inputs_hbox = QHBoxLayout()
        self.inputs_hbox.setContentsMargins(0, 0, 0, 0)
        self.inputs_widget = QWidget()

        self.inputs_widget.setLayout(self.inputs_hbox)
        main_vbox.addWidget(self.inputs_widget)

        main_rect = QWidget()
        rect_hbox = QHBoxLayout()
        rect_hbox.setContentsMargins(0, 0, 0, 0)
        main_rect.setLayout(rect_hbox)
        main_rect.setFixedHeight(30)
        main_vbox.addWidget(main_rect)
        main_rect.setStyleSheet(
            """
                QWidget {
                    background-color: #dbdbdb;
                    color: black;
                    border-radius: 8px;
                }
            """
        )

        self.nodeName = QLabel("Node Name")
        self.nodeName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rect_hbox.addWidget(self.nodeName)

        self.outputs_hbox = QHBoxLayout()
        self.outputs_hbox.setContentsMargins(0, 0, 0, 0)
        self.outputs_widget = QWidget()
        self.outputs_widget.setLayout(self.outputs_hbox)
        main_vbox.addWidget(self.outputs_widget)

    def setNode(self, node):
        self.inputs_widget.setHidden(True)
        self.outputs_widget.setHidden(True)

        self.nodeName.setText(node.getName())

        inputs_number = node.getNumberOfInputs()
        if inputs_number > 0:
            self.inputs_widget.setHidden(False)
        outputs_number = node.getNumberOfOutputs()
        if outputs_number > 0:
            self.outputs_widget.setHidden(False)

        for _ in range(inputs_number):
            input_btn = QRoundButton()
            input_btn.setButtonSize(10)
            self.inputs_hbox.addWidget(input_btn)

        for _ in range(outputs_number):
            output_btn = QRoundButton()
            output_btn.setButtonSize(10)
            self.outputs_hbox.addWidget(output_btn)

    def setPosition(self, position):
        self._position = position

    def getPosition(self):
        return self._position
