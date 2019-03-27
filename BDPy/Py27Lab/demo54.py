file1 = open('data\\python_introduction')

readme_txt = file1.read()
print type(readme_txt), len(readme_txt), readme_txt[:50]

file1.close()

with open('data\\python_introduction') as file2:
    readme_txt2 = file2.read().decode('utf-8')
    print type(readme_txt2), len(readme_txt2), readme_txt2[:50]

file3 = open('data\\clone1', 'w')
file3.write(readme_txt)
file3.close()

with open('data\\clone2', 'w') as file4:
    file4.write(readme_txt2.encode('UTF-8'))