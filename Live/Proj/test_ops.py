
from ops import add

def test_add():
    assert add(1, 1) == 2

def test_hello(tmpdir): # corresponds roughly to "setup" and "teardown"
    print("your tmpdir: ", tmpdir)