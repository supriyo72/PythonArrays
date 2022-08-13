from array import *

# arr= array('i', [])
# n= int(input("Enter the length of the array: "))

# for i in range(n):
#     x= int(input("Enter the array: "))
#     arr.append(x)
    
# print(arr)

# k=0
# val= int(input("What to search: "))
# for e in arr:
#     if e==val:
#         print(f"{val} is on index no {k}")
#         break
#     k+=1
    






#practice
# arr= array('i', [])
# n=int(input("no: "))

# for i in range(n):
#     x= int(input("Enter: "))
#     arr.append(x)
    
# print(arr)
# search=int(input("search: "))
# k=0
# for e in arr:
#     if e==search:
#         print(k)
#     else:
#         k=k+1








arr= array('i', [])
n= int(input("Enter the length of the array: "))

for i in range(n):
    x= int(input("Enter the array: "))
    arr.append(x)
    
print(arr)

k=0
val= int(input("What to search: "))
for e in arr:
    if e==val:
        print(arr.index(val))
    