import pandas as pd 
from DataTable.filter import filter_from_dataframe
from DataTable.pagination import apply_pagination
from DataTable.sort import sort_from_dataframe
from DataTable.check import *
from DataTable.calculate import *
from pandas import DataFrame

class df_datatables:
    def __init__(self, dataframe : DataFrame=None, sql=None,db_connection= None,params: dict={
            'order_by': 0,
            'sort_asc': True,
            'skip': 0,
            'limit_per_page': 10
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
    
    dataframe_ = dataframe

    if  params.get("skip") is not None  and  params.get("limit_per_page") is not None:
        dataframe_ = apply_pagination(dataframe_,
                                    skip=params["skip"],
                                    limit=params["limit_per_page"])
    if params.get("filter"):

        dataframe_ = filter_from_dataframe(dataframe,
                                            params['filter'],
                                            exclude_column=params.get("exclude_column"))
        dataframe = dataframe_
        
            
    if params.get("order_by")  and params.get("sort_asc"):
        dataframe_ = sort_from_dataframe(dataframe_,
                        params["order_by"],
                        ascending=params["sort_asc"])
    
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
