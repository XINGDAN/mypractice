#! /usr/bin/env python
#coding=utf-8

import pytest
from add import add_method

@pytest.mark.parametrize("x,y",[
    (3+5,8),
    (2+4,6),
    (6*9,42),
])
def test_add_by_paras(x,y):
    assert add_method(x,y) == x + y


