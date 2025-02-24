from .load_plugin import load_plugin

load_plugin()
from Core.Nodes.Cube import Cube
from Core.Nodes.Transform import Transform


def test_cube_inputs_number_should_be_zero():
    node = Cube()
    assert node.getNumberOfInputs() == 0


def test_cube_outputs_number_should_be_one():
    node = Cube()
    assert node.getNumberOfOutputs() == 1


def test_should_return_the_correct_input_node():
    cube = Cube()
    transform = Transform()
    transform.setInput(0, cube)
    assert transform.input(0) == cube


def test_should_return_None_when_getting_empty_input():
    cube = Cube()
    assert cube.input(0) == None
