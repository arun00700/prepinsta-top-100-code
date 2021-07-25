#2^1=2, 1^3+5^3+3^3 = 153, 2^4+4^4+5^4+6^4=2456 (power up with number of digit)
for i in range(1000000):
    num = str(i)
    a = 0
    for x in range(len(num)):
        b = int(num[x])
        c = pow(b,len(num))
        a = a + c
    if num == str(a):
        print(num, " the is Armstrong Number")

