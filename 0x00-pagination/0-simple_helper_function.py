#!/usr/bin/env python

"""Module for index_range function."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Take two integers and return a tuple of size two.
    Tuple contains a start index and end index corresponding
    to the range of indexes to return in a list.
    """
    end_index = page_size * page
    start_index = end_index - page_size
    return start_index, end_index
