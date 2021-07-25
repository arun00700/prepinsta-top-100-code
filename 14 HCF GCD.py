#60 =[1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36]
#72 = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30]
#HCF = common highest value , GCD =Greatest Common Divisor
#Final Answer = 12

a=int(input("Enter the value a :"))
b=int(input("Enter the value b :"))
a1=[]
b1=[]
c=[]
if a<b:
    a,b=b,a
for x in range(2,a):
    if a%x==0:
        a1.append(x)

for x in range(2,b):
 if b%x==0:
        b1.append(x)

for x in range(len(a1)):
    if a1[x] in b1:
       c.append(a1[x])
print(max(c))

