def gcd(a, b):
    while (a > 0 and b > 0):
        if (a > b):
            a = a % b
        else:
            b = b % a
    
    if (a == 0):
        return b
    else:
        return a
    
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(gcd(a, b))