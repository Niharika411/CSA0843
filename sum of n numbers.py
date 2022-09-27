#program to find sum of n numbers
#G.Niharika
print("enter the value")
n=int(input("enter a number:"))
if(n<0):
      print("enter a postive number")
else:
    sum=0
while(n>0):
    sum+=n
    n-=1
    print("sum=",sum)
