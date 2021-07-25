#Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise
x = int(input())
y = int(input())
z = int(input())
n = int(input())
d=[]
e=[]
for a in range(0,x+1):
    for b in range(0,y+1):
      for c in range(0,z+1):
          d.append([a,b,c])
print(d)
for i in d:
    if sum(i) !=n:
        e.append(i)
print(e)

