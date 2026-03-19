import pandas as pd

data = {
    "Name":['shamim', 'Karim', 'sharif', 'patwary', 'tafin', 'sadid'],
    "Age":[22, 26, 50,None, 13, 11],
    "Salary" :[5000, 10000, None, 20000, 3000, 2000],
    "Performance_Score":[90, 95, 88, 80, None, 75]
}

df = pd.DataFrame(data)
print("Before interpolation")
print(df)

###There is various method. Default is linear

print("After interpolation")
df['Age'] = df['Age'].interpolate(method='linear')
print(df)

