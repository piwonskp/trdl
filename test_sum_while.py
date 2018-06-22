from sums.sum_while import sum_while
from sums.sum_data import DATA


if __name__ == '__main__':
    import timeit, cProfile
    print('Czas trwania:',
          timeit.timeit("sum_while(DATA)", number=1,
                        setup="""
from __main__ import sum_while
from __main__ import DATA
                        """))

    cProfile.run('sum_while(DATA)')

    print('Memory profiling')

    from memory_profiler import profile

    profile(sum_while)(DATA)
