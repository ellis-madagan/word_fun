import string

def palindrome(s):
    translator = str.maketrans('', '', string.punctuation)
    s = s.replace(' ', '').lower().translate(translator)
    return s[::-1] == s

