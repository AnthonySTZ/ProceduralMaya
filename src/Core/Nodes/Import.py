from .BaseNode import BaseNode
from Core.Field.UnsignedFloat import UnsignedFloat

try:
    import maya.cmds as mc  # type: ignore
except:
    pass


class Import(BaseNode):
    def __init__(self):
        super().__init__()
        self._name = "Import"
        self._icon = "import_icon.png"
        self._num_inputs = 0
        self._num_outputs = 1
        self._parameters = {}

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        obj = self.getMesh()
        return obj

    def getMesh(self):
        return ""
