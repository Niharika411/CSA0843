#program to find factorial of a number
#G.Niharika
print("enter the number")
n=int(input("n="))
factorial=1
if(n==0):
    print("the factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
print("factorial value of",n,"is",factorial)
