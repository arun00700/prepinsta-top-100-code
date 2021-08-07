a=list(map(int,input("ENTER ARRAY ELEMENTS :").split()))
b=int(input("enter the number  of left rotation :"))
for x in range(b):
  a=a[1:len(a)]+a[0:1]
print(a)
#for left rotation frist value goes to last value
# -> 1 2 3 4 5 6
# i1 2 3 4 5 6 1
# i2 3 4 5 6 1 2
# i3 4 5 6 1 2 3