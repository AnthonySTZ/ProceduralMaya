from importlib import reload
import PluginLib.CompactQt.Qt as Qt
import UI.MainWindow as MainWindow

reload(Qt)
reload(MainWindow)


from PluginLib.CompactQt.Qt import QApplication, QWidget
from UI.MainWindow import MainWindow

from maya import OpenMayaUI as omui  # type: ignore
from shiboken2 import wrapInstance  # type: ignore


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
