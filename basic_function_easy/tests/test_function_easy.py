"""Test of the function"""
def inc(x):
 
""" Inc is a function with an X parametr"""
    return x + 1

def test_answer():

"""Test_answer will test if the function inc"""
    assert inc(3) == 5
