x = {"a": 1, "b": 2, "c": 3}

def invert_dinctionary(dictionary: dict):
    inverted = {}
    for key, value in dictionary.items():
        inverted[value] = key
    return inverted
print(invert_dinctionary(x))