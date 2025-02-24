from .load_plugin import load_plugin

load_plugin()
from Core.Logic.logics import *


def test_evenly_distribute_point_on_line():
    length = 50
    points = 5
    assert evenly_distribute_point_on_line(length, points) == [5, 15, 25, 35, 45]
