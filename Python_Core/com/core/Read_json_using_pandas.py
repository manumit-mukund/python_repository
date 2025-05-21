import pandas as pd

df = pd.read_json('file.json')

print(df.to_string())