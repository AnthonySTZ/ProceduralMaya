from .BaseNode import BaseNode
from Core.Field.UnsignedFloat import UnsignedFloat

try:
    import maya.cmds as mc  # type: ignore
except:
    pass


class Cube(BaseNode):
    def __init__(self):
        super().__init__()
        self._name = "Cube"
        self._icon = "cube_icon.png"
        self._num_inputs = 0
        self._num_outputs = 1
        self._parameters = {
            "width": UnsignedFloat(1.0),
            "height": UnsignedFloat(1.0),
            "depth": UnsignedFloat(1.0),
        }

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        obj = self.createCube()
        return obj

    def createCube(self):
        width = self._parameters["width"].value
        height = self._parameters["height"].value
        depth = self._parameters["depth"].value
        cube_obj = mc.polyCube(w=width, h=height, d=depth)[0]
        return cube_obj
