from array import *

arr= [2,4,3,5,6]
sum= int(input("Enter the sum: "))
result= [ ]
# for z in arr:
#     res= sum+z
#     result.append(res)
    
# print(result)

for z in range(len(arr)):
    res= arr[z]+sum
    result.append(res)
    
print(result)

