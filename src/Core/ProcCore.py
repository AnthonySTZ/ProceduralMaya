def reloadLib():
    import os
    import sys
    import glob
    import importlib
    from pathlib import Path

    print("Reloading all Modules")

    import_folder = Path(os.environ["PROCEDURAL_MAYA"]).as_posix() + "/src/"
    for src_file in glob.glob(import_folder + "**/*.py", recursive=True):
        relative_name_to_import_folder = src_file[len(import_folder) :]
        name = relative_name_to_import_folder.replace("\\", ".")[:-3]

        if name != "main" and name != "ProcCore":
            importlib.import_module(name)
            importlib.reload(sys.modules[name])
            importlib.import_module(name)


def createWindow():
    from PluginLib.CompactQt.Qt import QApplication, QWidget
    from UI.MainWindow import MainWindow

    if QApplication.instance():
        # Id any current instances of tool and destroy
        for win in QApplication.allWindows():
            if "Maya Procedural" in win.objectName():
                win.destroy()

    LOAD_IN_MAYA = False

    try:
        from maya import OpenMayaUI as omui  # type: ignore
        from shiboken2 import wrapInstance  # type: ignore

        mayaMainWindowPtr = omui.MQtUtil.mainWindow()
        mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)

        LOAD_IN_MAYA = True
    except:
        print("Run plugin as standalone")

    if LOAD_IN_MAYA:
        dialog = MainWindow
        dialog.window = dialog(parent=mayaMainWindow)
        dialog.window.setObjectName(
            str(dialog.__name__)
        )  # code above uses this to ID any existing windows
        print("Show Window")
        dialog.window.show()
    else:
        app = QApplication([])
        window = MainWindow()
        window.setStyleSheet(
            """
            QWidget {
                background-color: #424242;
                color: #c2c2c2;
            }
            """
        )
        window.show()
        app.exec()
