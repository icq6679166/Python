from datetime import datetime
now = datetime.now()

print now
print repr(now)
print [now]
print (now,)
print {now}
print {'k':now}
print (now) # not tuple
print [str(now)]