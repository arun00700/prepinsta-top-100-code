#A number is 526625 .If you read number “526625” from reverse order,
# it is same as “526625”.
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")