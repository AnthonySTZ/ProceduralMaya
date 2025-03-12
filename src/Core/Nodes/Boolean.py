from .BaseNode import BaseNode
from Core.Field.Types import Types

try:
    import maya.cmds as mc  # type: ignore
except:
    pass


class Boolean(BaseNode):

    UNION = 1
    DIFFERENCE = 2
    INTERSECTION = 3

    def __init__(self):
        super().__init__()
        self._name = "Boolean"
        self._icon = "boolean_icon.png"
        self._num_inputs = 2
        self._num_outputs = 1
        self._parameters = {
            "Operation": Types(
                "Union",
                {
                    "Union": self.UNION,
                    "Difference": self.DIFFERENCE,
                    "Intersection": self.INTERSECTION,
                },
            )
        }

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        if self.input(0) and self.input(1):
            first_xform = self.input(0).commandAtIndex(0)
            second_xform = self.input(1).commandAtIndex(0)
            if not mc.objExists(first_xform) and not mc.objExists(second_xform):
                return ""
            if not mc.objExists(first_xform):
                return second_xform
            if not mc.objExists(second_xform):
                return first_xform
            merged_obj = mc.mergeNode(f=first_xform, s=second_xform)
            return merged_obj

        if self.input(0):
            return self.input(0).commandAtIndex(0)
        if self.input(1):
            return self.input(1).commandAtIndex(0)
