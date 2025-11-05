# list comprehension  ----> for create a list

li = [i + 2 for i in range(10)]     # [i + 2 for i in range(10)  if i % 2 == 0] 
print(li)

li2 = []
for i in range(10):
    li2.append(i + 2)
print(li)