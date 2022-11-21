"""Utilities"""


class InvalidInputException(Exception):
    """Raised when the input cannot be processed to any meaningful output

    Exceptie ridicata atunci cand nu putem procesa datele de intrare intr-un
        output folosibil
    """


def sum_args(values, max_value=100):
    """
    Return the sum of the arguments that are below the max_value

    The default max_value is 100
    The function should ignore values that are not float/int

    Consider adding a minimum value parameter
    """
    accepted_types = (val for val in values
                      if (isinstance(val, int) or isinstance(val, float)))
    accepted_values = [val for val in accepted_types
                       if val <= max_value]
    if len(accepted_values) == 0:
        raise InvalidInputException(
            "There are no valid values in the input, result would be a default 0!")
    # for value in values:
    #     if isinstance(value, int) or isinstance(value, float):
    #         if max_value >= value:
    #             val_sum += value
    return sum(accepted_values)
