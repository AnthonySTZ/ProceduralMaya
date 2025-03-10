from .BaseNode import BaseNode
from Core.Field.UnsignedFloat import UnsignedFloat
from Core.Field.UnsignedInt import UnsignedInt

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
            "Sub Width": UnsignedInt(1),
            "Sub Height": UnsignedInt(1),
            "Sub Depth": UnsignedInt(1),
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
        sub_w = self._parameters["Sub Width"].value
        sub_h = self._parameters["Sub Height"].value
        sub_d = self._parameters["Sub Depth"].value
        cube_obj = mc.polyCube(
            w=width,
            h=height,
            d=depth,
            subdivisionsWidth=sub_w,
            subdivisionsHeight=sub_h,
            subdivisionsDepth=sub_d,
        )[0]
        return cube_obj
