from PluginLib.CompactQt.Qt import QGraphicsView


class NodesGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.buildUI()

    def buildUI(self):
        self.setStyleSheet(
            """
            QGraphicsView{
                background-color: red;
                border: 0;
            }
            """
        )
