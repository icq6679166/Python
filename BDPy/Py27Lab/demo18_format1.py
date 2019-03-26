import numpy

r = 4
a = r * r * numpy.pi
print '[1]radius=%f, area=%f' % (r, a)
print '[2]radius=%.3f, area=%.3f' % (r, a)
print '[3]radius=%(radius).3f, area=%(area).3f' % {'radius': r, 'area': a}
print '[4]radius=%(radius).3f, area=%(area).3f' % {'area': a, 'radius': r}
print '[5]radius={}, area={}'.format(r, a)
print '[6]radius={:.3f}, area={:.3f}'.format(r, a)
print '[7]radius={1:.3f}, area={0:.3f}'.format(a, r)
print '[8]sradius={radius:.3f}, area={area:.3f}'.format(radius=r, area=a)
