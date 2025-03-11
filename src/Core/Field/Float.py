from PluginLib.CompactQt.Qt import (
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QDoubleValidator,
    SIGNAL,
    QSizePolicy,
)
from Core.Field.Field import Field
from Core.Qt.AQJumpSlider import AQJumpSlider


class Float(Field):
    valueChanged = SIGNAL()

    def __init__(self, value=0.0):
        super().__init__()
        self.value = value
        self._slider_range = [-5, 5]

    def getUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(hbox)

        self._line_edit = QLineEdit(str(self.value))
        self._line_edit.setValidator(QDoubleValidator())
        self._line_edit.setFixedWidth(50)
        self._line_edit.returnPressed.connect(
            lambda le=self._line_edit: self.userChangedValue(le)
        )
        hbox.addWidget(self._line_edit)

        self._slider = AQJumpSlider()
        self._slider.valueChanged.connect(self.sliderValueChanged)
        hbox.addWidget(self._slider)

        return widget

    def toStr(self):
        return str(self.value)

    def sliderValueChanged(self, value):
        max = self._slider.maximum()
        min = self._slider.minimum()
        fit_min = self._slider_range[0]
        fit_max = self._slider_range[1]

        fitted_value = round(
            (value - min) / (max - min) * (fit_max - fit_min) + fit_min, 2
        )
        self._line_edit.setText(str(fitted_value))
        self.setValue(fitted_value)

    def userChangedValue(self, line_edit):
        self.setValue(line_edit.text())

    def setValue(self, value):
        try:
            self.value = float(value)
        except:
            self.value = 0
        self.valueChanged.emit()
