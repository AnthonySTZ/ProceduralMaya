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


def test_should_return_an_untaken_name_for_new_node():
    cube = Cube()  # name: "Cube"
    cube2 = Cube()
    cube2.setName("Cube1")  # name: "Cube1"
    scene = Scene()
    scene.addNode(cube)
    scene.addNode(cube2)
    assert scene.getUntakenName("Cube") == "Cube2"


def test_delete_nodes():
    scene = Scene()
    cube = Cube()
    transform = Transform()
    scene.addNode(cube)
    scene.addNode(transform)
    transform.setInput(0, cube)
