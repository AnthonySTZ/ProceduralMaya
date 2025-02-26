from PluginLib.CompactQt.Qt import QGraphicsPixmapItem
import os
from pathlib import Path


class NodeIcon(QGraphicsPixmapItem):
    def __init__(self, icon_name):
        super().__init__()
        self.buildUI(icon_name)

    def buildUI(self, icon):
        icon_path = Path(
            os.environ["PROCEDURAL_MAYA"], "Core", "Static", "node_icons", icon
        )
        if not icon_path.exists():
            return
