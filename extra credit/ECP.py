def dot_product(lst1: list[int], lst2: list[int]) -> int:
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
    parentheses_count = 0
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
    count: int = 0
    for i in range(len(lst)):
        if (lst[i] >= i - n) and (lst[i] <= i + n):
            count += 1
    return count

def move_to_back(lst, values):
    to_move = []
    for j in values:
        i = 0
        while i < len(lst):
            if lst[i]  == j:
                to_move.append(lst.pop(i))
            else:
                i += 1
    for elem in to_move:
        lst.append(elem)
        