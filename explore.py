import numpy as np
import pandas as pd

csv = pd.read_csv("./smol.csv", ";")
print("CSV file has " + str(len(csv.index)) + " rows")