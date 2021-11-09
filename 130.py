import pandas as pd
import csv
df = pd.read_csv("brown_stars.csv")
print(df.shape)

del df["a"]
del df["b"]

print(df.shape)

headers = []

with open('clean.csv','w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerows(headers)
    csvWriter.writerow(df)
      
