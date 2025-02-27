from .BaseNode import BaseNode
from Core.Field.Float import Float

try:
    import maya.mel as mel  # type: ignore
except:
    pass


class Cube(BaseNode):
    def __init__(self):
        super().__init__()
        self._name = "Cube"
        self._icon = "cube_icon.png"
        self._num_inputs = 0
        self._num_outputs = 1
        self._parameters = {
            "width": Float(1.0),
            "height": Float(1.0),
            "depth": Float(1.0),
        }

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        command = self.createCubeMelCommand()
        return mel.eval(command)

    def createCubeMelCommand(self):
        width = " -w " + self._parameters["width"].toStr()
        height = " -h " + self._parameters["height"].toStr()
        depth = " -d " + self._parameters["depth"].toStr()

        command = "polyCube" + width + height + depth + ";"
        return command
