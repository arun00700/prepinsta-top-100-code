num =input("enter the value :")
even=[]
odd=[]
for i in range(len(num)):
    if  int(num[i])%2==0:
        even.append(int(num[i]))
    else:
        odd.append(int(num[i]))

if sum(even)>sum(odd):
    print(sum(even)-sum(odd))
else:
    print(sum(odd) - sum(even))
bin()
int()
oct()
hex()