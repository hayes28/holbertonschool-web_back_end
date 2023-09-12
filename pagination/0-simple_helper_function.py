#!/usr/bin/env python3
"""Write a function named index_range that takes
two integer arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters"""
    return ((page - 1) * page_size, page * page_size)

"""I went with the more concise was of returning the
tuple, but this is the long version"""
"""start_index = (page - 1) * page_size
end_index = page * page_size
return (start_index, end_index)
"""
