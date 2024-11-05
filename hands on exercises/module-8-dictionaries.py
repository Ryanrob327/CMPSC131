def frequency(a_str: str) -> dict:
    d_count = {}
    
    for char in a_str:
        if char not in d_count:
            d_count[char] = 1
        else:
            d_count[char] = d_count[char] + 1
    return d_count
print(frequency('hello hello world!'))

def get_mixed(d1: dict, d2: dict) -> dict:
    new_d = {}
    for key , value in d1.items():
        if value in d2:
            new_d[key] = d2[value]
    