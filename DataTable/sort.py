from pandas import DataFrame

def sort_from_dataframe(df:DataFrame,column,ascending =True):
    '''
    This function sorts the column in the dataframe 
    
    parameter 
    ---------
    
    - df -> dataframe
    - column -> the index or name of column to sort
    - asscending (default : True) -> to sort it in assending order
    
    '''

    if isinstance(ascending,str):
        if ascending == "ASC":
            ascending = True
        else:
            ascending = False
    if isinstance(column , str):
        column = list(df.columns).index(column)
    
    df_sorted = df.sort_values(by=df.columns[column],ascending=ascending)
    df_sorted.reset_index(drop=True, inplace=True)
    return df_sorted
