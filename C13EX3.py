## C13 Recursion
# EX3 - Palindrome


def is_palindrome(s):
    if len(s) <= 1:  # base case
        return True
    elif s[0] != s[len(s)-1]:  # base case
        return False
    else:  # Reduction and recursive calls
        return is_palindrome(s[1: len(s) - 1])


def main():
    print("Is moon a palindrome?", is_palindrome("moon"))
    print("Is noon a palindrome?", is_palindrome("noon"))
    print("Is a a palindrome?", is_palindrome("a"))
    print("Is aba a palindrome?", is_palindrome("aba"))
    print("Is ab a palindrome?", is_palindrome("ab"))


main()
