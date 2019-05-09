from add import add_method
'''以下是我的测试用例'''
def test_add():
    assert add_method(1,2) == 2

def test_fushu():
    assert add_method(-1,0) == 3

def test_0():
    assert add_method(0,0) == -1
    #print('hi , i can do it')
