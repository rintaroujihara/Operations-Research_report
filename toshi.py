from math import *
import pandas as pd
import numpy as np
import numpy.linalg as LA
df = pd.read_excel('toshi.xlsx',header = 0)
df2 = df.fillna(0)
print(df2)
lines = []
for i in range(1,79):
    line = []
    for j in range(0,78):
        line.append(df2.iloc[i, j])
    lines.append(line)
print(lines)
w,v = np.linalg.eig(lines)
print(v[:, np.argmax(w)])