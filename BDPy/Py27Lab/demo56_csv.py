import csv

#f1 = open('data\\excel1.csv')
f1 = open('data\\excel2.csv')

reader1 = csv.reader(f1)
outputData = list(reader1)

f1.close()

print type(outputData)

for i in range(0, len(outputData)):
    print type(i), outputData[i]
    for j in range(0, len(outputData[i])):
        print j, outputData[i][j]
        print
