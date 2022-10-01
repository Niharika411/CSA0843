num=int(input("Enter the number of numbers "))
if(num==2):
    p=int(input("Enter First Number: "))
    q=int(input("Enter Second Number: "))
    for i in range(1,p+1):
        if(p%i==0 and q%i==0):
            gcd=i
            print("GCD of %d and %d is %d"%(p,q,gcd))
            lcm=(p*q)/gcd
            print("LCM of %d and %d is %d"%(p,q,lcm))
elif(num==3):
    p=int(input("Enter First Number: "))
    q=int(input("Enter Second Number: "))
    r=int(input("Enter Third Number: "))
    for i in range(1,p+1):
        if(p%i==0 and q%i==0 and r%i==0):
            gcd=i
            print("GCD of %d, %d and %d is %d"%(p,q,r,gcd))
            lcm=(p*q*r)/gcd
            print("LCM of %d, %d and %d is %d"%(p,q,r,lcm))
else:
    print("INVALID INPUT")
    
    
    
