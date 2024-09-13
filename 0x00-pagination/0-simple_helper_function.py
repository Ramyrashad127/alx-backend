#!/usr/bin/env python3


"""typing for annotation"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return start index and end index for page"""
    start_in = (page - 1) * page_size
    end_in = (page - 1) * page_size - 1
    return start_in, end_in
