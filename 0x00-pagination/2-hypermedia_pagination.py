#!/usr/bin/env python3


"""import modules"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return start index and end index for page"""
    start_in = (page - 1) * page_size
    end_in = page * page_size
    return start_in, end_in


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
        """retrive data"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        self.dataset()
        data = self.__dataset
        if len(data) < start:
            return []
        return data[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """hypermedia paginations"""
        data = self.get_page(page, page_size)
        st, en = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        meta_data = {
                    'page_siae': page_size,
                    'page': page,
                    'data': data,
                    'next_page': page + 1 if en < len(self.__dataset)
                    else None,
                    'prev_page': page - 1 if st > 1 else None,
                    'total_pages': total_pages
                }
        return meta_data
