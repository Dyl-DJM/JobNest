import pytest

from core.utils import Singleton, SingletonException

class SingletonTest(Singleton):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b


def test_should_create_instance():
    singleton = SingletonTest(1, 2)
    assert singleton

def test_should_raise_singleton_exception():
    with pytest.raises(SingletonException) as singleton_exception:
        singleton2 = SingletonTest(3, 4)
    assert str(singleton_exception.value) == "Another instance of the singleton is already running"

