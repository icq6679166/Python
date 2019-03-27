sales = ['s', 's', 's', 'm', 's', 'xl', 'l', 'xl', 'xl', 'm', 'm', 'm']

report = {}
print type(report)

for sale in sales:
    report.setdefault(sale, 0)
    report[sale] += 1

print report
