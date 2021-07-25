val=int(input("enter the value :"))
num=[]

for a in range(val):
    if a > 1:
        for x in range(2, a):
            if a % x == 0:
                break
        else: num.append(a)
                                   #for 30 =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for x in range(len(num)):         #take every value in num list
    for i in range(len(num)):     #take first value
         if num[x]+num[i]==val:   #2+3 2+5 2+6 2+7 2+11 2+13 2+17 2+19 2+23 2+29
              if num[x]<=num[i]:  #to avoid repeativity
                  print(num[x], " and ", num[i], " are prime numbers when added gives 30")
print(num)