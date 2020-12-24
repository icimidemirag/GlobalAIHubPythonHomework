bilgi= []
ad=str(input("Adınız: "))
soyad=str(input("\nSoyadınız: "))
yaş=int(input("\nYaşınız: "))
gün=int(input("\nDoğum yılınız: "))
bilgi.append(ad)
bilgi.append(soyad)
bilgi.append(yaş)
bilgi.append(gün)

for i in range(4):
    print("\n",bilgi[i])
    
print(bilgi)

if yaş<18:
    print("\nYou can't go out because it's too dangerous!")
else:
    print("\nYou can go out to the street.")