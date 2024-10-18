def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
 #test
print(is_palindrome("Bronya"))
print(is_palindrome("QwQ"))