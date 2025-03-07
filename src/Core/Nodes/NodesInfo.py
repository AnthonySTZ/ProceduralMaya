class NodesInfo:

    @staticmethod
    def getNodes():
        from Core.Nodes.Cube import Cube
        from Core.Nodes.Sphere import Sphere
        from Core.Nodes.Transform import Transform
        from Core.Nodes.Duplicate import Duplicate
        from Core.Nodes.Merge import Merge
        from Core.Nodes.Null import Null
        from Core.Nodes.Import import Import

        nodes = [Cube, Sphere, Transform, Duplicate, Merge, Null, Import]
        return nodes
