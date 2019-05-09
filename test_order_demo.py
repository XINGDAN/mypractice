import time
import pytest
import pytest_ordering

value = 0

@pytest.mark.run(order=2)
def test_add2():
    print("i am 2")
    time.sleep(2)

    assert value == 10

@pytest.mark.run(order=1)
def test_add():
    print("i am one")
    global value
    value = 10
    assert value == 10
