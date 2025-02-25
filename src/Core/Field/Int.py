from PluginLib.CompactQt.Qt import QHBoxLayout, QWidget, QLineEdit, QIntValidator


class Int:
    def __init__(self, value=0):
        self.value = value

    def getUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(hbox)

        line_edit = QLineEdit(str(self.value))
        line_edit.setValidator(QIntValidator())
        hbox.addWidget(line_edit)

        return widget
