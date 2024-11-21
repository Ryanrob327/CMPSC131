# File: RA_09.py         
# Author:  Ryan McWeeny    
# Section: 01R
# E-mail:  rrm5585@psu.edu   

def get_count(lst: list[int], num: int) -> int:
    if not lst:
        return 0
    if lst[0] == num:
        return 1 + get_count(lst[1:], num)
    else:
        return get_count(lst[1:], num)
    
def has_numbers(num1: int, num2: int) -> int:
    num1_last_digit = num1 % 10
    num2_last_digit = num2 % 10
    if num1 == 0:
        return True
    elif num2 == 0:
        return False
    if num1_last_digit == num2_last_digit:
        return has_numbers(num1 // 10, num2 // 10)
    else:
        return has_numbers(num1, num2 // 10)

def hailstone(num: int) -> int:
    if num == 1:
        return [1]
    if num % 2 == 0:
        return [int(num)] + hailstone(num / 2)
    else:
        return [int(num)] + hailstone(3 * num + 1)
    