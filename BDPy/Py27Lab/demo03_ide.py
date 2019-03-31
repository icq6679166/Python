def getDigit(x):
    """

    :type x: int or float
    """
    returnDigit = 0
    while x > 0:
        x //= 10
        returnDigit += 1
    return returnDigit


print getDigit(1000)
print getDigit(2 ** 10)
print getDigit(2 ** 32)
print getDigit(2 ** 64)
print getDigit(2 ** 512)
print 2 ** 512
