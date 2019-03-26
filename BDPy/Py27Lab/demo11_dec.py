from decimal import Decimal as Dec

print 5
print Dec(5)
print 0.2
print Dec(0.2)
print Dec(2.968)
print Dec('2.968')
print Dec(2968)*Dec(0.001)-Dec(2.968)
print Dec(2968)*Dec('0.001')-Dec('2.968')
