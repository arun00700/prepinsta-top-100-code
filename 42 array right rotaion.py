a=list(map(int,input("ENTER ARRAY ELEMENTS :").split()))
b=int(input("enter the number  of rotation :"))
c=[1]
for x in range(b):
    a = a[len(a)-1:len(a)]+a[0:len(a)-1]

    print(a)
#for right rotation last value goes to frist value
# 1 2 3 4 5 6 <-
# 6 1 2 3 4 5 <-i1
# 5 6 1 2 3 4 <-i2
# 4 5 6 1 2 3 <-i3
# 3 4 5 6 1 2 <-i4