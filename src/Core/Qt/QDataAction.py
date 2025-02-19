from PluginLib.CompactQt.Qt import QAction


class QDataAction(QAction):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self._data = None

    def setUserData(self, data):
        self._data = data

    def getUserData(self):
        return self._data
