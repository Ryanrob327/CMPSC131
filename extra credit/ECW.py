"""
Course  : CMPSC 131, Fall 2024
File    : ECW.py 
Name    : Ryan McWeeny

GitHub User:   Ryanrob327

Collaboration Statement: I worked on this assignment by myself, using only course materials
"""

def lower_case_str(string: str) -> str:
    result: str = ""
    for char in string:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def are_twins(psuid1: str, psuid2: str) -> bool:
    """
        checks if two psu ids are equivalent but one number apart

        Input:
        psuid1 [str]: the first psu id, psuid2 [str]: the second psu id

        Output: 
        [bool] true is both ids are identical but one number apart
    """
    initials1: str = lower_case_str(psuid1[:3])
    initials2: str = lower_case_str(psuid2[:3])
    
    number1: int = int(psuid1[3:])
    number2: int = int(psuid2[3:])
    
    return initials1 == initials2 and abs(number1 - number2) == 1


def sum_fold(lst: list[int]) -> None:
    """
        modifies existing list such that each element is the sum of all elements before it

        Input:
        lst [list[int]]: the original list to be modified

        Output: 
        [None] function is void but modifies the list passed into it
    """
    accumulated_sum: int = 0
    temp_value: int = 0
    for i in range(len(lst)):
        temp_value = lst[i]
        lst[i] += accumulated_sum
        accumulated_sum += temp_value