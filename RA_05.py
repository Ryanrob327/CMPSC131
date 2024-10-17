# File: RA_05.py         
# Author:  Ryan McWeeny    
# Section: 01R
# E-mail:  rrm5585@psu.edu    

def is_palindrome(lst: list) -> bool:
    for i in range(len(lst)):
        if lst[i] != lst[-(i+1)]:
            return False
    return True
            
def multiply(pol_1: list[int], pol_2: list[int]) -> list[int]:
    result_length = (len(pol_1) -1) + len(pol_2)
    result: list[int] = [0] * result_length
    for i in range(len(pol_1)):
        for j in range(len(pol_2)):
            result[(i+j - result_length)] += pol_1[i] * pol_2[j]
    return result


            