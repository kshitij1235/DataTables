from pandas import DataFrame

def filter_from_dataframe(df:DataFrame, partial_string:str, exclude_column: list=None):
    '''
    This is function is made to filter out the matching text
    
    parameters
    -------
    
    - df -> dataframe
    - partial_string -> the text that need to be filter
    
    '''

    # Convert dataframe to string and check if search term is present
    mask = df.astype(str).apply(lambda column: column.str.contains(partial_string, case=False, na=False)).any(axis=1)

    # Exclude specified columns from the search
    if exclude_column:
        mask &= ~df[exclude_column].astype(str).apply(lambda column: column.str.contains(partial_string, case=False, na=False)).any(axis=1)

    return df[mask]
