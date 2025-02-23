class Scene:
    def __init__(self):
        self._nodes = {}

    def addNode(self, node):
        node_name = node.getName()
        if node_name not in self._nodes:
            self._nodes[node_name] = node
            return

        new_name = self.getUntakenName(node_name)
        node.setName(new_name)
        self._nodes[new_name] = node

    def getUntakenName(self, name):
        i = 1
        while name + str(i) in self._nodes:
            i += 1
        return name + str(i)
