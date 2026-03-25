# pd.merge(df1, df2, on='column_name', how='type_of_join')

import pandas as pd

df_customer = pd.DataFrame ({
    "CustomerID" : [1,2,3],
    "Name" : ['A', 'B', 'C']
})

df_orders = pd.DataFrame({
    "CustomerID" : [1,2,4],
    "OrderAmount" : [250, 450, 350]
})

df_merged = pd.merge(df_customer, df_orders, on='CustomerID', how='inner')
print("Inner Join")
print(df_merged)

print("\nOuter join")
df_merged1 = pd.merge(df_customer, df_orders, on='CustomerID', how='outer')
print(df_merged1)

print("\nRight join")
df_merged2 = pd.merge(df_customer, df_orders, on='CustomerID', how='right')
print(df_merged2)