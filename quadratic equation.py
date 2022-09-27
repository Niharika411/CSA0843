#program to solve quadratic equation
#G.Niharika
import cmath
print("enter the values")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
discriminant=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(discriminant))/(2*a)
root2=(-b+cmath.sqrt(discriminant))/(2*a)
print("root1=",root1)
print("root2=",root2)
