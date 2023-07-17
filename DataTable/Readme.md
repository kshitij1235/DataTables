# Introduction 

This is a dataframes library use to perform various operations on them. 

# uses
- make datatables 
- performing sorting 
- perform filter
- perform pagination

# code 

```
import  pandas  as  pd

query  ="select * from username"

a = df_datatables(sql=query,db_connection=db_connection,params={ 
    'filter': filter_text,
    'order_by' : order_by,
    'sort_asc': assign_order(sort),
    'skip' : skip,
    'limit_per_page':limit_per_page 
    })
df = a.get_datatable()

return  df.to_dict()
```