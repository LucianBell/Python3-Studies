#!python

from decimal import Decimal, getcontext

radius = Decimal(3)
pie = Decimal(3.1415)

getcontext().prec = 8
area = pie * (radius ** 2)

print(area)
