# Error Handling in python
# error fixing by using tray and except
l=[1,2,3,4,5,6,7]
for i in range(len(l)+1):
   try:
     print(l[i])
   except IndexError:
      print("errro")


