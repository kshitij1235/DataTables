def get_start_and_end(page: int, items_per_page: int):
    """Calculate start and end indices for pagination."""
    start = (page - 1) * items_per_page
    end = start + items_per_page
    return start, end

