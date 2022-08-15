from array import *
# arr= array('i', [])
# n= int(input('Enter the range: '))

# for x in range(n):
#     num= int(input('Enter the next no: '))
#     arr.append(num)

# search= int(input('What to search: '))
# for z in arr:
#     if search==z:
#         print(str(search) + " found")









arr= array('i', [])
n= int(input('Enter the range: '))

for x in range(n):
    num= int(input('Enter the next no: '))
    arr.append(num)

search= int(input('What to search: '))
for z in range(0,len(arr)):
    if search== arr[z]:
        print(str(search) +" index is: " +str(z))