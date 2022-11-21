import pytest

from testingtdd.utils import sum_args, InvalidInputException


def test_sum_of_elements():
    elements = [2, 4, 5, 3, 9, 1, 0, -2]

    expected = 22
    assert sum_args(elements) == expected


def test_sum_with_max_value():
    elements = [2, 4, 5, 3, 9, 1, 0, -2]
    max_value = 5
    expected = 13
    assert sum_args(elements, max_value) == expected


def test_sum_with_non_numerals():
    elements = [2, 4, 5, 3, 9, 's', 0, -2]

    expected = 21
    assert sum_args(elements) == expected


def test_sum_invalid_values():
    elements = ['2, 4, 5, 3, 9', 's', {}, (1, 2, 3)]

    with pytest.raises(InvalidInputException):
        assert sum_args(elements)
