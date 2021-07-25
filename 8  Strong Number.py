#n=145  ->1! + 4! + 5! =145(strong number)
#n=124  ->1! + 2! + 4! =27  (not a strong number)
a1 = input("Enter the value :")
d = 0
b = 1

for x in range(len(a1)):
    a = int(a1[x])
    b = 1
    for x in range(a,1, -1):
        b = b * x
    d=d+b

if a1==str(d):
    print(a1,'is strong number')
else:
    print(a1, 'is not strong number')
