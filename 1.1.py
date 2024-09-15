import regex

def is_palindrome(string):
    string = str(string)
    if not isinstance(string, str):
        return False


    cleaned_string = regex.sub(r'[^a-zA-Z0-9]', '', str(string)).lower()


    return cleaned_string == cleaned_string[::-1]
print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))














