
# from main import add

def test_demo():
    def add(a, b):
        # This would be imported from your app
        return a + b
    assert add(1, 1) == 2

def test_this_will_fail():
    assert 0 == 1
