from PluginLib.CompactQt.Qt import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    Qt,
    QPushButton,
)

from Core.Qt.QRoundButton import QRoundButton


class NodeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        main_vbox = QVBoxLayout()
        self.setLayout(main_vbox)

        self.inputs_hbox = QHBoxLayout()
        inputs_widget = QWidget()
        inputs_widget.setLayout(self.inputs_hbox)
        main_vbox.addWidget(inputs_widget)

        main_rect = QWidget()
        rect_hbox = QHBoxLayout()
        main_rect.setLayout(rect_hbox)
        main_vbox.addWidget(main_rect)

        self.nodeName = QLabel("Node Name")
        self.nodeName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rect_hbox.addWidget(self.nodeName)

        self.outputs_hbox = QHBoxLayout()
        outputs_widget = QWidget()
        outputs_widget.setLayout(self.outputs_hbox)
        main_vbox.addWidget(outputs_widget)

    def setNode(self, node):
        self.nodeName.setText(node.getName())

        for _ in range(node.getNumberOfInputs()):
            input_btn = QRoundButton()
            input_btn.setButtonSize(10)
            self.inputs_hbox.addWidget(input_btn)

        for _ in range(node.getNumberOfOutputs()):
            output_btn = QRoundButton()
            output_btn.setButtonSize(10)
            self.outputs_hbox.addWidget(output_btn)
