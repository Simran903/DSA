n= int(input("Enter the value of n: "))
def number(count=1):
        if (count == n+1): return
        else:
            print(count)
            number(count + 1)

number()
