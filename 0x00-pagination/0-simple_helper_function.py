#!/usr/bin/env python3
"""module for simpler helper function"""


def index_range(page, page_size):
    """list for those particular pagination
    Keyword arguments:
    page: current page
    page_size: content per page
    Return: tuple of start and end
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
