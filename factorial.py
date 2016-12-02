#! /usr/bin/python

# Python program to find the factorial of a number using recursion
import sys

# def recur_factorial(n):
#    """Function to return the factorial
#    of a number using recursion"""
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# def factorial(n):
#     num = 1
#     while n >= 1:
#         num = num * n
#         n = n - 1
#     return num

def main():
    #print(len(sys.argv))
    if len(sys.argv) == 2:
        num = sys.argv[1]
        num = int(num)
    # check is the number is negative
        if num < 0:
            sys.stdout.write("Negative number passed")
        elif num == 0:
            sys.stdout.write(str(1))
        else:
            result_num = 1
            while num >= 1:
                result_num = result_num * num
                num = num - 1
            # for i in range(num):
            #     result_num *= i + 1 
            #retnum = recur_factorial(num)
            sys.stdout.write(str(result_num))
            
            
    else:
        sys.exit("Not enough arguments")


if __name__ == "__main__":
    main()