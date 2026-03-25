import pandas as pd

## Single grouping

data = {
    "Name" : ['A', 'B', 'C', 'D', 'E'],
    "Age" : [28, 34, 22, 34, 28],
    "Salary" : [50000, 60000, 45000, 52000, 480000]
}

df = pd.DataFrame(data)

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)


## Multigrouping 

grouped1 = df.groupby(['Age', 'Name'])['Salary'].sum()
print(grouped1)