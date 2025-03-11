from PluginLib.CompactQt.Qt import (
    QHBoxLayout,
    QWidget,
    QDoubleValidator,
    SIGNAL,
)
from Core.Field.Field import Field
from Core.Qt.AQDefocusLineEdit import AQDefocusLineEdit


class Float3(Field):

    valueChanged = SIGNAL()

    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    def toList(self):
        return [self.x, self.y, self.z]

    def toStr(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)

    def getUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(hbox)

        line_edit_x = AQDefocusLineEdit(str(self.x))
        line_edit_y = AQDefocusLineEdit(str(self.y))
        line_edit_z = AQDefocusLineEdit(str(self.z))

        line_edit_x.setValidator(QDoubleValidator())
        line_edit_y.setValidator(QDoubleValidator())
        line_edit_z.setValidator(QDoubleValidator())

        line_edit_x.returnPressed.connect(lambda le=line_edit_x: self.setX(le.text()))
        line_edit_y.returnPressed.connect(lambda le=line_edit_y: self.setY(le.text()))
        line_edit_z.returnPressed.connect(lambda le=line_edit_z: self.setZ(le.text()))

        line_edit_x.defocus.connect(lambda le=line_edit_x: self.setX(le.text()))
        line_edit_y.defocus.connect(lambda le=line_edit_y: self.setY(le.text()))
        line_edit_z.defocus.connect(lambda le=line_edit_z: self.setZ(le.text()))

        hbox.addWidget(line_edit_x)
        hbox.addWidget(line_edit_y)
        hbox.addWidget(line_edit_z)

        return widget

    def setX(self, value):
        try:
            self.x = float(value)
        except:
            self.x = 0.0
        self.valueChanged.emit()

    def setY(self, value):
        try:
            self.y = float(value)
        except:
            self.y = 0.0
        self.valueChanged.emit()

    def setZ(self, value):
        try:
            self.z = float(value)
        except:
            self.z = 0.0
        self.valueChanged.emit()
