class Scene:
    def __init__(self):
        self._nodes = {}

    def addNode(self, node):
        """
        Adds a node to the scene. Renames the node if a node with the same name already exists in the scene
        """
        node_name = node.getName()
        if node_name not in self._nodes:
            self._nodes[node_name] = node
            return

        new_name = self.getUntakenName(node_name)
        node.setName(new_name)
        self._nodes[new_name] = node

    def getUntakenName(self, name):
        """
        Tries every possibilites of name (pattern: name1, name2,...) and return the first that not exists in the scene.
        """
        i = 1
        while name + str(i) in self._nodes:
            i += 1
        return name + str(i)

    def getNodes(self):
        return list(self._nodes.values())

    def setRenderNode(self, node):
        print("Set Render to " + node.getName())
