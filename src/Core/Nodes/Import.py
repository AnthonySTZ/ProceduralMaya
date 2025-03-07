from .BaseNode import BaseNode
from Core.Field.String import String

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
        self._parameters = {"MeshName": String()}

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        obj = self.getMesh()
        return obj

    def getMesh(self):
        mesh = self._parameters["MeshName"].value
        if mc.objExists(mesh):
            dup_mesh = mc.duplicate(mesh)[0]
            mc.showHidden(dup_mesh)
            return dup_mesh
        return ""
