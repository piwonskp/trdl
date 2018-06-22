from sums.sum_iter import sum_iter
from sums.sum_data import DATA


if __name__ == '__main__':
    import timeit, cProfile
    print('Czas trwania:',
          timeit.timeit("sum_iter(DATA)", number=1,
                        setup="""
from __main__ import sum_iter
from __main__ import DATA
                        """))

    cProfile.run('sum_iter(DATA)')

    print('Memory profiling')

    from memory_profiler import profile

    profile(sum_iter)(DATA)
