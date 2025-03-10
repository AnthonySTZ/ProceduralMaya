from .BaseNode import BaseNode
from Core.Field.Float3 import Float3
from Core.Field.Float import Float

try:
    import maya.cmds as mc  # type: ignore
    import maya.mel as mel  # type: ignore
except:
    pass


class Bend(BaseNode):

    def __init__(self):
        super().__init__()
        self._name = "Bend"
        self._icon = "bend_icon.png"
        self._num_inputs = 1
        self._num_outputs = 1
        self._parameters = {
            "Curvature": Float(0.0),
            "Low Bound": Float(-1.0),
            "High Bound": Float(1.0),
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
        self.bendMesh(current_xform)

        return current_xform

    def bendMesh(self, xform):
        obj = xform
        return obj
