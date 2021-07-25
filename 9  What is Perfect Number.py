#28 ->factor 1,2,4,7,14 add up to 28
a=int(input('Enter the number :'))
b=0
for x in range(1,a):
    if a%x==0:
        b=b+x

if a==b:
    print(a,'is prefect number')
else:
    print(a, 'is not prefect number')
