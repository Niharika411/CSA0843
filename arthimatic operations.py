#program for arthimatic operations
#G.Niharika
print("enter the values")
x=int(input("x="))
n=int(input("n="))
print(" 1 for power\n 2 for addition\n 3 for subtraction\n 4 for multiplication\n 5 for division\n")
choice=int(input("enter your choice"))
pow=x**n
add=x+n
sub=x-n
mul=x*n
div=x/n
if(choice==1):
    print("power of x and n is:",pow)
elif(choice==2):
    print("addition of x and n is:",add)
elif(choice==3):
    print("subtraction of x and n is:",sub)
elif(choice==4):
    print("multiplacation of x and n is:",mul)
elif(choice==5):
    print("division of x and n is:",div)
else:
    print("invalid input")

