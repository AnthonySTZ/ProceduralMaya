from .BaseNode import BaseNode

try:
    import maya.cmds as mc  # type: ignore
except:
    pass


class Merge(BaseNode):
    def __init__(self):
        super().__init__()
        self._name = "Merge"
        self._icon = "merge_icon.png"
        self._num_inputs = 2
        self._num_outputs = 1
        self._parameters = {}

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        if self.input(0) and self.input(1):
            first_xform = self.input(0).commandAtIndex(0)
            second_xform = self.input(1).commandAtIndex(0)
            merged_obj = mc.mergeNode(f=first_xform, s=second_xform)
            return merged_obj

        if self.input(0):
            return self.input(0).commandAtIndex(0)
        if self.input(1):
            return self.input(1).commandAtIndex(0)
