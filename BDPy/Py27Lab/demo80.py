import pandas as pd
from pandas_datareader import data, wb

data1 = wb.download(indicator='SE.PRM.TENR', country=['all'], start='2002', end='2018')
print data1.shape
print data1.head()