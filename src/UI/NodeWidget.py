from PluginLib.CompactQt.Qt import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    Qt,
    QPoint,
    SIGNAL,
)

from UI.IOButton import IOButton
from UI.NodeTitleWidget import NodeTitleWidget


class NodeWidget(QWidget):

    inputClicked = SIGNAL(IOButton, int)
    outputClicked = SIGNAL(IOButton, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._position = QPoint(0, 0)
        self._is_moving = False
        self._mouse_offset = QPoint(0, 0)
        self._node = None
        self.buildUI()

    def buildUI(self):
        self.setStyleSheet(
            """
            QWidget {
                background-color: transparent;
            }
            """
        )
        main_vbox = QVBoxLayout()
        main_vbox.setContentsMargins(0, 0, 0, 0)
        main_vbox.setSpacing(2)
        self.setLayout(main_vbox)

        self.inputs_hbox = QHBoxLayout()
        self.inputs_hbox.setContentsMargins(0, 0, 0, 0)
        self.inputs_widget = QWidget()
        self.inputs_widget.setLayout(self.inputs_hbox)
        main_vbox.addWidget(self.inputs_widget)

        self.title_widget = NodeTitleWidget()
        main_vbox.addWidget(self.title_widget)

        self.outputs_hbox = QHBoxLayout()
        self.outputs_hbox.setContentsMargins(0, 0, 0, 0)
        self.outputs_widget = QWidget()
        self.outputs_widget.setLayout(self.outputs_hbox)
        main_vbox.addWidget(self.outputs_widget)

    def setNode(self, node):
        self._node = node
        self.inputs_widget.setHidden(True)
        self.outputs_widget.setHidden(True)

        self.title_widget.setNodeTitle(node.getName())
        self.setInputButtons(node)
        self.setOutputButtons(node)

    def getNode(self):
        return self._node

    def setInputButtons(self, node):
        inputs_number = node.getNumberOfInputs()
        if inputs_number > 0:
            self.inputs_widget.setHidden(False)

        for idx in range(inputs_number):
            input_btn = IOButton()
            input_btn.setButtonSize(8)
            input_btn.clicked.connect(lambda _: self.inputClicked.emit(input_btn, idx))
            self.inputs_hbox.addWidget(input_btn)

    def setOutputButtons(self, node):
        outputs_number = node.getNumberOfOutputs()
        if outputs_number > 0:
            self.outputs_widget.setHidden(False)

        for idx in range(outputs_number):
            output_btn = IOButton()
            output_btn.setButtonSize(8)
            output_btn.clicked.connect(
                lambda _: self.outputClicked.emit(output_btn, idx)
            )
            self.outputs_hbox.addWidget(output_btn)

    def setPosition(self, position):
        self._position = position
        self.moveToPosition()

    def getPosition(self):
        return self._position

    def moveToPosition(self):
        self.move(self._position)

    def mousePressEvent(self, event):
        if (
            event.buttons() == Qt.MouseButton.LeftButton
            and self.title_widget.underMouse()
        ):
            self._is_moving = True
            self._mouse_offset = event.pos()
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, a0):
        self._is_moving = False
        return super().mouseReleaseEvent(a0)

    def mouseMoveEvent(self, event):
        if self._is_moving:
            position = event.pos() - self._mouse_offset
            self.setPosition(
                self.parent().mapFromGlobal(self.title_widget.mapToGlobal(position))
            )

        return super().mouseMoveEvent(event)
