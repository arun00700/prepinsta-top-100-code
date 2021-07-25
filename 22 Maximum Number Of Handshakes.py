#A maximum number of handshakes that can be possible in a group meeting
# can be defined using a simple math formula but to ease it here is a python program
# that finds the maximum number of handshakes possible in a group of 30 people.
N=int(input("number of person :"))
a= int(N *((N-1)/2))
print(a)