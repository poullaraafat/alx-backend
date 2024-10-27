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
    return  (start_index, end_index)
