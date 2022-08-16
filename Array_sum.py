from numpy import *

# arr= array([2,3,5,4])
# arr1=array([5,6,8,7,3])
# arr2=array([3,6,5,7,8])
# arr3= arr1+arr2
# print(sum(arr))
# print(sqrt(arr))
# print(log(arr))
# print(arr3)
# print(max(arr))
# print(min(arr))
# print(concatenate([arr1,arr2]))



#copying arrays
# arr4=array([5,6,8,7,3])
# arr5 = arr4.view()

# print(arr4)
# print(arr5)
#id's are same which has to be different
# print(id(arr4))
# print(id(arr5))



arr6=array([5,6,8,7,3])
arr7 = arr6.copy()

arr6[1]= 10   #arr5 also changes which has to be different
print(arr6)
print(arr7)

