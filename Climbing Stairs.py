def stairs(n):
    if n<=1:
        return n
    return stairs(n-1)+stairs(n-2)
def count(s):
    return stairs(s+1)
s=int(input("Enter the Number of Steps: "))
print("The Number of Ways we can Climb Stairs:",(count(s)))
