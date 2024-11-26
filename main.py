import math
def calculate_sqaure_root(number):
    """Calculates the sqaure root of a given number

    Args:
        number (float): the number to calculate the sqaure root

    Raises:
        ValueError: If the input is negative

    Returns:
        float: the sqaure root of the input number
    """
    if number < 0:
        raise ValueError("Cannot calculte the sqaure root of a negative number")
    return math.sqrt(number)

def test_calculate_sqaure_root():
    assert calculate_sqaure_root(9) == 3