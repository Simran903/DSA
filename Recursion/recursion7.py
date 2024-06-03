# sum of first n numbers using parameterized way
n = int(input("Enter the value: "))
def calc_sum(n, sum):
    if (n < 1):
        print(sum)
        return
    else:
        calc_sum(n-1, sum+n)

# calc_sum(n, 0) #function call

# sum of first n numbers using functional way
def calc_sum_n(n):
    if (n == 0):
        return 0
    else:
        return n + calc_sum_n(n-1)
    
print(f"sum of 1 to {n} is: ",calc_sum_n(n))

# time complexity : O(N)
# space complexity : O(N)