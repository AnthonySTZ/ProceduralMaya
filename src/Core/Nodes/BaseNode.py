import abc
from Core.Nodes.NodeConnection import NodeConnection


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

    def setInput(self, input_index, input_node, output_index=0):
        if input_index >= self._num_inputs:
            print("Not enough inputs for " + self.getName() + " !")
            return

        if output_index >= input_node.getNumberOfOutputs():
            print("Not enough outputs for " + input_node.getName() + " !")
            return

        self._inputs[input_index] = NodeConnection(
            self, input_index, input_node, output_index
        )

    def inputConnection(self, index):
        if index not in self._inputs:
            return None

        return self._inputs[index]

    def input(self, index):
        if index not in self._inputs:
            return None

        return self._inputs[index].inputNode()
