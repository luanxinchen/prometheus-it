import pandas as pd
import numpy as np
data = pd.read_csv('metrics.csv',sep=';')
grouped = data.groupby(['Series'])
a = grouped['Value'].quantile(0.5)
b = grouped['Value'].quantile(0.9)
a.to_csv('tp50.csv',sep= ',')
b.to_csv('tp90.csv',sep= ',')
