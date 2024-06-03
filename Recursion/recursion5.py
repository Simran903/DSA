# print from 1 to N using backtracking
N = int(input("Enter the value of n: "))
def numbers(i, N):
    if (i < 1): return True
    else:
        numbers(i-1, N)
        print(i)

numbers(N, N)