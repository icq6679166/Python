import pandas

from matplotlib import pyplot, rc

data1 = pandas.read_csv('data\\data1.csv', skiprows=4, index_col="Country Name")
#data1.to_excel('data\\output.xlsx', sheet_name='python_generated_population')
print data1.shape
print data1.head()
print data1.columns
print data1['1960'].mean()
data1['join'] = data1['1960']+data1['1961']
print data1.columns

