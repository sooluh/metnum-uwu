def f(x):
    return 2.99*x**5-1.12*x**3-1.26


def regulafalsi(a, b, e=10**-4, n=100):
    step = 1
    condition = True

    while condition:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print('Iterasi ke-%d,\tC = %0.4f dan f(C) = %0.4f' % (step, c, f(c)))

        if f(a) * f(c) > 0:
            a = c
        else:
            b = c

        '''
        jika f(c) = 0 atau akar telah ditemukan, program akan terhenti
        jika |f(c)| < nilai toleransi program akan terhenti
        artinya, nilai toleransi/galat telah tercapai
        '''
        step = step + 1
        condition = f(c) != 0 and abs(f(c)) > e

    print('\nDitemukan, akarnya adalah: %0.4f' % c)


a = float(0)
b = float(1)

if f(a) * f(b) > 0.0:
    print('Nilai yang diberikan harus diantara akar.')
else:
    regulafalsi(a, b)
