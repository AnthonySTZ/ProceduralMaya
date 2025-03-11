from Core.Field.Float import Float


class UnsignedFloat(Float):

    def __init__(self, value=0):
        super().__init__(value)
        self._slider_range = [0, 5]

    def userChangedValue(self, line_edit):
        value = line_edit.text()
        if value[0] == "-":
            value = "0.0"
            line_edit.setText(value)
        self.setValue(value)
        self.setSliderValue(self.value)

    def setValue(self, value):
        try:
            self.value = max(0, float(value))
        except:
            self.value = 0
        self.valueChanged.emit()
