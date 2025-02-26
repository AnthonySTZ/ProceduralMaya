from .BaseNode import BaseNode
from Core.Field.Float3 import Float3
from Core.Field.Types import Types

try:
    import maya.cmds as mc  # type: ignore
except:
    pass


class Transform(BaseNode):

    ScaRotTsl = 0
    ScaTslRot = 1
    RotScaTsl = 2
    RotTslSca = 3
    TslScaRot = 4
    TslRotSca = 5

    def __init__(self):
        super().__init__()
        self._name = "Transform"
        self._num_inputs = 1
        self._num_outputs = 1
        self._parameters = {
            "Transform Order": Types(
                "TslRotSca",
                {
                    "Scale Rot Trans": self.ScaRotTsl,
                    "Scale Trans Rot": self.ScaTslRot,
                    "Rot Scale Trans": self.RotScaTsl,
                    "Rot Trans Scale": self.RotTslSca,
                    "Trans Scale Rot": self.TslScaRot,
                    "Trans Rot Scale": self.TslRotSca,
                },
            ),
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

        print(self._parameters["Transform Order"].getValue())

        current_xform = self.input(0).commandAtIndex(0)
        shapes = mc.listRelatives(current_xform, shapes=True)

        translate = self._parameters["Translate"].toList()
        rotate = self._parameters["Rotate"].toList()
        scale = self._parameters["Scale"].toList()

        mc.polyMoveVertex(shapes, t=translate, ro=rotate, s=scale)
        return current_xform
