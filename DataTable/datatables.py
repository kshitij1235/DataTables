import pandas as pd 
from DataTable.filter import *
from DataTable.sort import *
from DataTable.check import *
from DataTable.calculate import *
from pandas import DataFrame


class df_datatables:
    def __init__(self, 
                dataframe : DataFrame=None, 
                sql=None,
                db_connection= None,
                params: dict={
            'order_by': 0,
            'sort_asc': True,
            'skip': 0,
            'limit_per_page': 10,
            'search': '',
            'column_search':''
            }):
        """
        This class will return class the DataFrame object with default config
        
        arguments 
        ---------
        - dataframe -> dataframe object (if want to send dataframe db object is not needed)
        - sql -> native sql query (if you want to send a query it is necessary to send a db_connection object)
        - db_connection - > db connection object 
        - params -> to modify the output 
            - {
            'filter': "example string / None",
            'order_by' : 1 <- index of column to sort,
            'sort_asc': True ,
            'skip' : int (skip numbers of pages),
            'limit_per_page':int,
            'exclude_column_search':[] (should not search this column)
            }
        
        """
        if dataframe is not None and not dataframe.empty:
            self.dataframe = dataframe


        else: 
            result = db_connection.connect().execute(sql)
            self.dataframe = pd.DataFrame(result.fetchall(), columns=result.keys())

        self.params = params
        
    
    def get_datable(self):
        return Datable(self.dataframe, params=self.params)
    def get_data(self):
        return fetch_data(self.dataframe)
        


def Datable(dataframe:DataFrame , params : dict):
    '''
    This is a complete datatable function 
    
    you just have to pass in  a params dict
    
    structure of param
    ---------------
    - {
    'filter': "example string / None",
    'order_by' : 1 / "str" <- index of column to sort,
    'sort_asc': True ,
    'skip' : int (skip numbers of pages),
    'limit_per_page':int 
    'exclude_column_search':[]
    } 
    
    return 
    ------
    - {
        "total_record": (eg)1000,
        "dataframe" : dataframe_ 
    }
    
    '''
    

    search = params.get("filter") 
    include_column_for_search = params.get("search_column")
    search_in_column = params.get("search_values")
    page_number = params.get("skip")
    items_in_one_page = params.get("limit_per_page")
    order_by_column =  params.get("order_by")
    sort_by = params.get("sort_asc")


    dataframe_ = dataframe

    #filter the search 
    if search:
        dataframe = filter_from_dataframe(dataframe,search)
        dataframe_ = dataframe

    #search for included column search
    if include_column_for_search and search_in_column:
        for val in search_in_column:
            dataframe= filter_from_dataframe(dataframe,
                                               val, 
                                               include_column=include_column_for_search)
            dataframe_ = dataframe

    # paginating 
    if  page_number  and  items_in_one_page  :
        start ,end = get_start_and_end(page_number,
                                       items_in_one_page)
        dataframe_ = dataframe.iloc[start:end]

    #sort by and order by (default) 
    if order_by_column and sort_by:
        dataframe_ = sort_from_dataframe(dataframe_,
                        order_by_column,
                        ascending=sort_by)

    return{
        "total_record":len(dataframe),
        "dataframe" : dataframe_ 
    }

def fetch_data(dataframe:DataFrame):
    '''
    this returns all the data without filter
    return 
    ------
    - {
        "total_record": (eg)1000,
        "dataframe" : dataframe_ 
    }
    
    '''
    
    dataframe_ = dataframe

    
    return{
        "total_record":len(dataframe),
        "dataframe" : dataframe_ 
    }
