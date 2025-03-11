from PluginLib.CompactQt.Qt import QLineEdit, SIGNAL


class AQDefocusLineEdit(QLineEdit):

    defocus = SIGNAL()

    def __init__(self, text=""):
        super().__init__(text)

    def focusOutEvent(self, e):
        print("Focus Out")
        self.defocus.emit()
        return super().focusOutEvent(e)
