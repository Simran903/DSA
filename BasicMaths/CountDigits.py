def countDigits(n):
    count = 0
    while (n > 0):
        # lastDigit = n % 10 # extraction of digits
        count += 1
        n = n // 10
    print(count)


countDigits(n = int(input("Enter your number: "))
)