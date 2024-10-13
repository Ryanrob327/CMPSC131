"""
Course  : CMPSC 131, Fall 2024
File    : ECP.py 
Name    : Ryan McWeeny

GitHub User:   Ryanrob327

Collaboration Statement: I worked on this assignment by myself, using only course materials
"""

def title_case(string: str) -> str:
    """
        properly capitalizes string by capitalizing first letter of each word and lower casing every other letter

        Input:
        string [str]: string to be modified into proper capitalization

        Output: 
        [str] properly capitalized string
    """
    words: str = string.split()
    result: list[str] = []
    for word in words:
        new_word: str = ""
        for i, char in enumerate(word):
            if i == 0 and 'a' <= char <= 'z':
                new_word += chr(ord(char) - 32)
            elif i != 0 and 'A' <= char <= 'Z':
                new_word += chr(ord(char) + 32)
            else:
                new_word += char 
        result.append(new_word)
    return ' '.join(result)

def dot_product(lst1: list[int], lst2: list[int]) -> int:
    """
        multiplies index of each list by corresponding index of other list respectively and add all products together

        Input:
        lst1 list[int]: first list, lst2 list[int]: second list

        Output: 
        [int] sum of dot products
    """
    length: int = 0
    sum: int = 0
    if len(lst1) <= len(lst2):
        length = len(lst1)
    else:
        length = len(lst2)
    for i in range(length):
        sum += lst1[i] * lst2[i]
    return sum

def is_balanced(a_str: str) -> bool:
    """
        checks if string has balanced parenthesis, if so, returns true, otherwise, returns false

        Input:
        a_str [str]: string to check for parenthesis

        Output:
        [bool] balanced parenthesis or not
    """
    parentheses_count: int = 0
    for char in a_str:
        if char == '(':
            parentheses_count += 1
        elif char == ')':
            parentheses_count -= 1
        if parentheses_count < 0:
            return False
    if parentheses_count == 0:
        return True
    else:
        return False 
    
def almost_there(lst: list[int], n: int) -> int:
    """
        returns how many elements of the list are within "n" of the respective element's index

        Input:
        lst [list[int]]: list of elements to check, n [int]: number to check against elements from lst

        Output:
        [int] number of elements in lst within "n" of the respective elements index
    """
    count: int = 0
    for i in range(len(lst)):
        if (lst[i] >= i - n) and (lst[i] <= i + n):
            count += 1
    return count

def move_to_back(lst: list[int], values: list[int]):
    """
        mutates list so that each element in list that also appears in "values" is moved to the back of the list
        
        Input:
        lst [list[int]]: list of elements to mutate, values [list[int]]: list of numbers to move to back of lst

        Output:
        [void] function returns void but mutates lst
    """
    to_move: list[int] = []
    for j in values:
        i = 0
        while i < len(lst):
            if lst[i]  == j:
                to_move.append(lst.pop(i))
            else:
                i += 1
    for elem in to_move:
        lst.append(elem)
        