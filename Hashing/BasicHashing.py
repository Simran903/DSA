def countNum():
    # Read the length of the array from user input
    n = int(input("Enter the length of array: "))
    arr = []

    # Read n elements into the array from user input
    for i in range(n):
        arr.append(int(input("Enter the element: ")))

    # Precompute the hash map (dictionary) to count occurrences of each number
    hash_map = {}
    for i in range(n):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1  # Increment the count if the number is already in the hash_map
        else:
            hash_map[arr[i]] = 1  # Initialize the count to 1 if the number is not in the hash_map

    # Read the number of queries from user input
    query = int(input("Enter the number of queries you want to perform: "))

    # Process each query
    while query > 0:
        # Read the number for which the count is to be fetched
        number = int(input("Enter the number: "))
        
        # Fetch the count from hash_map, default to 0 if number not found
        print(hash_map.get(number, 0))
        
        # Decrement the query counter
        query -= 1

# Call the function to execute the above logic
countNum()
