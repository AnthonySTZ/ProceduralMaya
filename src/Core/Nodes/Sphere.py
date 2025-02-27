from .BaseNode import BaseNode
from Core.Field.Float import Float
from Core.Field.Float3 import Float3
from Core.Field.Int import Int

try:
    import maya.mel as mel  # type: ignore
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

        command = self.createSphereMelCommand()
        return mel.eval(command)

    def createSphereMelCommand(self):
        axis = " -ax " + self._parameters["Axis"].toStr()
        radius = " -r " + self._parameters["Radius"].toStr()
        sub_a = " -sx " + self._parameters["Subdivisions Axis"].toStr()
        sub_h = " -sy " + self._parameters["Subdivisions Height"].toStr()

        command = "polySphere" + axis + radius + sub_a + sub_h + ";"
        return command
