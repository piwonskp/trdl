

def sum_iter(l):
    result = 0
    for i in l:
        result += i
    return result


if __name__ == '__main__':
    from sum_data import DATA
    sum_iter(DATA)
