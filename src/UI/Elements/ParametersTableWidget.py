from PluginLib.CompactQt.Qt import QTableWidget, QLabel, SIGNAL


class ParametersTableWidget(QTableWidget):

    valueChanged = SIGNAL()

    def __init__(self, parameters):
        super().__init__(len(parameters), 2)
        self._parameters = parameters
        self.buildUI()

    def buildUI(self):

        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)

        i = 0
        for param, value in self._parameters.items():
            label = QLabel(param)
            field_widget = value.getUI()
            value.valueChanged.connect(self.valueChanged.emit)
            self.setCellWidget(i, 0, label)
            self.setCellWidget(i, 1, field_widget)
            i += 1

        self.resizeColumnsToContents()
