from Lib.CompactQt.Qt import QWidget, QVBoxLayout, QApplication, QDialog
from maya import OpenMayaUI as omui  # type: ignore
from shiboken2 import wrapInstance  # type: ignore


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildUI()

    def buildUI(self):
        self.setWindowTitle("Maya Procedural")
        vbox = QVBoxLayout()
        self.setLayout(vbox)


def createWindow():
    if QApplication.instance():
        # Id any current instances of tool and destroy
        for win in QApplication.allWindows():
            if "Maya Procedural" in win.objectName():
                win.destroy()

    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)

    dialog = MainWindow
    dialog.window = dialog(parent=mayaMainWindow)
    dialog.window.setObjectName(
        str(dialog.__name__)
    )  # code above uses this to ID any existing windows
    print("Show Window")
    dialog.window.show()
