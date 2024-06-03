n = int(input("Enter the value of n: "))
def revNumbers(n):
    if (n <= 0): return
    else:
        print(n)
        n -= 1
        revNumbers(n)


revNumbers(n)