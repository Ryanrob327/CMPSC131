# File: RA_05.py         
# Author:  Ryan McWeeny    
# Section: 01R
# E-mail:  rrm5585@psu.edu    

def translate(d: dict, msg: str) -> str:
    words: list = msg.split()
    new_string: str = ""
    for i in range(len(words)):
        if words[i] in d:
            words[i] = d[words[i]]
        if i < (len(words) - 1):
            new_string += words[i] + " "
        else:
            new_string += words[i]
        print(i, len(words))
    return new_string

def get_pair_sum(lst: list[int], target: int) -> tuple | int:
    d: dict = {}
    for num in lst:
        compliment = target - num
        if compliment in d:
            return (compliment, num)
        d[num] = True
    return -1
