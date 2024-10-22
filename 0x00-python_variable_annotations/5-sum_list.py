#!/usr/bin/env python3
"""Write a type-annotated function sum_list
takes a list input_list of floats as argument
"""


def sum_list(input_list: list[float]) -> list[float]:
    """returns their sum as a float."""
    return (sum(input_list))
