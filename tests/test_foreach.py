import pytest
from foreach import foreach


def square(x):
    return x**2


def test_sequential_square():
    params = [1, 2, 3, 4, 5]
    result = foreach(square, params, parallel=False)
    expected_result = [1, 4, 9, 16, 25]
    assert result == expected_result


def test_parallel_square():
    params = [1, 2, 3, 4, 5]
    result = foreach(square, params, parallel=True)
    expected_result = [1, 4, 9, 16, 25]
    assert result == expected_result
