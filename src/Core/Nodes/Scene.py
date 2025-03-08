try:
    import maya.mel as mel  # type: ignore
except:
    pass


class Scene:
    def __init__(self):
        self._nodes = {}
        self._last_mesh = ""
        self._current_render_node = None

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
        if name not in self._nodes:
            return name
        i = 1
        while name + str(i) in self._nodes:
            i += 1
        return name + str(i)

    def renameNode(self, old_name, new_name):
        if old_name not in self._nodes:
            return
        new_name = self.getUntakenName(new_name)
        self._nodes[new_name] = self._nodes.pop(old_name)
        self._nodes[new_name].setName(new_name)
        return new_name

    def getNodes(self):
        return list(self._nodes.values())

    def setRenderNode(self, node):
        self._current_render_node = node
        self.update()

    def update(self):
        print(self._last_mesh)
        if self._last_mesh:
            try:
                print("Last mesh : " + self._last_mesh)
                delete_command = "delete " + self._last_mesh + ";"
                mel.eval(delete_command)
            except Exception as e:
                print(e)

        if self._current_render_node is None:
            return

        print("Rendering")
        try:
            self._last_mesh = self._current_render_node.commandAtIndex(0)
        except Exception as e:
            print(e)
        print("Rendered " + str(self._last_mesh))
        mel.eval("select -clear;")

    def deleteNode(self, node_name):
        if node_name not in self._nodes.keys():
            return

        deleted_node = self._nodes[node_name]

        for node in deleted_node._outputs.keys():
            connection = deleted_node._outputs[node]
            input_index = connection.inputIndex()
            print(input_index)
            del node._inputs[input_index]

        del self._nodes[node_name]
