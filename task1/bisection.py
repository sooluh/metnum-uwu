def f(x):
    '''
    rumus persamaan: 2,99 x ^ 5 - 1,12 x ^ 3 - 1,26

    , diketik menjadi . jika dalam bahasa pemrograman (aturan internasional)
    x adalah nilai variabel yang di "pass" ke dalam parameter fungsi f

    ** artinya ^ (pangkat)
    '''
    return 2.99*x**5-1.12*x**3-1.26


'''
fungsi "bisection" memiliki empat parameter (a, b, e dan n)
parameter e bersifat opsional, secara default terisi sebagai 10^-4 (0.0001)
parameter n pun opsional, secara default terisi sebagai 100
'''
def bisection(a, b, e=10**-4, n=100):
    '''
    deklarasi variabel untuk keperluan iterasi

    step dimulai dari 1 (akan meningkat setiap perulangan)
    condition diinisiasi sebagai True, untuk menjalankan iterasi pertama
    '''
    step = 1
    condition = True

    while condition:
        '''
        deklarasikan nilai c, dimana nilainya berisi sebuah rumus perhitungan
        '''
        c = (a + b) / 2

        '''
        cetak informasi yang didapat

        % didalam python berfungsi untuk concatenation string
        concatenation string adalah penggabungan nilai string dengan variabel atau string lainnya

        %d untuk concatenation bernilai integer
        %f untuk concatenation bernilai float

        %0.4f artinya concatenation bernilai float dengan menerapkan 4 angka dibelakang koma
        \t untuk menggunakan (tab)

        %d (akan) ditimpa dengan nilai dari variabel step
        %0.4f yang pertama ditimpa dengan nilai dari variabel c
        %0.4f yang terakhir ditimpa dengan nilai dari variabel c yang di "pass" ke fungsi f untuk menemukan nilai f(x)
        '''
        print('Iterasi ke-%d,\tC = %0.4f dan f(C) = %0.4f' % (step, c, f(c)))

        '''
        jika f(a) x f(c) < 0 maka c adalah b (variabel b ditimpa dengan nilai dari variabel c)
        selain itu maka c adalah a (variabel a ditimpa dengan nilai dari variabel c)
        '''
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        '''
        variabel step ditingkatkan (+1) disetiap iterasi

        fungsi abs adalah fungsi bawaan python
        untuk menentukan nilai absolut dari sebuah bilangan
        hah?

        misalkan ada sebuah nilai -2.034, dimasukkan ke dalam fungsi abs,
        maka hasilnya 2.034 (tidak mempedulikan simbol negatif atau positif)

        ketika nilai divariabel c dimasukkan ke dalam fungsi f(x)
        lalu hasilnya masih lebih daripada nilai toleransi (dalam hal ini 10^-4)
        dan iterasi masih kurang dari sama dengan variabel n (100)
        maka variabel condition akan bernilai true dan iterasi akan terus berlanjut
        '''
        step = step + 1
        condition = abs(f(c)) > e and step <= n

    '''
    ketika iterasi berhenti, artinya variabel condition bernilai false
    kemungkinan, antara f(c) sudah melebihi batas toleransi
    atau iterasi sudah melebihi 100 (nilai dari parameter n)
    maka artinya, kita sudah menemukan akarnya
    '''
    print('\nDitemukan, akarnya adalah: %0.4f' % c)


'''
pada screenshot di atas, menggunakan metode tabel untuk menentukan batas bawah dan batas atas
didapat angka 1 sebagai batas bawah dan 2 sebagai batas atas
angka tersebut dimasukkan kedalam fungsi float untuk menghasilkan nilai pecahan (1.0 dan 2.0)
'''
a = float(0)
b = float(1)

'''
divalidasi bahwa batas atas dan bawah memang benar bernilai 1 dan 2
ketika f(a) x f(b) lebih dari 0 (float = 0.0)
maka algoritma biseksi tidak bisa dijalankan, ini adalah human error!
'''
if f(a) * f(b) > 0.0:
    print('Nilai yang diberikan harus diantara akar.')
else:
    '''
    ketika batas atas dan bawah tepat
    maka nilai a dan b dimasukkan ke fungsi bisection
    untuk menjalankan metode bisection menggunakan python
    '''
    bisection(a, b)
