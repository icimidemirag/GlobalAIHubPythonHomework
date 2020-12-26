import time 
import sys 
from decimal import Decimal 

test=0

ad=str("İçimi")
soyad=str("Demirağ")
for i in range(3):
    if ad==input(str("Adınız (Girdiğiniz her kelimenin ilk harfini büyük yazınız.): ")):
        if soyad==input(str("Soyadınız (Girdiğiniz her kelimenin ilk harfini büyük yazınız.): ")):
            break
        else:
            print("Soyadınızı yanlış girdiniz.")
            test+=1
    else:
        print("Adınızı yanlış girdiniz.")
        test+=1
if test==3:    
    sys.exit()

def dersSeçimi(j=1,i=0):
    dersler = ["matematik","fizik","programlama","kimya","biyoloji"]
    print("\nAlabileceğiniz dersler: ")
    print(dersler)
    seçilen_dersler = []
    j=1

    while i<5:
        a=str(input("\nDers seçimi: ")).lower()
        try:
            dersler.index(a)
            seçilen_dersler.append(a)
            dersler.remove(a)
            if i<4:
                print("\nSeçtiğiniz dersler: ",seçilen_dersler)
                print("\nSeçebileceğiniz dersler: ",dersler)
            i+=1
        except:
            print("\nBu dersi daha önce seçtiniz ya da dersin adını yanlış girmektesiniz. Lütfen yeniden bir ders seçiniz.\n")
            print("Seçebileceğiniz dersler: ",dersler)
        if i<5:
            try:
                x=int(input("\n\nDers seçimine devam etmek istiyor musunuz? Çıkmak için(0) / Devam etmek için herhangi bir değer giriniz: "))
            except:
                x=1
        if x==0:
            break
    return seçilen_dersler

k=1
liste = list(dersSeçimi())
while k!=0:
    y=int(len(liste))
    if y<3:
        print("\nYeterli sayıda ders seçmediniz. Yeniden derslerinizi seçiniz.")
        dersSeçimi()
    else:
        k=0

z=int(0)
print("\nSeçtiğiniz dersler:\n")
while z<y:
    print(z,". ", liste[z])
    z+=1

while True: 
    try:
        m=int(input("\nSeçtiğiniz dersler arasından sınava girmek istediğiniz dersin numarasını giriniz: "))
        break
    except:
        print("\nGeçersiz değer girdiniz.")
        True
        
        
while m>=y or m<0:
    print("\nGeçersiz sayi girdiniz.")
    m=int(input("\nSeçtiğiniz dersler arasından sınava girmek istediğiniz dersin numarasını giriniz: "))
    if m<y and m>=0:
        break
print("\nSeçtiğiniz ders: ",liste[m])

time.sleep(2)
print("\nVize notunuzun %30'u ortalamanıza etki edecektir.")
print("Final notunuzun %50'si ortalamanıza etki edecektir.")
print("Proje notunuzun %20'si ortalamanıza etki edecektir.")

notlar = {"Vize":0,"Final":0,"Proje":0}
v=notlar['Vize'] = float(input("\nVize notunuzu giriniz: "))
f=notlar['Final'] = float(input("Final notunuzu giriniz: "))
p=notlar['Proje'] = float(input("Proje notunuzu giriniz: "))

while True:
    if v<0 or v>100 or f<0 or f>100 or p<0 or p>100:
        print("\nHatalı giriş! Notlarınız 0-100 arasında olmalıdır.") 
        v=notlar['Vize'] = float(input("\nVize notunuzu giriniz: "))
        f=notlar['Final'] = float(input("Final notunuzu giriniz: "))
        p=notlar['Proje'] = float(input("Proje notunuzu giriniz: "))
    else:
        break
    
print("\n",notlar)

sonuc = Decimal(v*0.3 + f*0.5 + p*0.2)
ortalama = round(sonuc,2)
time.sleep(1)
print("Bu dersten yıl sonu ortalamanız: ",ortalama,"\n")
time.sleep(1)
if ortalama<30:
    print("Harf notunuz: FF")
    time.sleep(1)
    print("\nDersi geçemediniz.")
elif ortalama>=30 and ortalama<50:
    print("Harf notunuz: DD")
elif ortalama>=50 and ortalama<70:
    print("Harf notunuz: CC")
elif ortalama>=70 and ortalama<90:
    print("Harf notunuz: BB")
elif ortalama>=90 and ortalama<=100:
    print("Harf notunuz: AA")

time.sleep(1)

# Made by 'İçimi Demirağ' and 'Ali Mert Kocaman' :)