#number is 12004509 all 0’s are replays of 1’s so number is 12114519
a=input("Enter the value :")
for x in range(len(a)):
    if int(a[x])==0:
        print(1,end="")
    else:
        print(a[x],end="")