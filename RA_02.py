# File: RA_02.py         
# Author:  Ryan McWeeny    
# Section: YOUR_RECITATION_SECTION_HERE
# E-mail:  rrm5585@psu.edu 

def get_code(input: int):
    if input % 2 == 1:
        return 'CMPSC'
    elif input >= 2 and input <= 5:
        return 131
    elif input >= 6 and input <= 20:
        return 'CMPSC'
    elif input > 20:
        return 131
    
def joint(a: int, b: int, c: int):
    if (a+b) % 2 == 0:
        if ((a+b) % 7) % 2 == 1:
            return 1
        else:
            return 2
    elif (a+b+c) % 2 == 1:
        product = (a*b*c)//11
        if product % 2 == 0:
            return 3
        elif product > 10:
            return 4
        else:
            return 5
    else:
        return 6
    
def reverse(input: int):
    num = input
    arr = []
    for i in range(4):
        arr.append(num %10)
        num //= 10
    return (arr[0] * 1000) + (arr[1] * 100) + (arr[2] * 10) + arr[3]

def sum_of_powers(input: int):
    num = input
    arr = []
    for i in range(4):
        arr.append(num %10)
        num //= 10
    return (arr[0] ** 1) + (arr[1] ** 2) + (arr[2] ** 3) + (arr[3] ** 4)

def foo(num):
   counter = num * 2
   value = 2
   if num < 30:
      counter += 1
      print("The value of counter is", counter)
   else:
      print("The value of counter is", counter)


    
print(reverse(1234))
print(sum_of_powers(1234))