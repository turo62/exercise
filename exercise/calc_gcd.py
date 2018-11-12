# Calculates the largest common divisor for two numbers.

def calc_gcd(): 
    
    x = int(input("Enter an integer: "))
    y = int(input("Enter another integer: "))
    if x > y: 
        z = y 
    else: 
        z = x 
    for i in range(1, z+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 
  
print(calc_gcd())