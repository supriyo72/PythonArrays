#numpy
from numpy import *
# vals= array([2,4,5,7,6])
# print(vals)

# vals= array([2,4,5,7,6])

# vals= array([2.9,4,5.8,7.4,6]) #will fully convert all integers into float
# o/p:  [2.9 4.  5.8 7.4 6. ]

# vals= array([2,4,5,7,6],float)  #will fully convert all integers into float
# print(vals.dtype)
# print(vals)





#linspace()
# values= linspace(start,stop,parts)
# values= linspace(0,15,16)  #0 to 15 will be divided in 16 parts
# values= linspace(0,15,20)
# values= linspace(0,10,15)  
# values= linspace(0,10)  #bydefault is 50
# print(values)






#arange
# # valss= arange(start,stop,steps)
# valss= arange(2,16,2)
# print(valss)



#logspace
# valz= logspace(log1,log2,parts)
# valz=logspace(1,40,5)
# print(valz)




#ones and zeros

# one= ones(5)  #o/p:  [1. 1. 1. 1. 1.]
one= ones(5,int) #o/p: [1 1 1 1 1]
print(one)

zero= zeros(5,int)
print(zero)