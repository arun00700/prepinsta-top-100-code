# 6 = (1+2+3+6) / 6       = 2
#28 =(1+2+4+7+14+28) / 28 = 2  (abundancy)

a=int(input("Enter the value a:"))
b=int(input("Enter the value b:"))
a1=0
b1=0
for x in range(1,a+1):
    if a%x==0:
        a1=a1+x
for i in range(1,b+1):
    if b%i==0:
        b1=b1+i
if a1/a==b1/b:
    print(a," and ",b," are friendly pair")
else:
    print(a," and ",b," are not friendly pair")


