# encoding=UTF-8
import os
import sys

print os.getcwd()
path1 = u'某某資料'
os.mkdir(path1)
os.chdir(path1)
print os.getcwd().decode('ms950')
os.chdir('..')
os.rmdir(path1)

for i in sys.argv:
    print i
print sys.executable