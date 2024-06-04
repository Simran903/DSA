def is_palindrome(x: int) -> bool:
    # Negative numbers are not palindromes
    if x < 0:
        return False

    # Create the reversed number
    original = x
    reversed_num = 0

    while x != 0:
        last_digit = x % 10
        x //= 10
        reversed_num = reversed_num * 10 + last_digit

    return original == reversed_num

print(is_palindrome(787))  # Output: True
print(is_palindrome(-121))  # Output: False
print(is_palindrome(123))   # Output: False
print(is_palindrome(0))     # Output: True
