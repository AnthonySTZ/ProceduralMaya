from Core.Qt.AQMovableRectItem import AQMovableRectItem


class NodeRect(AQMovableRectItem):
    WIDTH = 90
    HEIGHT = 25

    def __init__(self, x, y):
        super().__init__(x, y, self.WIDTH, self.HEIGHT)
