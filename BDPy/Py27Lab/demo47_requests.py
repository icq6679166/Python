import requests
from bs4 import BeautifulSoup

url1 = 'https://www.uuu.com.tw/'

result1 = requests.get(url1)

print result1.status_code, type(result1.content), len(result1.content)
soup1 = BeautifulSoup(result1.content, "html.parser")
print soup1.title
courses = soup1.find('div', {'id': 'course_list'})
items = courses.find_all('a')
for i in items:
    print i
