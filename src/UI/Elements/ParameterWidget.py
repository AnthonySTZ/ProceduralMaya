from PluginLib.CompactQt.Qt import QWidget, QHBoxLayout, QLabel, Qt, SIGNAL


class ParameterWidget(QWidget):

    valueChanged = SIGNAL()

    def __init__(self, param, value):
        super().__init__()
        self.buildUI(param, value)

    def buildUI(self, param, value):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 5, 0, 0)
        hbox.setSpacing(10)
        self.setStyleSheet(
            """
            QLineEdit {
                padding: 4px;
            }            
            """
        )
        self.setLayout(hbox)

        label = QLabel(param)
        label.setFixedWidth(100)
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter)

        parameters_edit = value.getUI()
        value.valueChanged.connect(self.valueChanged.emit)

        hbox.addWidget(label)
        hbox.addWidget(parameters_edit)
