if __name__ == '__main__':
    import timeit, cProfile
    print(timeit.timeit("sum(DATA)", number=1,
                        setup="""
from __main__ import DATA
                        """))

    cProfile.run('sum(DATA)')

    print('Memory profiling')

    from memory_profiler import profile

    profile(sum)(DATA)
