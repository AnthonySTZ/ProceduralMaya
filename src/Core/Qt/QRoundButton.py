from PluginLib.CompactQt.Qt import QPushButton


class QRoundButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setButtonSize(self, size):
        self.setFixedSize(size, size)
        self.setStyleSheet(
            "QPushButton{border-radius:"
            + str(size / 2)
            + ";background-color: #c9c9c9;}"
            + "QPushButton:hover{background-color: #e0e0e0;}"
        )
