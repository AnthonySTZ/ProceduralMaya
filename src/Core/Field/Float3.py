from PluginLib.CompactQt.Qt import QHBoxLayout, QWidget, QLineEdit, QDoubleValidator


class Float3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def toList(self):
        return [self.x, self.y, self.z]

    def getUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(hbox)

        line_edit_x = QLineEdit(str(self.x))
        line_edit_y = QLineEdit(str(self.y))
        line_edit_z = QLineEdit(str(self.z))

        line_edit_x.setValidator(QDoubleValidator())
        line_edit_y.setValidator(QDoubleValidator())
        line_edit_z.setValidator(QDoubleValidator())

        hbox.addWidget(line_edit_x)
        hbox.addWidget(line_edit_y)
        hbox.addWidget(line_edit_z)

        return widget
