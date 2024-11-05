def bar(matrix: list) -> int:
    total = 0
    for element in matrix:
        total += element
    return total

def foo(matrix: list) -> int:
    total = 0
    for row in matrix:
        total += bar(row)
    return total


print(foo([[1,2,3], [4,5,6], [7,8,9]]))