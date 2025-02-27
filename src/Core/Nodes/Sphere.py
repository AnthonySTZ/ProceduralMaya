from .BaseNode import BaseNode
from Core.Field.Float import Float
from Core.Field.Float3 import Float3
from Core.Field.Int import Int

try:
    import maya.cmds as mc  # type: ignore
except:
    pass


class Sphere(BaseNode):
    def __init__(self):
        super().__init__()
        self._name = "Sphere"
        self._icon = "sphere_icon.png"
        self._num_inputs = 0
        self._num_outputs = 1
        self._parameters = {
            "Axis": Float3(0.0, 1.0, 0.0),
            "Radius": Float(1.0),
            "Subdivisions Axis": Int(20),
            "Subdivisions Height": Int(20),
        }

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        axis = self._parameters["Axis"].toList()
        radius = self._parameters["Radius"].value
        sub_a = self._parameters["Subdivisions Axis"].value
        sub_h = self._parameters["Subdivisions Height"].value

        mc.nurbsToPolygonsPref()

        return mc.polySphere(ax=axis, r=radius, sx=sub_a, sy=sub_h)
