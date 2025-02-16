from PluginLib.CompactQt.Qt import QAction


class QDataAction(QAction):
    def __init__(self, parent):
        super().__init__(parent)
        self._data = None

    def setUserData(self, data):
        self._data = data

    def getUserData(self):
        return self._data
