

def sum_while(l, result=0):
    while True:
      if l == []:
          return result
      result += l[0]
      l = l[1:]


if __name__ == '__main__':
    from sum_data import DATA

    sum_while(DATA)
