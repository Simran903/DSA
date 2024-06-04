def Armstrong(n):
    # Negative numbers are not armstrongs
    if n < 0:
        return False
    
    original = n
    sum = 0
    while (n > 0):
        lastDigit = n % 10
        sum = sum + (lastDigit ** 3)
        n = n // 10
    
    if (sum == original):
        return True
    else:
        return False

n = int(input("Enter the number: "))
print(Armstrong(n))