# 17.04.2022
# Burak GÜN 
# burak.gun@hotmail.com


# Tip dinamik olarak değişebilir. burak yerine 7 yazsaydım değişken int türünde olacaktı
#Python dilinde tek tırnak ('') ile çift tırnak("") arasında bir fark yoktur.

# Öylesine deneme olarak koydum. İlk harfi büyük harf yapıyor.
x = 'burak gün'.capitalize()

# bütün karakterleri büyük harf yapar
x = x.upper()

print( ' x = {}'.format(x) )
print(f'tür = { type(x) }' )

# Eğer bu şekilde yazdırırsam sonuç : 'Ahmet 4, Mehmet ise 6 yaşındadır' olarak çıkacaktır. Ki bu zaten beklediğimiz bir sonuç.
print('Ahmet {}, Mehmet ise {} yaşındadır'.format(4, 6))

#Ancak kodu bu şekilde değiştirirsek, yani sıralama indeksini değiştirsek, çıktı da değişecektir.
#Buradan şunu anlıyoruz ki, format içindeki sayıların indeksi var ve bunu {} içerisinde yazarak, 
#Hangi sayının çıktı olarak gösterileceği sırasını değiştirebiliriz.

print('Ahmet {1}, Mehmet ise {0} yaşındadır'.format(4, 6))

# Çıktı : Ahmet 6    , Mehmet ise    4 yaşındadır.
# Yani çıktı içerisinde boşluk ekleme yapar
print('Ahmet {1:<5}, Mehmet ise {0:>4} yaşındadır'.format(4, 6))

q = 33
x = f'Yolcu sayısı {6} ve koltu sayisi {q}' 
print(x)


#--------------------------------------------------- Numeric Type ---------------------------------------------------------#

# normalde int/int sonucu int olarak vermesine alışmışken, burada sonuç float olarak döner.
# Eğer int/int sonucunun int dönmesini istiyorsak // işareti ile bölme yapmamız gerekiyor.

var1 = 9/1   # sonuç = 9.0 - Float
var2 = 9//3  # sonuç = 3 - int

print(f'var1 = {var1} var2 = {var2}')
print(type(var1) , type(var2))

# Önemli Not
# Aşağıdaki işlemin sıfır olması gerekir. Ancak virgüllü ifadelerdeli hata payından(precision) dolayı sonuç bu şekilde çıktı.
# Bu yüzden para işlemlerinde float point kullanımlası önerilmez. 
var3 = 0.1 + 0.20 - 0.30 
print(var3)

# Yukarıdaki işlemi sorunsuz çalıştırmak için decimal kütüphanesini import etmemiz gerekmektedir.

from decimal import *

c = Decimal('0.10')
d = Decimal('0.20')

e = c + c - d 
print('e = {}'.format(e))
print(type(e))



#--------------------------------------------------- Bool Type ---------------------------------------------------------#

# Önemli Not
# Burada None türünü de unutmamak lazım. if true ya da if false gibi işlemler yapılırken dikkat etmek de fayda var


var4 = 3 < 4 # True , False  değerleri gelebilir
print('var = {}'.format(var4))
print(type(var4))


#--------------------------------------------------- Sequence Type ---------------------------------------------------------#

#Python da 4 adet built-in veri tipi vardır:
# 1- Tuple
# Sıralama değiştirilemez, veri eklenip çıkartılamaz. 
# () arasına veriler koyulur. 
# Bir tane bile değişlen olsa sonuna virgül konulmak zorundadır. Örnek : ('burak' ,)

var7 = ('22', '45', 'burak')
for r in var7 :
    print(f' r = {r}')


# 2- List
# Dizidir. Veri ekleme çıkarma sıra değiştirme yapılabilir.
# [] arasına veriler koyulur.

var6 = [1, 3, 5, 7, 9, 'burakgün', 13, [23,24]]

for k in var6 :
    print(f' k = {k}')

# 3- Dictionary
# Enum'a benzettim. Değişkene karşılık gelen değeri vardır.
# Ekleme, çıkarma, değiştirme yapılabilir
# {} arasına koyulur

xy = { 'bir': 1, 'iki': 2, 'üç': 3, 'dört':4 }
for k,v in xy.items():
    print(f'key = {k}, value = {v}')



# 4- Set
# Değiştirilemezler, sıraları(index) yoktur
# ilerleyen kısımlarda detaylı bakılacaktır. 



