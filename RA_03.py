# File: RA_03.py         
# Author:  Ryan McWeeny    
# Section: 001R
# E-mail:  rrm5585@psu.edu 


# Part 1
def get_sum_for():
    sum = 0
    for i in range(1, 101):
        sum += 1/i
    return sum
def get_sum_while():
    sum = 0
    i = 1
    while i <= 100:
        sum += 1/i
        i += 1
    return sum

# Part 2
def sum_multiples_xor(num: int) -> int:
    if num <= 0:
        print("Input must be positive")
        return -1
    else:
        total = 0
        count = 0
        for i in range(1,num):
            mul_of_3 = i % 3 == 0
            mul_of_7 = i % 7 == 0
            if (mul_of_3 or mul_of_7) and not (mul_of_3 and mul_of_7):
                total += i
                count += i
        print("Count of numbers summed:", count)
        return total

# Part 3
def get_index(num, digit) -> int:
    running = True
    number = num
    i = 1
    while running:
        if number % 10 == digit:
            return i
        elif number == 0:
            return -1
        else:
            number //= 10
            i += 1


print(sum_multiples_xor(240))