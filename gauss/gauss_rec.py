from gauss.matrix import subtract_rows, multiply_row


def solve(triangular, result=None):
    result = result or []

    if triangular == []:
        return result

    equation = triangular[0]
    coefficients = equation[1:-1]
    right_side = equation[-1]

    left_side = zip(coefficients, result)
    left_side = sum([a * x for a, x in left_side])

    right_side -= left_side

    value = right_side / equation[0]
    result.insert(0, round(value, 3))

    return solve(triangular[1:], result)


def zero_column(matrix, row, result=None):
    result = result or []

    if matrix == []:
        return result

    multiplier = matrix[0][0] / row[0]
    subtract_row = multiply_row(row, multiplier)

    result.append(subtract_rows(matrix[0], subtract_row)[1:])

    return zero_column(matrix[1:], row, result)


def make_triangular(matrix, result=None):
    result = result or []

    result.append(matrix[0])
    if len(matrix) == 1:
        return result

    matrix = zero_column(matrix[1:], matrix[0])

    return make_triangular(matrix, result)



def gauss(matrix):
    triangular = make_triangular(matrix)

    reversed_values = solve(list(reversed(triangular)))

    return list(reversed(reversed_values))


if __name__ == '__main__':
    from gauss.matrix import MATRIX
    gauss(MATRIX)
