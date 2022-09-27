#program to check if a number is prime or not
#G.Niharika
print("enter the number")
n = int(input("n="))
flag = False
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break
if flag:
    print("the given number is a not a prime number")
else:
    print("the given number is a prime number")
