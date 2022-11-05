say1 = int(input("Sayı gir:"))
toplam = 0
for i in range(1,say1):

    if(say1 %i == 0):

        toplam = toplam + i

if(say1 == toplam):
    print("{} sayısı mükemmel bir sayıdır.".format(say1))
else:
    print("{} sayısı mükemmel bir sayı değildir.".format(say1))

