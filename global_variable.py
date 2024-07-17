
#  Outside Global Variable Use 

x=20   # Global Variable

def age():    # Function Defination
    x=19      # Local Variable
    print("Your age is:",x) # THIS WILL PRINT LOCAL VARIABLE

age() # Function Call
print("Your age is:",x) # THIS PRINT GLOBAL VARIABLE

# Inside Global Variable Use 
def name():
    global y # Global Varible
    y="sujal"
    print("name is:"+y)

name()
print("name",y)