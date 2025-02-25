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

        line_edit_x.returnPressed.connect(lambda le=line_edit_x: self.setX(le.text()))
        line_edit_y.returnPressed.connect(lambda le=line_edit_y: self.setY(le.text()))
        line_edit_z.returnPressed.connect(lambda le=line_edit_z: self.setZ(le.text()))

        hbox.addWidget(line_edit_x)
        hbox.addWidget(line_edit_y)
        hbox.addWidget(line_edit_z)

        return widget

    def setX(self, value):
        self.x = float(value)
        print(value)
        self.valueChanged.emit()

    def setY(self, value):
        self.y = float(value)
        print(value)
        self.valueChanged.emit()

    def setZ(self, value):
        self.z = float(value)
        print(value)
        self.valueChanged.emit()
