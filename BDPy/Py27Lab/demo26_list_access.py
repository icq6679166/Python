day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

lengths = []
for day in day_of_week:
    lengths.append(len(day))

print lengths

# type2
print [len(day) for day in day_of_week]
print["**" + day + "**" for day in day_of_week if len(day) > 6]
sun, mon, tue, wed, thr, fri, sat = day_of_week
print sun, tue, fri
print mon, wed, sat

import random

random.seed(0326)
num_list = []
for i in range(20):
    num_list.append(random.randint(1, 50))
print num_list
sorted1 = sorted(num for num in num_list if num > 20)
print sorted1

sorted2 = sorted((num for num in num_list if num < 20), reverse=True)
print sorted2
