#! /usr/bin/python

# Python program to find the factorial of a number using recursion
import sys

def recur_factorial(n):
   """Function to return the factorial
   of a number using recursion"""
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

def main():
    #print(len(sys.argv))
    if len(sys.argv) == 2:
        num = sys.argv[1]
        num = int(num)
    # check is the number is negative
        if num < 0:
            sys.exit("Negative number passed")
        elif num == 0:
            sys.exit("The factorial of 0 is 1")
        else:
            retnum = recur_factorial(num);
            return retnum    
    else:
        sys.exit("Not enough arguments")


if __name__ == "__main__":
    main()