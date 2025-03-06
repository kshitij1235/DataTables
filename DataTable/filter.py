from pandas import DataFrame
import pandas as pd 
def filter_from_dataframe(df: DataFrame,
                          partial_string: str,
                          exclude_column: list = None,
                          include_column: list = None):
    '''
    This function is made to filter out the matching text
    
    parameters
    -------
    - df -> dataframe
    - partial_string -> the text that needs to be filtered. If it contains commas, each element is searched separately.
    - exclude_column -> list of columns to exclude from search (optional)
    - include_column -> list of columns to include in search (optional)
    '''

    # Split the partial_string into multiple substrings if it contains commas
    search_terms = [term.strip() for term in partial_string.split(",")]
    
    # Convert search terms to regex pattern with word boundaries for exact matching
    pattern = '|'.join(search_terms)
    
    # Determine which columns to search
    if include_column:
        # Ensure include_column is a list
        if isinstance(include_column, str):
            include_column = [include_column]
        columns_to_search = include_column
    else:
        # Use all columns except excluded ones
        columns_to_search = df.columns.tolist()
        if exclude_column:
            if isinstance(exclude_column, str):
                exclude_column = [exclude_column]
            columns_to_search = [col for col in columns_to_search if col not in exclude_column]
    
    # Initialize mask as all False
    mask = pd.Series(False, index=df.index)
    
    # Apply search to each column and combine with OR
    for col in columns_to_search:
        if col in df.columns:
            col_mask = df[col].astype(str).str.contains(pattern, case=False, na=False)
            mask = mask | col_mask
    
    return df[mask]