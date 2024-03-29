#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple

"""Module for Server class."""


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Iniatialize dataset attribute to None."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Create the Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page from a dataset according to the pagination paras."""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        data = self.dataset()
        indices = index_range(page, page_size)
        return data[indices[0]:indices[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Take two integers and return a tuple of size two.
    Tuple contains a start index and end index corresponding
    to the range of indexes to return in a list.
    """
    end_index = page_size * page
    start_index = end_index - page_size
    return start_index, end_index
