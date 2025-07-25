import pandas as pd
import os

os.getcwd()
os.chdir(r"../../resources")

df = pd.DataFrame(data=[
    ['1', 'A', '25/4/2025'],
    ['2', 'B', '26/8/2025'],
    ['3', 'C', '18/1/2025']],
    columns=['ID', 'NAME', 'DATE OF JOINING'])

df.to_json('file1.json', orient='split', compression='infer')

df = pd.read_json('file1.json', orient='split', compression='infer')

print(df)