# Tuples

fruit=("apple","baba","mango")
number=(1,4,2,7,4)
print(type(fruit))

print(number.index(4))
print(fruit.index("mango"))
print(list(tuple(number)))


# set

s={1,3,4,2,1}
j={1,4}
l=[1,1,8,5,5]
print(set(l))
print(list(set(l)))
# set opeartion

print(s.intersection(j)) # it dispaly same value present in both set
print(s.union(j))# it display all the numbers presents in it
print(s.difference(j))
print(s.add(123))
print(s)
s.pop()
print(s) #remove 1
s.pop()
print(s)
print(j.issubset(s))
print(s.issubset(j))


