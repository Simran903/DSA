n= int(input("Enter the value of n: "))
def name(count = 0):
    if (count == n): return
    else:
        print("Yash Thakur")
        count += 1
        name(count)
name()
