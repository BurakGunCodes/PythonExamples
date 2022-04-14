# 14.04.2022
# Burak GÜN 
# burak.gun@hotmail.com


# by yorum satırıdır. (# ile kullanılır)
# çoğunlukla her satırda bir statement | expression göreceksin. İlla ki koymak istiyorsan noktalı virgül(;) ile yan yana koyabilirsin.
# Python yazılımında boşluklar önemlidir.


print('Burak Gün'); 


import platform

print( 'this is python version {}'.format( platform.python_version() ) )

version2 = platform.python_version()
print('Another way to show. Version is :{} '.format(version2) )



a = 100
b = 550

# WhiteSpace önemlidir. If ve Else kapsamına dikkat et
if a < b :
    print('a < b')
else :
    print('b < a')  
    
# değişken yazdırmak için {} ve .format() kullanılır. 
# .format() string metodudur.  

# tekli değişken
print("değişken1= {}".format (256))

# çoklu değişken
print("değişken1= {}  değişken2 ={}".format (256,12))


# .format() farklı versionu olarak aşağıdaki yapı kullanılır
var1 = 78
var2 = 3
print(f'Sensörden gelen veri1 = {var1} veri2 = {var2}')



# veriyi yan yana yazdırmak için 
# for dögüsü için 'Conditionals_and_Loops.py' dosyasına bakabilirsin.
# end= 'character' içerisindeki character kısmında ne yazarsan onun aysını çıktı arasına yerleştirecek. ' ' bu şekilde boş karakter bırakırsan boş kalacak
# Örnek olarak aşağıdakiler.( 0 5 10 15 20 sayıları for döngüsü örneğinden geliyor)
# end='//' Çıktı : 0//5//10//15//20//
# end='*' Çıktı : 0*5*10*15*20*

for x in range(0,25,5):
    print(x, end= ' ', flush = True) 















