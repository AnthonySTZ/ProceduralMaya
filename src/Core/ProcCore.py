def reloadLib():
    from importlib import reload
    import PluginLib.CompactQt.Qt as Qt
    import UI.NodesView as NodesView
    import UI.MainWindow as MainWindow
    import Core.Nodes.NodesInfo as NodesInfos
    import Core.Qt.QtInfo as QtInfo

    reload(Qt)
    reload(QtInfo)
    reload(NodesInfos)
    QtInfo.QtInfo.reloadQtCore()
    NodesInfos.NodesInfo.reloadNodes()
    reload(NodesView)
    reload(MainWindow)


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
