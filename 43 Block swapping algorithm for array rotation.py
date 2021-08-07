a=list(map(int,input("ENTER ARRAY ELEMENTS :").split()))
b=int(input("enter the number  of left rotation :"))
for x in range(b):
  for i in range(len(a)-1):
      a[i],a[i-1]=a[i-1],a[i]
print(a)