str1 = "ABCDE"
int1 = 100
list1 = ['A', 'B', 'C', 'D', 'E']
print type(str1), len(str1), str1[1]
print type(list1), len(list1), list1[1]
list1[1] = 'b'
print list1
# str1[1]='b'
print hex(id(str1)), hex(id(int1))
int1 = 200
str1 = "AbCDE"
print hex(id(str1)), hex(id(int1))
