#A number is 526625 .If you read number “526625” from reverse order,
# it is same as “526625”.
from array import *
a= int(input("enter the number of input :"))
b=array("i",[])
for x in range(a):
      b1=int(input(("Enter a value :")))
      b.append(b1)
m=[]
for x in range(a):
      c1=str(b[x])
      if c1 == c1[::-1]:
            m.append(c1)
print(max(m))