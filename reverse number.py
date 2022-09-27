n = int(input("Enter the integer number: "))  
revs_number = 0    
while (n > 0):
    remainder = n % 10  
    revs_number = (revs_number * 10) + remainder  
    n = n // 10  
print("The reverse number is : {}".format(revs_number))

    
