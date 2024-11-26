import math
import random
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
def test_integer_range():
    for _ in range(100):
        number = random.randint(1,100)

        if number % 2 !=0:
            number *=2
        if number % 3 == 0:
            number //= 3
        if number % 4 == 0:
            number *= 4
        if number > 4:
            with pytest.raises(ValueError):
                integer_range(number)
        else:
            assert integer_range(number) == number
            

