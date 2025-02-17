import abc


class BaseNode:
    def __init__(self):
        self._name = "Node"
        self._num_inputs = 0
        self._num_outputs = 0
        self._inputs = {}
        self._outputs = {}
        self._parameters = {}

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getNumberOfInputs(self):
        return self._num_inputs

    def getNumberOfOutputs(self):
        return self._num_outputs

    def getParameters(self):
        return self._parameters

    def setParameters(self, key, value):
        self._parameters[key] = value

    @abc.abstractmethod
    def getOutput(self, output_index):
        raise NotImplementedError("Output not implemented")
