from sums.sum_rec import sum_rec
from sums.sum_data import DATA


if __name__ == '__main__':
    import timeit, cProfile
    print('Czas trwania:',
          timeit.timeit("sum_rec(DATA)", number=1,
                        setup="""
import sys
from __main__ import sum_rec
from __main__ import DATA


sys.setrecursionlimit(100000)
                        """)
    )

    cProfile.run('sum_rec(DATA)')

    print('Memory profiling')

    import sys
    from memory_profiler import profile

    sys.setrecursionlimit(100000)
    profile(sum_rec)(DATA)
