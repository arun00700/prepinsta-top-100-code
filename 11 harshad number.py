#1729 is a Harshad number since 1 + 7 + 2 + 9 = 19, and 1729 = 19 × 91.
for a in range(1,100):
    a = str(a)
    b = 0
    for x in range(len(a)):
        b = b + int(a[x])

    if int(a) % b == 0:
        print(a, " is harshad number ")
