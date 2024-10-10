# File: RA_04.py         
# Author:  Ryan McWeeny    
# Section: 01R
# E-mail:  rrm5585@psu.edu  

def replace_char(string: str, char_to_replace: str, replacement_char: str) -> tuple:
    num_replacements = 0
    lst = []
    for char in string:
        lst.append(str(char))
    for i in range(len(lst)):
        if lst[i] == replacement_char:
            lst[i] = char_to_replace
            num_replacements += 1
    new_str = ""
    for element in lst:
        new_str += element
    return (new_str, num_replacements)
    
def filter_even(lst: list[int]) -> list[int]:
    new_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            new_lst.append(lst[i])
    return new_lst
    
def filter_even_destructive(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:
            lst.pop(i)
        else:
            i += 1
