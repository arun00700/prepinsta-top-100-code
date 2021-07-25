#Number : 16
#Factors: 1, 2, 4, 8, 16

a=int(input("enter the value :"))
for x in range(1,a+1):
    if a%x==0:
        if a==x:
            print(x)
        else:
            print(x,end=",")
