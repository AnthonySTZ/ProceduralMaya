from PluginLib.CompactQt.Qt import (
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QDoubleValidator,
    QObject,
    SIGNAL,
)


class Float3(QObject):

    valueChanged = SIGNAL()

    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__()
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

        line_edit_x.textEdited.connect(lambda text: self.setX(text))
        line_edit_y.textEdited.connect(lambda text: self.setY(text))
        line_edit_z.textEdited.connect(lambda text: self.setZ(text))

        hbox.addWidget(line_edit_x)
        hbox.addWidget(line_edit_y)
        hbox.addWidget(line_edit_z)

        return widget

    def setX(self, value):
        try:
            self.x = float(value)
        except:
            self.x = 0
        self.valueChanged.emit()

    def setY(self, value):
        try:
            self.y = float(value)
        except:
            self.y = 0
        self.valueChanged.emit()

    def setZ(self, value):
        try:
            self.z = float(value)
        except:
            self.z = 0
        self.valueChanged.emit()
