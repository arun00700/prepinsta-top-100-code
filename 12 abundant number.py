#12
#1*12
#2*6
#3*4
#1 + 2 + 3 + 4 + 6=16 > 12 (Abundant Number)
a=int(input("Enter the number :"))
b=0
for x in range(1,a):
    if a%x==0:
        b=b+x
if b>a:
    print(a,"is abundant number")
else:print(a,"is not abundant number")