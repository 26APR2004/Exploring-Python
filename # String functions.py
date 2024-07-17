# String functions

name="sujal"
gender="MALE"

# The function capitalize() convert first word of the name into calpital
r=name.capitalize()
print(r)

#The function upper() convert overall name into calpital form
g_1=name.upper()
print(g_1)

#The function lower() convert overall name into small form
g_2=gender.lower()
print(g_2)

# To check the data is in capital or in small leter
print(name.isupper())
print(gender.isupper())
print(name.islower())
print(gender.islower())

# to check the data is the combination of numbers+characters or not
prn="22UAI072"
print(prn.isalnum())
print(name.isalnum())

# Does the string contain only alpa bet words/contain only smalll words
age="20    "
print(prn.isalpha())
print(name.isalpha())
print(prn.isdigit())
print(age.isdigit())


# This will find the index number for that you recommanded
print(name.find("s"))
print(name.find("l"))

# How to remove the blanck space
print(age.strip())
