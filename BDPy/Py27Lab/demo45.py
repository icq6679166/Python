# encoding=UTF-8
import json

dict1 = {'name': 'BDPY', 'duration': '35hr', 'lcation': '台北'}
print type(dict1), dict1
json_string1 = json.dumps(dict1)
print type(json_string1), json_string1

list1 = ['welcome', '歡迎', u'光臨', 100, 3.14, None, True, False, dict1]
print type(list1), list1
json_string2 = json.dumps(list1)
print type(json_string2), json_string2

obj1 = json.loads(json_string1)
print type(obj1)
for k, v in obj1.items():
    print k, v

obj2 = json.loads(json_string2)
print type(obj2)
for i in obj2:
    if isinstance(i, dict):
        for k, v in i.items():
            print k, v
    else:
        print i
