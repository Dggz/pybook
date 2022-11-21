from testingtdd.utils import sum_args


def test_sum_of_elements_below_max_val():
    max_value = 10
    elements = [2, 4, 5, 3, 9, 1, 0, -2]

    expected = 22

    assert sum_args(max_value, *elements) == expected
