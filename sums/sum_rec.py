

def sum_rec(l, result=0):
    if l == []:
        return result
    result += l[0]
    return sum_rec(l[1:], result)


if __name__ == '__main__':
    from sum_data import DATA
    import sys
    sys.setrecursionlimit(100000)

    sum_rec(DATA)
