#100101 ->right to left
#         1*2^0 + 0*2^1 + 1*2^2 + 0*2^3 + 0*2^4 + 1*2^5 =37
a=input("enter the value :")
c=0
for x in range(len(a)):
     b=int(a[-1-x])*pow(2,int(x))
     c=c+b

print(c)