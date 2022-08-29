from array import *
arr= array('i',[2,4,3,5,6])
newarr= array(arr.typecode, (a+a for a in arr))
i=0
while(i<len(arr)):
    print(newarr[i],end=" ")
    
    i+=1
