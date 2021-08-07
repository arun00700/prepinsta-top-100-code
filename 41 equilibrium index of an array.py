#1 2 3 4 3 2 1
#   3  =   3
#a[3] is eqlibrium index
a=list(map(int,input("Enter array1 :").split()))
b=0
for i in range(len(a)):
   if sum( a[:i])==sum(a[i+1 : ]):
       print(i)
       break