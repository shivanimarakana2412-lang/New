import myModule

myModule.greet()

result = myModule.add(1, 2, 3, 4, 5)
print("The sum is:", result)


li = [12 , 55 , 74 , 25 , 15 , 156 , 782 , 45]
 
fruits = ["apple", "banana", "cherry", "date"]

print(sorted(li))     
print(sorted(li, reverse=True)) 

print(sorted(fruits))
print(sorted(fruits , key=len))      
print(sorted(fruits , reverse=True))


newli = list(map(lambda x: x*2 , li))
print(newli)

newfruits = list(map(lambda x: x.upper() , fruits))
print(newfruits)

fli = list(filter(lambda x: x%2==0 , li))
print(fli)

mli = list(map(lambda x: x*2 , li))
print(mli)

from functools import reduce
newlist = reduce(lambda x , y: x+y , li)
print(newlist)