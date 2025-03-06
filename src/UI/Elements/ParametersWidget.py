from PluginLib.CompactQt.Qt import QWidget, QLabel, SIGNAL, QGridLayout, Qt


class ParametersWidget(QWidget):

    valueChanged = SIGNAL()

    def __init__(self):
        super().__init__()
        self.buildUI()

    def buildUI(self):
        self.gridlayout = QGridLayout(self)
        self.setLayout(self.gridlayout)

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

    def updateParams(self, parameters):
        i = 0
        for param, value in parameters.items():
            label = QLabel(param)
            label.setAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter
            )
            field_widget = value.getUI()
            value.valueChanged.connect(self.valueChanged.emit)
            self.gridlayout.addWidget(label, i, 0)
            self.gridlayout.addWidget(field_widget, i, 1)
            i += 1

    def clearParams(self):
        for i in reversed(range(self.gridlayout.count())):
            item = self.gridlayout.itemAt(i)
            item.widget().setParent(None)
