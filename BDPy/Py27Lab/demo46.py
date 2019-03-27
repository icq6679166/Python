import requests
url1 = "https://bugzilla.mozilla.org/rest/bug/35"
result1 = requests.get(url1)
print result1.status_code, type(result1.content)
print result1.content[:100]
result_obj = result1.json()
print type(result_obj),[l for l in result_obj]
bugs = result_obj["bugs"]
firstBug = bugs[0]
print type(firstBug)
for k, v in firstBug.items():
    print k, v