
elemanlar = []

x = int(input("Kaç tane sayi gireceksiniz: ")) # Kullanıcıya kaç tane sayı gireceğini soruyoruz

for i in range(0, x):
    elemanlar.append(input("Sayıları Giriniz: ")) # Girilen her sayıyı elemanlar listesine atıyoruz

# elemanlar = [5,4,3,2,1]
z = len(elemanlar)
print(elemanlar)
for j in range(1, z):
    for i in range(1, z):
        if int(elemanlar[i-1]) > int(elemanlar[i]): # elemanlar listesinin elemanlarını 1.ve 2. eleman, 2. ve 3. eleman şeklinde karşılaştırıyoruz
            sayi = elemanlar[i]
            elemanlar[i] = elemanlar[i-1]
            elemanlar[i-1] = sayi

        print(elemanlar)
