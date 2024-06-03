# reverse ann array using two pointer approach
def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end = " ")
    print()

def reverseArray(arr, n):
    p1 = 0
    p2 = n-1
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    printArray(arr, n)

if __name__ == "__main__":
    arr = []
    length_arr = int(input("Enter the length of array:"))
    for i in range(length_arr):
        ele = int(input("Enter the element of array:"))
        arr.append(ele)
    n = len(arr)
    reverseArray(arr, n)

# time complexity: O(n)
# space complexity: O(1)
    
# reverse ann array using recursive approach

def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()

def reverseArray(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverseArray(arr, start+1, end-1)

if __name__ == "__main__":
    arr = []
    length_arr = int(input("Enter the length of array:"))
    for i in range(length_arr):
        ele = int(input("Enter the element of array:"))
        arr.append(ele)
    n = len(arr)
    reverseArray(arr, 0, n-1)
    printArray(arr, n)

# Time Complexity: O(n)
# Space Complexity: O(1)