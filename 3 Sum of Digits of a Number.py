#Enter the Number: 1568    ->  1+5+6+8
#Sum of Digits of a Number: 20

num =int(input("enter the number :"))
num1=str(num)
sum=0
for x in range(0,len(num1)):
     a=int(num1[x])
     sum=sum+a
print("sum of digits is",sum)