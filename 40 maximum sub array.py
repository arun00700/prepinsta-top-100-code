a=list(map(int,input("Enter array1 :").split()))
b=a[::-1]

for x in range(1,len(a)):
    a[x]=a[x]*a[x-1]
    b[x]=b[x]*b[x-1]

print(max(a+b))
