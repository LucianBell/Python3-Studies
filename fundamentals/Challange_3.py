#!python
from math import pi

if __name__ == '__main__':
    """
    Here I can have the main module, where the code is executed.
    And then import the functions from module 'Challange_3' to
    another python module.
    """
    radius = float(input("Define the circle radius: "))

    area = pi * (radius ** 2)

    print(area)
