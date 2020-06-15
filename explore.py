import numpy as np
import pandas as pd

csv = pd.read_csv("./smol.csv", ";")
print("CSV file has " + str(len(csv.index)) + " rows")
print(csv.head())
csv.to_csv("test.csv", index=False, header=True)