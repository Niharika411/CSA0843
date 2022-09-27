#program to chek if the given string is anagram or not
#G.Niharika
print("enter the strings")
s1=input("s1=")
s2=input("s2=")
if(sorted(s1)== sorted(s2)):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")        
         
