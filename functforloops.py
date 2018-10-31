#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
assignment: Python 2.7 Katas - Functions and For Loops

Description: Katas practicing Functions and For Loops

Author: Aaron Jackson
GitHub: TimeApollo
"""
__author__ = 'TimeApollo'

# how to do with args and get added functionality
# def add( *args):
#     return sum(args)

def add( num1 , num2 ):
    """returns the sum of 2 values"""
    return num1 + num2

def multiply( num1 , num2 ):
    """returns the product of 2 whole numbers"""
    """dont know how to do absolute without multiply or abs funct"""
    """know i dont need all this, just wanted to handle negatives"""
    if num1 == 0 or num2 == 0:
        return 0
    num1_sign = 1 if num1 > 0 else 0
    num2_sign = 1 if num2 > 0 else 0

    total = 0
    if num1_sign == num2_sign:
        for _ in range(abs(num1)):
            total = add( total , abs(num2) )
        return total
    elif num1_sign:
        for _ in range(num1):
            total = add( total , num2 )
        return total
    else:
        for _ in range(num2):
            total = add( total , num1 )
        return total

def power( num , nth ):
    """returns num to the nth power (whole power)"""
    if nth == 0:
        return 1
    total = 1
    for _ in range(abs(nth)):
        total = multiply(total , num)

    return total if nth > 0 else 1.0/total

def factorial( num ):
    """returns factorial of value"""
    total = 1
    for i in range(1 , add(num , 1)):
        total = multiply( total , i )
    return total

def fibonacci( nth ):
    """returns the nth number in fibonacci sequence"""
    first , second = 0 , 1
    for _ in range( nth - 1):
        first , second = second , add( first , second )
    return first 

def main():
    tests()

def tests():
    print( "Testing Add function")
    print( 'Values: 2 , 4  Expected: 6 Result: {}'.format(add(2,4)))
    print( 'Values: 2 , -3  Expected: -1 Result: {}'.format(add(2,-3)))
    print( 'Values: 202 , 13  Expected: 215 Result: {}'.format(add(202,13)))

    print( "\nTesting Multiply Function")
    print( 'Values: 6 , 8  Expected: 48 Result: {}'.format(multiply(6,8)))
    print( 'Values: 2 , -3  Expected: -6 Result: {}'.format(multiply(2,-3)))
    print( 'Values: -2 , 3  Expected: -6 Result: {}'.format(multiply(-2,3)))
    print( 'Values: -2 , -3  Expected: 6 Result: {}'.format(multiply(-2,-3)))
    print( 'Values: 11 , 9  Expected: 99 Result: {}'.format(multiply(11,9)))
    print( 'Values: 1 , 0  Expected: 0 Result: {}'.format(multiply(1,0)))

    print( "\nTesting Power Function")
    print( 'Values: 2 , 8  Expected: 256 Result: {}'.format(power(2,8)))
    print( 'Values: -2 , 3  Expected: -8 Result: {}'.format(power(-2,3)))
    print( 'Values: 2 , -3  Expected: 0.125 Result: {}'.format(power(2,-3)))
    print( 'Values: -2 , -3  Expected: -0.125 Result: {}'.format(power(-2,-3)))
    print( 'Values: -2 , 0  Expected: 1 Result: {}'.format(power(-2,0)))

    print( "\nTesting Factorial Function")
    print( 'Values: 4  Expected: 24 Result: {}'.format(factorial(4)))
    print( 'Values: 6  Expected: 720 Result: {}'.format(factorial(6)))
    print( 'Values: 8 Expected: 40320 Result: {}'.format(factorial(8)))
    print( 'Values: 1 Expected: 1 Result: {}'.format(factorial(1)))

    print( "\nTesting Fibonacci Function")
    print( 'Values: 8  Expected: 13 Result: {}'.format(fibonacci(8)))
    print( 'Values: 4  Expected: 2 Result: {}'.format(fibonacci(4)))
    print( 'Values: 10 Expected: 34 Result: {}'.format(fibonacci(10)))
    print( 'Values: 2 Expected: 1 Result: {}'.format(fibonacci(2)))
    print( 'Values: 1 Expected: 0 Result: {}'.format(fibonacci(1)))

if __name__ == "__main__":
    main()

