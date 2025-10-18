import pandas as pd
import os

os.getcwd()
os.chdir(r"../../resources")

df = pd.read_json('file1.json')

print(df.to_string())