from PluginLib.CompactQt.Qt import (
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QIntValidator,
    SIGNAL,
)
from Core.Field.Field import Field
from Core.Qt.AQJumpSlider import AQJumpSlider
from Core.Logic import logics


class Int(Field):
    valueChanged = SIGNAL()

    def __init__(self, value=0):
        super().__init__()
        self.value = value
        self._slider_range = [-5, 5]

    def getUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(hbox)

        self._line_edit = QLineEdit(str(self.value))
        self._line_edit.setValidator(QIntValidator())
        self._line_edit.setFixedWidth(50)
        self._line_edit.returnPressed.connect(
            lambda le=self._line_edit: self.userChangedValue(le)
        )
        hbox.addWidget(self._line_edit)

        self._slider = AQJumpSlider()
        self._slider.userChangedValue.connect(self.sliderValueChanged)
        hbox.addWidget(self._slider)

        return widget

    def sliderValueChanged(self, value):
        max = self._slider.maximum()
        min = self._slider.minimum()
        fit_min = self._slider_range[0]
        fit_max = self._slider_range[1]

        fitted_value = int(logics.fit_value(value, min, max, fit_min, fit_max))
        self._line_edit.setText(str(fitted_value))
        self.setSliderValue(fitted_value)
        self.userChangedValue(self._line_edit)

    def setSliderValue(self, value):
        max = self._slider.maximum()
        min = self._slider.minimum()
        fit_min = self._slider_range[0]
        fit_max = self._slider_range[1]
        slider_value = logics.fit_value(value, fit_min, fit_max, min, max)
        self._slider.setValue(int(slider_value))

    def userChangedValue(self, line_edit):
        self.setValue(line_edit.text())
        self.setSliderValue(self.value)

    def toStr(self):
        return str(self.value)

    def setValue(self, value):
        try:
            self.value = int(value)
        except:
            self.value = 0
        self.valueChanged.emit()
