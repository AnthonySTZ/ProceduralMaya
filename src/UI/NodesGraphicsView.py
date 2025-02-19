from PluginLib.CompactQt.Qt import QGraphicsView


class NodesGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        self._scene = scene
        super().__init__(scene, parent)
