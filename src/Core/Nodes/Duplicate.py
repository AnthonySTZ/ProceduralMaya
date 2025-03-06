from .BaseNode import BaseNode
from Core.Field.Float3 import Float3
from Core.Field.UnsignedInt import UnsignedInt
from Core.Field.Types import Types

try:
    import maya.cmds as mc  # type: ignore
    import maya.mel as mel  # type: ignore
except:
    pass


class Duplicate(BaseNode):

    ScaRotTsl = 0
    ScaTslRot = 1
    RotScaTsl = 2
    RotTslSca = 3
    TslScaRot = 4
    TslRotSca = 5

    def __init__(self):
        super().__init__()
        self._name = "Duplicate"
        self._icon = "duplicate_icon.png"
        self._num_inputs = 1
        self._num_outputs = 1
        self._parameters = {
            "Amount": UnsignedInt(0),
            "Translate": Float3(0.0, 0.0, 0.0),
            "Rotate": Float3(0.0, 0.0, 0.0),
            "Scale": Float3(1.0, 1.0, 1.0),
        }

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        if self.input(0) is None:
            print("No connection !")
            return

        current_xform = self.input(0).commandAtIndex(0)
        dup_obj = self.duplicateMesh(current_xform)

        return dup_obj

    def duplicateMesh(self, xform):
        amount = self._parameters["Amount"].value
        translate = self._parameters["Translate"].toList()
        rotate = self._parameters["Rotate"].toList()
        scale = self._parameters["Scale"].toList()
        obj = mc.duplicateNode(
            obj=xform,
            a=amount,
            tx=translate[0],
            ty=translate[1],
            tz=translate[2],
            rx=rotate[0],
            ry=rotate[1],
            rz=rotate[2],
            sx=scale[0],
            sy=scale[1],
            sz=scale[2],
        )
        return obj
