def contains(my_str: str, char: str) -> bool:
    for i in my_str:
        if i == char:
            return True
    return False
print(contains("we are!", "r"))
print(contains("we are!", "s"))

def get_upper(my_str: str) -> str:
    output = ""
    for char in my_str:
        value = ord(char)
        if 65 <= value <= 90:
            output += char
        else:
            upper_char = chr(value - 32)
            output += upper_char
    return output
def is_palindrome(my_str: str) -> bool:
    i = 0
    j = len(my_str) - 1
    my_str = get_upper(my_str)
    while i < j:
        if my_str[i] != my_str[j]:
            return False
        i += 1
        j -= 1
    return True
print(is_palindrome("racecar"))
print(is_palindrome("Racecar"))

def get_user(email: str) -> str:
    user_name = ""
    i = 0
    size = len(email)
    while i < size and email[i] != '@':
        user_name += email[i]
        i += 1
    return user_name
print(get_user("user@gmail.com"))

def keep_it(char: str) -> bool:
    code = ord(char)
    if (code == 32) or (65 <= code <= 90) or (97 <= code <= 122):
        return True
    else:
        return False
def remove_punctuation(text: str) -> str:
    new_string = ""
    for char in text:
        if keep_it(char):
            new_string += char
    return new_string
print(remove_punctuation("guiwalugui.!fa$"))