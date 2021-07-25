a=int(input("enter the month :"))
b=int(input("enter the year :"))
if a==2 and b%4==0:
    print("29 days")
elif a==2:
    print("28 days")
elif a in [1,3,5,7,9,11]:
    print("31 days")
else:
    print("30 days")