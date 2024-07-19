#!python
from math import pi
import sys # sys module to get args. via terminal

def circle(radius):
    area = pi * (radius ** 2)
    return area

if __name__ == '__main__':
    print(sys.argv) # Showing the list of arguments passed in terminal (it builds an array for it)
    """
    Here I can have the main module, where the code is executed.
    And then import the functions from module 'Challange_3' to
    another python module.
    """
    area = circle(radius=float(sys.argv[1]))
    print(f'Area: {area}')
