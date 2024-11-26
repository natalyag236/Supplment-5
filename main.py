import math
def calculate_sqaure_root(number):
    if number < 0:
        raise ValueError("Cannot calculte the sqaure root of a negative number")
    return math.sqrt(number)

def test_calculate_sqaure_root():
    assert calculate_sqaure_root(9) == 3