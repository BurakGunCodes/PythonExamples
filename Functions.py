# 14.04.2022
# Burak GÜN 
# burak.gun@hotmail.com

# fonksiyonun geri dönüş (return) değeri yok ise, NONE döndürür


# temel anlamda fonksiyon tanımlanması
def function(n):
    print(n)



def topla(a,b):
    return a+b 



print(f'sonuc = { topla(1,5) }')

# eğer default olarak değer atamak istiyorsak, parametre kısmında bunu belirtiyoruz
def function2 (var = 5):
    print(var)

# fonksiyona değer girişi yapmadığımız için default olarak atanan değer çıktı olarak verir
# Çıktı 5, çünkü default olarak yukarıda 5 olarak yazıldı
function2()

# içerisinde girdi sağlarsak, sağlanan girdiye göre çıktı üretir
# Çıktı 45
function2(45)



# yukarıda toplama işlemince return kullandığımız için, fonksiyonu değişkene atayabiliyoruz
var3 = topla(4,8);
print(var3)

# eğer geri dönüş olmayan bir fonksiyonu değişkene atama yaptığımızda 'None' sonucunu alırız
# Çıktı None
var4 = function2()
print(var4)



# Asal sayı bulma örnek fonksiyonu

# belirlenecek


