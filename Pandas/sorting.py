##Single Value

import pandas as pd

data = {
    "Name" : ['A', 'B', 'C'],
    "Age" : [28, 34, 22],
    "Salary" : [1000, 2000, 3000]
}

df = pd.DataFrame(data)
print(df)


df.sort_values(by='Age', ascending=False, inplace=True)
print(df)

##Multiple Value

df2 = pd.DataFrame(data)

df2.sort_values(by=['Age', 'Salary'], ascending=[True, True], inplace=True)
print(df2)