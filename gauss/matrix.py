

def subtract_rows(row, row2):
    return [cell - row2[i] for i, cell in enumerate(row)]


def multiply_row(row, multiplier):
    return [x * multiplier for x in row]

 MATRIX = [
     [9, 3, 4, 7],
     [4, 3, 4, 8],
     [1, 1, 1, 3]
 ]

# import random, sys

# SIZE = 250
# MATRIX = [[random.randint(-sys.maxsize, sys.maxsize) for __ in range(SIZE + 1)] for _ in range(SIZE)]
