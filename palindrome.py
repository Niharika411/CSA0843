#program to check whether a given string is a palindrome or not
#G.Niharika
string = input("enter the string : ")

if(string == string[:: - 1]):
   print("The given string is palindrome")
else:
   print("The given string is not a palindrome")


