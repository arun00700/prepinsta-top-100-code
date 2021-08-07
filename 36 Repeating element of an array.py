from array import *
arr=array("i",map(int,input("ENTER ARRAY ELEMENTS ").split()))
arr=list(arr)
try:
  for x in range(len(arr)):
    if arr.count(arr[x])>1:
        print(arr[x])
        arr.remove(arr[x])
except:
    print()
