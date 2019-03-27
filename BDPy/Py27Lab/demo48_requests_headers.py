import requests
from bs4 import BeautifulSoup

# https://www.mobile01.com/category.php?id=4
# https://www.mobile01.com/category.php?id=5
# https://www.mobile01.com/category.php?id=2
# https://www.mobile01.com/category.php?id=6


url1 = 'https://www.mobile01.com/'
headers = {'User-Agent': 'BDPY',
           'From': 'trump@usa.com'}

result1 = requests.get(url1, headers=headers)

print result1.status_code, type(result1.content), len(result1.content)
soup1 = BeautifulSoup(result1.content, "html.parser")
print soup1.title

hot_posts = soup1.find('div', {'id': 'hot-posts'})
items = hot_posts.find_all('a')
for item in items:
    print item

base_url = 'https://www.mobile01.com/category.php?id=%d'
ids = [2, 4, 5, 6]

for id in ids:
    print '\n\n'
    url = base_url % (id)
    result1 = requests.get(url, headers=headers)

    print result1.status_code, type(result1.content), len(result1.content)
    soup1 = BeautifulSoup(result1.content, "html.parser")
    print '**' + str(soup1.title)


    hot_posts = soup1.find('div', {'id': 'hot-posts'})
    items = hot_posts.find_all('a')
    for item in items:
        print item
