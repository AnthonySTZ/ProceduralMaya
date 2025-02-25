from .BaseNode import BaseNode
from Core.Field.Float import Float


class Cube(BaseNode):
    def __init__(self):
        super().__init__()
        self._name = "Cube"
        self._num_inputs = 0
        self._num_outputs = 1
        self._parameters = {"width": Float(), "height": Float(), "depth": Float()}
