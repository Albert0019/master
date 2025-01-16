def is_palindrome(s: str) -> bool:
    s = s.lower()  # Convert to lowercase to ensure case-insensitive comparison
    return s == s[::-1]  # Compare the string with its reverse

# Test
print(is_palindrome("level"))  # True
print(is_palindrome("Bronya"))  # False