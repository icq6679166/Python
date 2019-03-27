import math
import random

print math.pi
print math.log(2, 2), math.log(2, 10)

for i in range(20):
    print random.randint(1, 100),

l1 = ['Disney', "Marvel", 'DC', "Universal Studio", "Sony"]
for i in range(10):
    print random.choice(l1)

cards = ['A', 'K', 'Q', 'J', '10', '9']
for i in range(10):
    random.shuffle(cards)
    print cards
