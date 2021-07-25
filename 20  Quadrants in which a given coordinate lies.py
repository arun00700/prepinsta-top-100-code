#+X+Y where both the points are at positive X-axis and positive Y-axis so we call this as the First quadrant.
#-X+Y where one point lies at the negative X-axis and other at positive Y-axis so we call it the Second quadrant.
#-Y-X where both the points lie at negative X-axis and negative Y-axis so we call it the Third quadrant.
#-Y+X where one point is at the negative Y-axis and the other one is at positive X-axis so we call it the Fourth quadrant.
x=int(input("enter the value :"))
y=int(input("enter the value :"))
if x==0 and y==0:
    print("origin")
if x>0:
    if y>0:
        print("first")
    else:
        print("second")

elif x<0:
    if y>0:
        print("second")
    else:
        print("four")