import pandas as pd
import os

os.getcwd()
os.chdir(r"../../resources")

df = pd.read_csv('output.csv')

print(df)