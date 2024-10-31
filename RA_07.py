# File: RA_07.py         
# Author:  Ryan McWeeny    
# Section: 01R
# E-mail:  rrm5585@psu.edu    
    

def extract_emails(file_name: str) -> list[str]:
    emails: list[str] = []
    file = open(file_name, 'r')
    content = file.readlines()
    for line in content:
        line = line.split()
        for word in line:
            if '@' in word and '.' in word:
                emails.append(word)
    return emails


def is_palindrome(string: str) -> bool:
    for i in range(len(string)):
        if string[i] != string[-(i+1)]:
            return False
    return True
def palindrome_counter(file_name: str) -> int:
    count: int = 0
    file = open(file_name, 'r')
    content: str = file.readlines()
    for line in content:
        line = line.split()
        for word in line:
            if is_palindrome(word):
                count += 1
    return count
                
                    
        