from Core.Field.Float import Float


class UnsignedFloat(Float):

    def __init__(self, value=0):
        super().__init__(value)

    def userChangedValue(self, line_edit):
        value = line_edit.text()
        if value[0] == "-":
            value = value[1:]
            line_edit.setText(value)
        self.setValue(value)

    def setValue(self, value):
        try:
            self.value = abs(float(value))
        except:
            self.value = 0
        self.valueChanged.emit()
