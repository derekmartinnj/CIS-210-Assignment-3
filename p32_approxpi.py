'''
Project 3.2 Approximating Pi CIS 210 Winter 2019

Author: Derek MArtin

Credits: N/A

Approximate pi using Monte Carlo algorithm
'''
import math
import random

def montePi(numDarts):
    '''
    (int) -> float

    Call isInCircle() numDarts times, and calculate an approximation of pi based on the results

    >>> montePi(100)
    3.08
    >>> montePi(100000)
    3.143072
    
    ** Due to random element, examples may not be replicable.
    ** Radius value is set to 1
    '''
    inCircle = 0

    for i in range(numDarts):
        if (isInCircle(random.random(), random.random(), 1)):
            inCircle += 1

    pi = inCircle/numDarts * 4 # Multiply by 4 because this section of the circle == (pi / 4)

    return pi

def isInCircle(x, y, r):
    '''
    (number), (number), (number) -> boolean

    Determine whether the 'dart' has landed within the area of the circle.
    
    >>> isInCircle(0, 0, 1)
    True
    >>> isInCircle(.5, .5, 1)
    True
    '''
    distance = math.sqrt(x**2 + y**2)
    if (distance < r): # Compare (distance of point from origin) to (radius) to see if point falls within circle
        return True
    else:
        return False

def reportPi(numDarts, approxPi):
    '''
    (int), (float) -> float

    Display the percentage error between Monte Carlo and math.pi approximations of pi

    >>> reportPi(1000, montePi(1000))
    With 1000 iterations:
    my approximate value for pi is: 3.104
    math lib pi value is: 3.141592653589793
    This is a 1.2 percent error.
    >>> reportPi(100, montePi(100))
    With 100 iterations:
    my approximate value for pi is: 3.48
    math lib pi value for pi is: 3.141592653589793
    This is a 10.77 percent error.

    ** approxPi argument = montePi(numDarts)
    '''
    pi = math.pi
    difference = abs(round((((pi - approxPi) / pi) * 100), 2)) # Calculate percent error between Monte Carlo approx and math.pi
    print("With", numDarts, "iterations:")
    print("my approximate value for pi is:", approxPi)
    print("math lib pi value for pi is:", pi)
    print("This is a", difference, "percent error.")
    return None

def main():
    '''Main function for calling montePi() and reportPi()'''
    montePi(100    reportPi(100, montePi(100))
    montePi(100000)
    reportPi(100000, montePi(100000))
    montePi(10000000)
    reportPi(10000000, montePi(10000000))
    return None

main()
