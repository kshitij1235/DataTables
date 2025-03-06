def has_limit_offset(sql_query : str):
    '''
    check if the sql quer has limit and offet
    '''
    sql_query = sql_query.lower()
    
    has_limit = 'limit' in sql_query
    has_offset = 'offset' in sql_query
    
    return has_limit and has_offset 
