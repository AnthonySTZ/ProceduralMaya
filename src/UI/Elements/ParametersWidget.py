from PluginLib.CompactQt.Qt import QWidget, QLabel, SIGNAL, QGridLayout, Qt


class ParametersWidget(QWidget):

    valueChanged = SIGNAL()

    def __init__(self, parameters):
        super().__init__()
        self._parameters = parameters
        self.buildUI()

    def buildUI(self):
        layout = QGridLayout(self)
        self.setLayout(layout)

        self.setStyleSheet(
            """
            QLabel {
                padding-right: 5px;
            }
            QLineEdit {
                padding-left: 3px;
            }
            """
        )

        i = 0
        for param, value in self._parameters.items():
            label = QLabel(param)
            label.setAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter
            )
            field_widget = value.getUI()
            value.valueChanged.connect(self.valueChanged.emit)
            layout.addWidget(label, i, 0)
            layout.addWidget(field_widget, i, 1)
            i += 1
