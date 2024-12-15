print('PILIH OPSI PERMAINAN')
print('1. Buah')
print('2. Negara')
print('3. Pekerjaan')
print('4. Hewan')
print('5. Warna')
print('6. Sayur')

pilihan = input('Masukkan pilihan Anda:')

if pilihan == '1':
    print('setrobir')
    jawaban = input('Masukkan jawaban Anda:')
    kesempatan = 1

    while jawaban != 'stroberi' and kesempatan != 3:
        print('Jawaban salah! Silahkan coba lagi.')
        kesempatan = kesempatan + 1
        print('kesempatan:', kesempatan)
        jawaban = input('Masukkan jawaban Anda:')
    if jawaban == 'stroberi':
        print('Jawaban benar!')

if pilihan == '2':
    print('arkoe')
    jawaban = input('Masukkan jawaban Anda:')
    kesempatan = 1

    while jawaban != 'korea' and kesempatan != 3:
        print('Jawaban salah! Silahkan coba lagi.')
        kesempatan = kesempatan + 1
        print('kesempatan:', kesempatan)
        jawaban = input('Masukkan jawaban Anda:')
    if jawaban == 'korea':
        print('Jawaban benar!')

if pilihan == '3':
    print('isrtaek')
    jawaban = input('Masukkan jawaban Anda:')
    kesempatan = 1

    while jawaban != 'arsitek' and kesempatan != 3:
        print('Jawaban salah! Silahkan coba lagi.')
        kesempatan = kesempatan + 1
        print('kesempatan:', kesempatan)
        jawaban = input('Masukkan jawaban Anda:')
    if jawaban == 'arsitek':
        print('Jawaban benar!')

if pilihan == '4':
    print('jangin')
    jawaban = input('Masukkan jawaban Anda:')
    kesempatan = 1

    while jawaban != 'anjing' and kesempatan != 3:
        print('Jawaban salah! Silahkan coba lagi.')
        kesempatan = kesempatan + 1
        print('kesempatan:', kesempatan)
        jawaban = input('Masukkan jawaban Anda:')
    if jawaban == 'anjing':
        print('Jawaban benar!')

if pilihan == '5':
    print('ahimt')
    jawaban = input('Masukkan jawaban Anda:')
    kesempatan = 1

    while jawaban != 'hitam' and kesempatan != 3:
        print('Jawaban salah! Silahkan coba lagi.')
        kesempatan = kesempatan + 1
        print('kesempatan:', kesempatan)
        jawaban = input('Masukkan jawaban Anda:')
    if jawaban == 'hitam':
        print('Jawaban benar!')

if pilihan == '6':
    print('tolwer')
    jawaban = input('Masukkan jawaban Anda:')
    kesempatan = 1

    while jawaban != 'wortel' and kesempatan != 3:
        print('Jawaban salah! Silahkan coba lagi.')
        kesempatan = kesempatan + 1
        print('kesempatan:', kesempatan)
        jawaban = input('Masukkan jawaban Anda:')
    if jawaban == 'wortel':
        print('Jawaban benar!')