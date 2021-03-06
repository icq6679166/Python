from decimal import Decimal as Dec, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN

a1 = 2.5
a2 = 3.5
a3 = 4.5
a4 = 5.5
l1 = [a1, a2, a3, a4]
for l in l1:
    d1 = Dec(l)
    output1 = Dec(d1.quantize(Dec('1'), rounding=ROUND_HALF_UP))
    print('round_half_up', d1, output1)

    output2 = Dec(d1.quantize(Dec('1'), rounding=ROUND_HALF_DOWN))
    print('round_half_down', d1, output2)

    output3 = Dec(d1.quantize(Dec('1'), rounding=ROUND_HALF_EVEN))
    print('round_half_even', d1, output3)
