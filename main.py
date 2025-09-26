import math
from math import *

x = float(input("x = ")) * 10

while x in range(-50, 51):
    if x <= 0:
        y = sin(x + cos(x)) / cos(x + sin(x))
        print(y / 10, x / 10)
        x += 5
    elif (x > 0) and (x <= 10):
        y = (x * log(2 * x, math.e)) + (math.e ** 2 * x)
        print(y / 10, x / 10)
        x += 5
    elif x > 10:
        y = 3 * sin(x ** 3) + (3 ** x * cos(3 * x))
        print(y / 10, x / 10)
        x += 5
