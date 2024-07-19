#!python
from math import pi

def circle(radius):
    area = pi * (radius ** 2)
    return area

if __name__ == '__main__':
    """
    Here I can have the main module, where the code is executed.
    And then import the functions from module 'Challange_3' to
    another python module.
    """
    my_input = float(input("Define the circle radius: "))

    area = circle(radius=my_input)
    print(f'Area: {area}')
