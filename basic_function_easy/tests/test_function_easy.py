"""Test of the function"""
def toto():
    print('FOO')

def test_toto():
    assert toto() == 'foo'
