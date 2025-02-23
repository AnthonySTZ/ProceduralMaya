class Scene:
    def __init__(self):
        self._nodes = {}

    def addNode(self, node):
        node_name = node.getName()
        if node_name not in self._nodes:
            self._nodes[node_name] = node
