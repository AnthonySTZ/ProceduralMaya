from PluginLib.CompactQt.Qt import QGraphicsEllipseItem


class AQClickableEllipseItem(QGraphicsEllipseItem):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__(pos_x, pos_y, width, height)
