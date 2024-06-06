# counting the frequency of numbers in an array.
def main():
    # Read the length of the array
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    # Precompute the hash array with size 13
    hash_map = [0] * 13
    for num in arr:
        hash_map[num] += 1

    # Read the number of queries
    q = int(input())
    for _ in range(q):
        # Read the number to query
        number = int(input())
        # Fetch and print the count from hash_map
        print(hash_map[number])

if __name__ == "__main__":
    main()