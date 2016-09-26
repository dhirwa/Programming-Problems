def reverse_string(string):
    new = string[::-1]
    return new



def palindrome(s):
    if s == reverse_string(s):
        return True

    else:
        return False

print palindrome("Hell")
