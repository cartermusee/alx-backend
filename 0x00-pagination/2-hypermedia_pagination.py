#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """list for those particular pagination
    Keyword arguments:
    page: current page
    page_size: content per page
    Return: tuple of start and end
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
        """simple pagination
        Keyword arguments:
        page: current page
        page_size: content per page
        Return: dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()
        if not data:
            return []
        start, end = index_range(page, page_size)
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """simple pagination
        Keyword arguments:
        page: current page
        page_size: content per page
        Return: dataset
        """
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        page_data = self.get_page(page, page_size)

        def next_page():
            """method for next page"""
            if len(self.get_page(page + 1, page_size)) > 0:
                return page + 1
            else:
                return None

        def prev():
            """method for previous page"""
            if page > 1:
                return page - 1
            else:
                return None
        data_all = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page(),
            'prev_page': prev(),
            'total_pages': total_pages
        }
        return data_all
