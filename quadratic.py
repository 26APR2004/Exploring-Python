# Solve the quadratic equation a**2+b*x+c=0
# import the math module

import cmath
# Take input
a=int(input("Enter the a:"))
b=int(input("Enter the b:"))
c=int(input("Enter the c:"))

# calculate Descriminate

c=(b**2)-(4*a*c)

# two solution are

s_1=(-b+cmath.sqrt(c)/(2*a))
s_2=(-b-cmath.sqrt(c)/(2*a))

print("The solution is {} and {}".format(s_1,s_2))