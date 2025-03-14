from .BaseNode import BaseNode
from Core.Field.UnsignedInt import UnsignedInt

try:
    import maya.cmds as mc  # type: ignore
    import maya.mel as mel  # type: ignore
except:
    pass


class Subdivide(BaseNode):

    def __init__(self):
        super().__init__()
        self._name = "Subdivide"
        self._icon = "subdivide_icon.png"
        self._num_inputs = 1
        self._num_outputs = 1
        self._parameters = {
            "Subdivisions": UnsignedInt(0.0),
        }

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        if self.input(0) is None:
            print("No connection !")
            return

        current_xform = self.input(0).commandAtIndex(0)
        if not mc.objExists(current_xform):
            return ""

        self.subdivideMesh(current_xform)

        return current_xform

    def subdivideMesh(self, xform):
        subd = self._parameters["Subdivisions"].value

        mc.polySmooth(xform, divisions=subd)
