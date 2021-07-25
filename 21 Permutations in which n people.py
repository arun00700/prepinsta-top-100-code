#a!/(a-b)!
import math
a = int(input('Enter the number of students :'))
b = int(input('Enter the number of seats :'))
a1=math.factorial(a)
b1=math.factorial(a-b)
c=a1//b1
print(c)