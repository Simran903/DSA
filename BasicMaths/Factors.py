def divisor(n):
    for i in range(1, n+1):
        if (n % i == 0):
            print(i, end=" ")

# n = int(input("Enter the value of n: "))
# divisor(n)


# Other Approach 
def list_factors(n):
    if n <= 0:
        return "Input should be a positive integer."
    
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    
    factors.sort()
    return factors

# Example usage:
n = int(input("Enter the value of n: "))
print(f"The factors of {n} are: {list_factors(n)}")


