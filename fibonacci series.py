#program to find fibonacci series of a given number
#G.Niharika
print("enter the value")
n=int(input("n="))
n1=int(input("n1="))
n2=int(input("n2="))
print("fibonacci series:",n1,n2,end=" ")
for i in range(2,n):
  n3=n1+n2
  n1=n2
  n2=n3
  print(n3,end=" ")

