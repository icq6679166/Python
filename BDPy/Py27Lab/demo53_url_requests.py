#encoding=UTF-8
import requests

# base_url = 'YOUR_BASE_URL/%s.json'
base_url = 'https://demo53.firebaseio.com/%s.json'
url1 = base_url % 'data1_string'
r1 = requests.put(url1, json='hello BDPY')
print r1.status_code, r1.content

url2 = base_url %'data2_chinese'
r2 = requests.put(url2, json='中文')
print r2.status_code, r2.content

url3 = base_url %'data3_unicode'
r3 = requests.put(url3, json=u'萬國碼也可以')
print r3.status_code, r3.content
