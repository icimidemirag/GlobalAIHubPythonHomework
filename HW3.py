import random
import string
import time

kelimeler=["python","java","programlama","bilgisayar","kodlama","ekran","anakart"]
ad=input("Adınızı giriniz: ")
time.sleep(1)
print("\nMerhaba",ad,",oyuna hoş geldiniz!")
time.sleep(1)
input("\nHazır mısınız? Hazır olduğunuzda ENTER tuşuna basınız...")

kelime = random.choice(kelimeler)
kelime = kelime.upper()
kelimeninHarfleri = set(kelime)
alfabe = set(string.ascii_uppercase)
kullanılanHarfler = set()
can = 6

while len(kelimeninHarfleri) > 0 and can > 0:
    print("\nKalan canlarınız: ",can)
    print("\nŞu ana kadar kullandığınız harfler: ", " ".join(kullanılanHarfler))
    kelimeList = [harf if harf in kullanılanHarfler else "-" for harf in kelime]
    print("\nKelime: ", " ".join(kelimeList))

    girilenHarf = input('\nBir harf giriniz: ').upper()
    if girilenHarf in alfabe:
        kullanılanHarfler.add(girilenHarf)
        if girilenHarf in kelimeninHarfleri:
            kelimeninHarfleri.remove(girilenHarf)
        else:
            can-=1
            print("\n", girilenHarf, "harfi kelimede bulunmamaktadır.")
    elif girilenHarf in kullanılanHarfler:
        print("\nBu harfi zaten seçtiniz, lütfen yeni bir harf giriniz.")
    else:
        print("\nHatalı giriş yaptınız!")

if can == 0:
    print("\nOyunu kaybettin! Doğru kelime buydu: ", kelime, '!')
else:
    print("\nKazandın! Doğru kelime buydu:", kelime, '!')