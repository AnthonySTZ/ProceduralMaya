from .BaseNode import BaseNode
from Core.Field.Float3 import Float3
from Core.Field.Float import Float

try:
    import maya.cmds as mc  # type: ignore
    import maya.mel as mel  # type: ignore
except:
    pass


class Twist(BaseNode):

    def __init__(self):
        super().__init__()
        self._name = "Twist"
        self._icon = "twist_icon.png"
        self._num_inputs = 1
        self._num_outputs = 1
        self._parameters = {
            "Start Angle": Float(0.0),
            "End Angle": Float(0.0),
            "Low Bound": Float(-1.0),
            "High Bound": Float(1.0),
            "Rotation": Float3(0.0, 0.0, 0.0),
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
        self.twistMesh(current_xform)

        return current_xform

    def twistMesh(self, xform):
        start_angle = self._parameters["Start Angle"].value
        end_angle = self._parameters["End Angle"].value
        low_bound = self._parameters["Low Bound"].value
        high_bound = self._parameters["High Bound"].value

        rotation = self._parameters["Rotation"].toList()

        twist_obj = mc.nonLinear(
            xform,
            type="bend",
            startAngle=start_angle,
            endAngle=end_angle,
            lowBound=low_bound,
            highBound=high_bound,
        )
        mc.xform(twist_obj, rotation=rotation)
        mc.select(xform)
        mel.eval("DeleteHistory;")
