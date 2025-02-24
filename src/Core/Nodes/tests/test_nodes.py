from .load_plugin import load_plugin

load_plugin()
from Core.Nodes.Cube import Cube
from Core.Nodes.Transform import Transform


def test_cube_inputs_number_should_be_zero():
    node = Cube()
    assert node.getNumberOfInputs() == 0
