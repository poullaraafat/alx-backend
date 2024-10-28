#!/usr/bin/env python3
import csv
import math
from typing import List
"""
0-simple_helper_function.py file
"""


def index_range(page, page_size):
    """function to return the start index and
    the end index of dataset

    Args:
        page (integer): page number
        page_size (integer): page size

    Returns:
        tuple: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get the page from dataset

        Args:
            page (int, optional): Defaults to 1.
            page_size (int, optional):Defaults to 10.

        Returns:
            List[List]:
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(dataset):
            return []

        return dataset[start:end]
