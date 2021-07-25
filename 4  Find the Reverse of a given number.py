#Find the Reverse of a given number
num =input("enter the number :")
print("Reverse of a Number :",end="")
for x in range(len(num),0,-1):
     print(x,end="")

print("\n",num[::-1])