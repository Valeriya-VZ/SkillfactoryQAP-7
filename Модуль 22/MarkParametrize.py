#  напишите функцию, которая определяет, можно ли составить треугольник из
# трёх отрезков, длины которых передаются в функцию.

import pytest


def is_triangle(x, y, z):
    if x > 0 and y > 0 and z > 0 and (x < (y + z) and x > (y - z) and y < (x + z) and
                                      y > (x - z) and z < (x + y) and z > (x - y)):
        return True
    else:
        return False


@pytest.mark.parametrize("x", [3, 1, 0, (-1)], ids=["positive", "not_triangle", "zero", "negative"])
@pytest.mark.parametrize("y", [4])
@pytest.mark.parametrize("z", [5])
def test_is_triangle(x, y, z):
    result = is_triangle(x, y, z)
    print(result)
    assert result == True

# В результате: 4 теста, из которых один позитивный и три негативных.
