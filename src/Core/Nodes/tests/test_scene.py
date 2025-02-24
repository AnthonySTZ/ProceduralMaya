from .load_plugin import load_plugin

load_plugin()
from Core.Nodes.Cube import Cube
from Core.Nodes.Transform import Transform
from Core.Nodes.Scene import Scene


def test_should_return_list_of_nodes_in_scene():
    cube = Cube()
    transform = Transform()
    scene = Scene()
    scene.addNode(cube)
    scene.addNode(transform)
    assert scene.getNodes() == [cube, transform]
