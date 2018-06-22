from gauss.matrix import subtract_rows, multiply_row


def solve(triangular):
    result = []

    while triangular != []:
        equation = triangular[0]
        coefficients = equation[1:-1]
        right_side = equation[-1]

        left_side = zip(coefficients, result)
        left_side = sum([a * x for a, x in left_side])

        right_side -= left_side

        value = right_side / equation[0]
        result.insert(0, round(value, 3))

        triangular = triangular[1:]

    return result


def zero_column(matrix, base_row):
    for i, row in enumerate(matrix):
        multiplier = row[0] / base_row[0]
        subtract_row = multiply_row(base_row, multiplier)

        matrix[i] = subtract_rows(row, subtract_row)[1:]

    return matrix


def make_triangular(matrix):
    for i in range(len(matrix)):
        matrix = matrix[:i+1] + zero_column(matrix[i+1:], matrix[i])

    return matrix



def gauss(matrix):
    triangular = make_triangular(matrix)

    reversed_values = solve(list(reversed(triangular)))

    return list(reversed(reversed_values))


if __name__ == '__main__':
    from gauss.matrix import MATRIX
    gauss(MATRIX)
