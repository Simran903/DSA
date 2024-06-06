def main():
    # Read the input string
    s = input()

    # Precompute the frequency of each character in the string
    hash_map = [0] * 26
    for char in s:
        hash_map[ord(char) - ord('a')] += 1

    # Read the number of queries
    q = int(input())
    for _ in range(q):
        # Read the character for which the frequency is to be fetched
        c = input().strip()
        # Fetch and print the frequency from hash_map
        print(hash_map[ord(c) - ord('a')])

if __name__ == "__main__":
    main()
