n=int(input("enter number of  pairs :"))
arr=[]
for i in  range(n):
    l=list(map(int,input().split()))
    arr.append(l)
print(arr)

try:
 for i in range(n):
        a = arr.count(arr[i])
        b = arr.count(arr[i][::-1])
        if a + b > 1:
            print(arr[i])
            try:
             arr.remove(arr[i])
             arr.remove(arr[i][::-1])
            except:
                print()
except:
    print()
