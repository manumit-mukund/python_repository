import pandas as pd
import os

os.getcwd()
os.chdir(r"../../resources")

print("your current working directory= ",os.getcwd())


data = {'Name': ['A', 'B', 'C'],
        'Age': [25, 30, 28],
        'City': ['Delhi', 'Patna', 'Mumbai']}

df = pd.DataFrame(data)

df.to_csv('output_1.csv',  index=False)
df.to_csv('output_2.csv',  index=True)

print("CSV file 'output.csv' created successfully.")