from add import add_method
import pytest_rerunfailures
import pytest_sugar,pytest_assume
import random
import  time

def test_rerun_add():
    time.sleep(2)
    assert add_method(2,3) == random.randint(2,7)














