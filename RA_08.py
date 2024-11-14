# File: RA_08.py         
# Author:  Ryan McWeeny    
# Section: 01R
# E-mail:  rrm5585@psu.edu   

def awards(lst: list[list[str]]) -> dict:
    result: dict = {}
    for i in range(len(lst)):
        print(lst[i])
        if lst[i][1] not in result:
            result[lst[i][1]] = 1
        elif lst[i][1] in result:
            result[lst[i][1]] += 1
    return result

def get_largest(lst: list[list[int]]) -> int:
    largest: int = lst[0][0]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if largest < lst[i][j]:
                largest = lst[i][j]
    return largest

def get_row_average(lst: list[list[int]]) -> list[float]:
    result: list[float] = []
    for i in range(len(lst)):
        sum: int = 0
        count: int = 0
        for j in range(len(lst[i])):
            sum += lst[i][j]
            count += 1
        result.append(sum / count)
    return result
    