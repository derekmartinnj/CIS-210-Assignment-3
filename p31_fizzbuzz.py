'''
Project 3.1 Fizzbuzz CIS 210 Winter 2019

Author: Derek Martin

Credits: N/A

Code a function that implements the fizzbuzz game using math, conditional stataements, and loops.
'''

def fb(n):
    '''
    (int) -> (int) or (string)

    Display values based on the divisibility of each number from 1 to input n.

    >>> fb(3)
    1
    2
    fizz

    >>> fb(4)
    1
    2
    fizz
    4
    '''
    for i in range (n + 1):
        divThree = i % 3 # use modolo operator to get the remainder
        divFive = i % 5
        if (i > 0): # skip zero
            if ((divThree == 0) and (divFive == 0)): # Check if the remainder is 0 (evenly divisable)
                print ("fizzbuzz")
            elif (divThree == 0):
                print("fizz")
            elif (divFive == 0):
                print("buzz")
            else:
                print(i)
    print("Game over!")
    return None
