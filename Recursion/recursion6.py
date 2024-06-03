# print from N to 1 using backtracking

n = int(input("Enter the value of n: "))

def revNumbers(i, n):
    if (n < i): return
    else:
        revNumbers(i+1, n)
        print(i)

revNumbers(1, n)