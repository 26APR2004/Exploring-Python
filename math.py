#import the math 

import math

def area_triangle(a,b,c):  # define function
    s=a+b+c/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

# Take input 
a=float(input("Enter the side 1:"))
b=float(input("Enter the side 2:"))
c=float(input("Enter the side 3:"))

area=area_triangle(a,b,c)  # Function call

# output
print("Area of triangle of sides {},{},{}is:".format(a,b,c),area)
