from Core.Field.Int import Int


class UnsignedInt(Int):

    def __init__(self, value=0):
        super().__init__(value)
        self._slider_range = [0, 5]

    def userChangedValue(self, line_edit):
        value = line_edit.text()
        if value[0] == "-":
            value = "0"
            line_edit.setText(value)
        self.setValue(value)
        self.setSliderValue(self.value)

    def setValue(self, value):
        prev_value = self.value
        try:
            self.value = max(0, int(value))
        except:
            self.value = 0
        if self.value != prev_value:
            self.valueChanged.emit()
