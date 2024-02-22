def is_palindrome(string: str):
    return string == string[::-1]


print(is_palindrome("bob"))
print(is_palindrome("alabala"))
print(is_palindrome("ne e palindrom"))
