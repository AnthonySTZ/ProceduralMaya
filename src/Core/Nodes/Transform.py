from .BaseNode import BaseNode


class Transform(BaseNode):
    def __init__(self):
        super().__init__()
        self._name = "Transform"
        self._num_inputs = 3
        self._num_outputs = 2
        self._parameters = {"Translate": 0.0, "Rotate": 0.0, "Scale": 1.0}
