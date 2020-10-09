import pandas as pd
import numpy as np

csvName = input('please input the file name:')

metric = pd.read_csv(csvName,sep=';',na_values=['null'])
grouped = metric.groupby(['Series'])
tp50 = grouped['Value'].quantile(0.5)
tp90 = grouped['Value'].quantile(0.9)
#fname = '1.xlsx'
fname = metric.iat[0,1]+'-'+metric.iat[-1,1]+'.xlsx'
#fname = datetime.now().strftime('%Y%m%d-%H-%M')+'-Output.xlsx'
writer = pd.ExcelWriter(fname)

tp50.to_excel(writer,sheet_name='tp50')
tp90.to_excel(writer,sheet_name='tp90')
writer.save()

print('file output to ' + fname)
#print (fname)
