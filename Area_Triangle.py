# # Area of Triangle

# a=int(input("Enter the height:"))
# b=int(input("Enter the breadth:"))

# Area=0.5*a*b
# print("Area of Triangle mis:",Area)


#import the math module

import cmath

def area_triangle(a,b,c):  # define function
    s=a+b+c/2
    return cmath.sqrt(s*(s-a)*(s-b)*(s-c))

# Take input 
a=float(input("Enter the side 1:"))
b=float(input("Enter the side 2:"))
c=float(input("Enter the side 3:"))

area=area_triangle(a,b,c)  # Function call

# output
print("Area of triangle of sides {},{},{}is:".format(a,b,c),area)
