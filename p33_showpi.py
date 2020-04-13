'''
Approximating pi.  CIS 210 W19 Project 3-3
showMontePi

Author: Derek Martin

Credits: Based on code on p.78 Miller and Ranum text.

Approximate pi using a Monte Carlo simulation.
Then add graphics to visualize simulation.
'''

from turtle import *
import math
import random

def showMontePi(numDarts):
    '''
    (int) -> graphics

    Calculate pi and use turtle graphics to display the simulation

    ** random element in algorithms may cause examples to not be replicable
    '''
    # pen should stay up for drawing darts
    drawBoard()
 
    inCircle = 0

    # throw the darts and check whether
    # they landed on the dart board and
    # keep count of those that do
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        if (isInCircle(x, y, 1)):
            inCircle += 1
            color('blue')
        else:
            color('red')

        goto(x, y)
        dot()

    # calculate approximate pi
    approxPi = inCircle/numDarts * 4

    #wn.exitonclick()

    return approxPi

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
    if (distance <= r): # Compare (distance of point from origin) to (radius) to see if point falls within circle
        return True
    else:
        return False

def drawBoard():
    wn = Screen()
    wn.setworldcoordinates(-2, -2, 2, 2)

    speed(0); hideturtle()
    penup()

    goto(-1, 0)
    pendown()
    goto(1, 0)
    penup()
    goto(0, 1)
    pendown()
    goto(0, -1)
    penup()
    goto(0, -1)
    return None

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
    showMontePi(1000)
    reportPi(1000, showMontePi(1000))

main()


