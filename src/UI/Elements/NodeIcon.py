from PluginLib.CompactQt.Qt import QGraphicsPixmapItem, QPixmap, Qt
import os
from pathlib import Path


class NodeIcon(QGraphicsPixmapItem):
    def __init__(self, icon_name, size):
        super().__init__()
        self.buildUI(icon_name, size)

    def buildUI(self, icon, size):
        icon_path = Path(
            os.environ["PROCEDURAL_MAYA"], "src", "Core", "Static", "node_icons", icon
        )
        if not icon_path.exists():
            print(icon_path.as_posix() + " does not exists !")
            return

        pixmap = QPixmap(icon_path.as_posix())
        scaled_pixmap = pixmap.scaled(
            size,
            size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.setPixmap(scaled_pixmap)
