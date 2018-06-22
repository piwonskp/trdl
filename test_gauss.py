from gauss.gauss_rec import gauss as gauss_rec
from gauss.gauss_iter import gauss as gauss_iter
from gauss.matrix import MATRIX


if __name__ == '__main__':
    import timeit, cProfile
    from memory_profiler import profile

    print('<<<<<<<<<<<<<<<<<<< ITERACYJNE >>>>>>>>>>>>>>>>>>>')
    print('Czas trwania:',
          timeit.timeit("gauss_iter(MATRIX)", number=1,
                        setup="""
from __main__ import gauss_iter
from __main__ import MATRIX
                        """))

    cProfile.run('gauss_iter(MATRIX)')

    print('Memory profiling')


    profile(gauss_iter)(MATRIX)

    print('<<<<<<<<<<<<<<<<< REKURENCYJNE >>>>>>>>>>>>>>>>>>')
    print('Czas trwania:',
          timeit.timeit("gauss_rec(MATRIX)", number=1,
                        setup="""
from __main__ import gauss_rec
from __main__ import MATRIX
                        """))

    cProfile.run('gauss_rec(MATRIX)')

    print('Memory profiling')

    profile(gauss_rec)(MATRIX)
