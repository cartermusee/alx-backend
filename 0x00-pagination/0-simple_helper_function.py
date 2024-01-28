#!/usr/bin/env python3
"""module for simpler helper function"""
from typing import Tuple


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
