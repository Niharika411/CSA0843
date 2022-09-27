#program to find graetest of three numbers
#G.Niharika
print("enter the values")
a=int(input("first number:"))
b=int(input("second number:"))
c=int(input("third number:"))
if(a>b)and(a>c):
    print("a is greater")
elif(b>a)and(b>c):
    print("b is greater")
else:
    print("c is greater")
