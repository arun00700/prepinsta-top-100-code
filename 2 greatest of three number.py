a=int(input("enter nummber a:"))
b=int(input("enter nummber b:"))
c=int(input("enter nummber c:"))
if a>b>c:
    print(a,"greatest number")
elif b>c>a:
    print(b,"greatest number")
elif c>b>a:
    print(c, "greatest number")
else:print("enter correct value")