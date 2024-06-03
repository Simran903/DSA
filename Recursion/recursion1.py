n = int(input("How many times to print: "))
count=0
def func1(count, n):
    if count == n: return
    else:
        print("Hello world")
        count += 1
        func1(count, n)

func1(count, n)