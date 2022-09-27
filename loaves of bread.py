a=int(input("fresh loaves:"))
b=int(input("day old loaves:"))
r=185.00
p=r*a
q=0.6*r*b
t=p+q
if(a<0):
    print("invalid input")
else:
    print("regular price:",r)
    print("Amount of new loaves:",p)
    print("Amount of old loaves:",q)
    print("Total Amount:",t)
