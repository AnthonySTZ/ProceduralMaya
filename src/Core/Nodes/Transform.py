from .BaseNode import BaseNode
from Core.Field.Float3 import Float3
from Core.Field.Types import Types

try:
    import maya.cmds as mc  # type: ignore
    import maya.mel as mel  # type: ignore
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
        self._icon = "transform_icon.png"
        self._num_inputs = 1
        self._num_outputs = 1
        self._parameters = {
            "Transform Order": Types(
                "Scale Rot Trans",
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

        current_xform = self.input(0).commandAtIndex(0)

        shapes = mc.listRelatives(current_xform, shapes=True)
        order = self._parameters["Transform Order"].getValue()
        mel.eval("select -r " + " ".join(shapes))
        self.transformBaseOnOrder(shapes, order)

        return current_xform

    def transformBaseOnOrder(self, shapes, order):
        translate_command = self.createTranslateCommand()
        rotate_command = self.createRotateCommand()
        scale_command = self.createScaleCommand()

        if order == self.ScaRotTsl:
            mel.eval(scale_command)
            mel.eval(rotate_command)
            mel.eval(translate_command)
            return

        if order == self.ScaTslRot:
            mel.eval(scale_command)
            mel.eval(translate_command)
            mel.eval(rotate_command)
            return

        if order == self.RotScaTsl:
            mel.eval(rotate_command)
            mel.eval(scale_command)
            mel.eval(translate_command)
            return

        if order == self.RotTslSca:
            mel.eval(rotate_command)
            mel.eval(translate_command)
            mel.eval(scale_command)
            return

        if order == self.TslScaRot:
            mel.eval(translate_command)
            mel.eval(scale_command)
            mel.eval(rotate_command)
            return

        if order == self.TslRotSca:
            mel.eval(translate_command)
            mel.eval(rotate_command)
            mel.eval(scale_command)
            return

    def createTranslateCommand(self):
        translate = " -t " + self._parameters["Translate"].toStr()
        command = "polyMoveVertex" + translate + ";"
        return command

    def createRotateCommand(self):
        rotate = " -ro " + self._parameters["Rotate"].toStr()
        command = "polyMoveVertex" + rotate + ";"
        return command

    def createScaleCommand(self):
        scale = " -s " + self._parameters["Scale"].toStr()
        command = "polyMoveVertex" + scale + ";"
        return command
