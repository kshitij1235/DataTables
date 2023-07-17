from pandas import DataFrame
def apply_pagination(df:DataFrame, skip:int, limit:int):
    """
    Apply pagination to a DataFrame using skip and limit.
    
    Args
    ------
        - df (pandas.DataFrame): The DataFrame to apply pagination to.
        - skip (int): The number of rows to skip.
        - limit (int): The maximum number of rows to include.
    
    Returns
    -------
        - pandas.DataFrame: The paginated DataFrame.
    """
    return df.iloc[skip:skip+limit]