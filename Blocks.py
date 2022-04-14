# 14.04.2022
# Burak GÜN 
# burak.gun@hotmail.com



var1 = 45
var2 = 7

#block yapısı
#eğer print metodları sol tarafdan aynı karakter uzunluğunda olmazsa hata verir --> IndentationError: unindent does not match any outer indentation level
if var1 > var2 :
        #print(..) burada yazsaydım yukarıdaki hatayı verecekti.
    print(f'{var1} > {var2} ')
    print('hala block içerisinde  ')

else:
    print(f'{var1} < {var2}')