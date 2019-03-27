import demo33

print "inside demo34"
demo33.foo(5, 6)
demo33.bar(7, 8)

import demo33 as d3

d3.foo(9, 10)
d3.bar(11, 12)

from demo33 import foo, bar

foo(13, 14)
bar(15, 16)

from demo33 import foo as f, bar as b

f(17, 18)
b(19, 20)

import demo_pkg.demo35 as d35

d35.foo(1, 2)
d35.bar(3, 4)

from demo_pkg.demo35 import foo as fo, bar as bo

fo(5, 6)
bo(7, 8)
