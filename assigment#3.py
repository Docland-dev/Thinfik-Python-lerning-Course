"""Homework Assignment #3: "If" Statements


Details:
 
Create a function that accepts 3 parameters and checks for equality between any two of them.

Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.


Extra Credit:

Modify your function so that strings can be compared to integers if they are equivalent. For example, 
if the following values are passed to your function:

6,5,"5"

You should modify it so that it returns true instead of false.

Hint: there's a built in Python function called "int" that will help you convert strings to Integers."""

a = 50
b = 100
c = 80

if a < b and c == a:
    print(True)
elif a == b:
        print("a and b are equal")
else:
    print(False)

d = int("100")

if a < c and b == d:
    print("a is less than c and b is equal to d")