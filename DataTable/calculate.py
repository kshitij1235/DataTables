def cal_skip(skip):
    """calculate skip ( formula = skip+10/10)"""
    return (skip+10)/10 if skip != 0 else 1

def cal_offset(skip,limit_per_page):
    """calculate offset (formula = (skip - 1) * limit_per_page)"""
    skip=cal_skip(skip)
    return (skip - 1) * limit_per_page