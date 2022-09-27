def WaterContainer(d,a):
    area=0
    for i in range(a):
        for j in range(i+1,a):
            area=max(area,min(d[j],d[i])*(j-1))
    return area
arr=[]
n=int(input("Enter the Number of Elemnts:"))
for i in range(0,n):
    ele=int(input("Enter the Elements:"))
    arr.append(ele)
s=len(arr)
print(WaterContainer(arr,s))
