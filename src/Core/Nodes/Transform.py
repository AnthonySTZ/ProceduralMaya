from .BaseNode import BaseNode
from Core.Field.Float3 import Float3


class Transform(BaseNode):
    def __init__(self):
        super().__init__()
        self._name = "Transform"
        self._num_inputs = 1
        self._num_outputs = 1
        self._parameters = {
            "Translate": Float3(),
            "Rotate": Float3(),
            "Scale": Float3(),
        }
