class NodesInfo:

    @staticmethod
    def getNodes():
        from Core.Nodes.Cube import Cube

        nodes = [
            Cube,
        ]
        return nodes

    @staticmethod
    def reloadNodes():
        from importlib import reload
        import Core.Nodes.Cube as Cube

        reload(Cube)
