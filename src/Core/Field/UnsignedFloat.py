from Core.Field.Float import Float


class UnsignedFloat(Float):

    def __init__(self, value=0):
        super().__init__(value)

    def setValue(self, value):
        try:
            self.value = abs(float(value))
        except:
            self.value = 0
        self.valueChanged.emit()
