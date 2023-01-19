from fibonacci import fib

def test_fibonacci():

    for i,f in enumerate([0, 1, 1, 2, 3, 5, 8]):
        assert fib(i) == f
