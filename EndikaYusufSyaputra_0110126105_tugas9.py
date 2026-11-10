#Celcius ke Farenheit
def celciuskefarenheit(celcius):
    hasil=(celcius*(9/5))+32
    print(hasil)

print(celciuskefarenheit(0))
print(celciuskefarenheit(100))

#Genap
def is_genap(bilangan):
    print(bilangan % 2 == 0)

is_genap(4)
is_genap(7)

#Lulus atau Gagal
def nilai(skor):
    if skor >= 80:
        print("Lulus")
    elif skor <= 60:
        print("Gagal")
    else:
        print("game over")

nilai(95)
nilai(70)
nilai(44)

#Bilangan Ganjil
def bilangan(angka):
    for i in range(1, angka+1):
        if i % 2 != 0:
            print(i, end=" ")

bilangan(20)
