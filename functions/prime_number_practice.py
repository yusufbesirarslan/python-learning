# Prime number and divisor practice
# This file contains basic function examples using loops and conditions


def asal_sayilari_bul(sayi1, sayi2):
    """
    Returns a list of prime numbers between sayi1 and sayi2 (inclusive).
    """
    asal_sayilar = []

    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if sayi % i == 0:
                    break
            else:
                asal_sayilar.append(sayi)

    return asal_sayilar


def tam_bolenleri_bul(sayi):
    """
    Returns a list of divisors of the given number (except 1 and itself).
    """
    tam_bolenler = []

    for i in range(2, sayi):
        if sayi % i == 0:
            tam_bolenler.append(i)

    return tam_bolenler


if __name__ == "__main__":
    sayi1 = int(input("1. sayı: "))
    sayi2 = int(input("2. sayı: "))

    print("Asal sayılar:", asal_sayilari_bul(sayi1, sayi2))
    print("20'nin tam bölenleri:", tam_bolenleri_bul(20))
