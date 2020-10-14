import pytest
from .. base_class import BaseProduct



@pytest.fixture
def get_base_class_obj():
    x = BaseProduct("xx", 100, 1)

def test_is_base_exists():
    x = BaseProduct("xx", 100, 1)
    assert hasattr(x, "name")
    #assert BaseProduct

def test_base_class_repr():
    x = BaseProduct("xx", 100, 1)
    assert repr(x) == "xx"