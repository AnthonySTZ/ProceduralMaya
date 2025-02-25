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

    def getParameters(self):
        return self._parameters

    def setParameters(self, key, value):
        self._parameters[key] = value

    """ INPUTS AND OUTPUTS """

    def getNumberOfInputs(self):
        return self._num_inputs

    def getNumberOfOutputs(self):
        return self._num_outputs

    def setInput(self, input_index, input_node, output_index=0):
        """
        Creates a connection between this node and another.

        input_index : index of the input of this node.
        input_node : node that the connection comes from.
        output_index : index of the input of the input_node.
        """

        if input_index >= self._num_inputs:  # input out of range
            print("Not enough inputs for " + self.getName() + " !")
            return

        if input_node is None:
            if input_index in self._inputs:
                del self._inputs[input_index]
            return

        if output_index >= input_node.getNumberOfOutputs():  # input out of range
            print("Not enough outputs for " + input_node.getName() + " !")
            return

        connection = NodeConnection(input_node, output_index, self, input_index)
        self._inputs[input_index] = connection

    def inputConnection(self, index):
        """
        Returns the NodeConnection at input index.
        If no input connection found, returns None.
        """

        if index not in self._inputs:
            return None

        return self._inputs[index]

    def input(self, index):
        """
        Returns the Node at input index.
        If no input connection found, returns None.
        """

        if index not in self._inputs:
            return None

        return self._inputs[index].inputNode()

    """ CORE """

    def commandAtIndex(self, index):
        raise NotImplementedError("Command not implemented")
