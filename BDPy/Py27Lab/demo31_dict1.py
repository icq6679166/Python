salesRecord = {'iphone XR': 200, 'iphone XS': 300, 'ipad pro': 100, 'apple watch4': 150}
print salesRecord['ipad pro'], salesRecord['apple watch4']
print salesRecord.get('HTC'), salesRecord.get('apple watch4')
salesRecord['appleTV'] = 100
for record in salesRecord:
    print record, salesRecord[record]
for key in salesRecord.keys():
    print 'key=', key, ' ,record=', salesRecord[key]
print 'appleTV' in salesRecord, 'htc' in salesRecord, 100 in salesRecord
total = 0
for items in salesRecord.values():
    total += items
print "total sales=", total
for item in salesRecord.items():
    print item[0], item[1]
salesRecord.update({'ipod touch': 30, 'iphone XS': 150})
for k, v in salesRecord.items():
    print 'xxxx=>',k, v
del salesRecord['apple watch4']
for k, v in salesRecord.items():
    print 'OOOO=>',k, v