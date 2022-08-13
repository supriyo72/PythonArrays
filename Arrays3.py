# from array import *
# vals= array('i',[5,9,7,8,4,2])
# Newarr= array(vals.typecode, (a for a in vals))

# for e in Newarr:
#     print(e)





# from array import *
# vals= array('i',[5,9,7,8,4,2])
# Newarr= array(vals.typecode, (a*a for a in vals))

# for e in Newarr:
#     print(e)





from array import *
vals= array('i',[5,9,7,8,4,2])
Newarr= array(vals.typecode, (a*a for a in vals))

i=0
while(i<len(Newarr)):
    print(Newarr[i])
    
    i+=1
    