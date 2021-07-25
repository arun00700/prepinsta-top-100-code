#n=25, 25*25=625  Output: Automorphic (last digits are n)
#n=76, 76*76=5776  Output: Automorphic (last digits are n)
for a in range(1,10000000000):
    b = a * a
    a = str(a)
    b = str(b)
    c = 0
    for x in range(len(a)):
        if a[-1 - x] == b[-1 - x]:
            c += 1

    if c == len(a):
        print(a, "automorphic value")

    else:
        pass
        #print(a, " is not automorphic value")


