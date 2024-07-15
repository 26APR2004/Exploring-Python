# Dictionary in Python

student={"Name":"Sujal","PRN":"22UAI072","Age":20}

# get Function
print(student.get("Name"))
print(student.get("Age"))

# Key Function
print(student.keys())

# pop Function
print(student.pop("Age"))
print(student)

# update Function
print(student.update({"Age":"20"}))
print(student)

# values Function
print(student.values())

# items Function(it will print all the items)
print(student.items())

# popitem (This function remove last item)
print(student.popitem())
print(student)

# clear
print(student.clear())
print(student)
