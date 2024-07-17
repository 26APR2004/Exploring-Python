# Conditional ststements

num=4
if num%2==0:
    print("num is Divisible by 2")
else:
    print("it does not divisible by 2")

#onther way
num_1=25
if num_1%2==0:
    print("num is Divisible by 2")
elif num_1%5==0:
    print("it divisible by 5")
else:
    print("number is not divisible by both")

# Nested if 

if num_1%2==0:
    if num_1%5==5:
        print("number is divsible by both 2 and 5")
    else:
        print("number is just divisible by 2, not 5")
else:
    print("it not divisible by both")

# Shortb method to write nested if

if num_1%2==0 and num_1%5==0:
      print("YES it is divisible by both")