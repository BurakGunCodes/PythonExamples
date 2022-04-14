# 14.04.2022
# Burak GÜN 
# burak.gun@hotmail.com


#--------------------if else--------------------# 

from pickle import TRUE


var1 = 789
var2 = 36
var3: 99

# if else 
if var1 == var2 : 
    print(f'{var1} = {var2}')
else:
    print('eşit değiller')


#--------------------if elif--------------------# 

# if elif(else if) 
if var1 == var2 : 
    print(f'{var1} = {var2}')
elif var1 > var2:
    print(f'{var1} > {var2}')
elif var2 > var2:
    print(f'{var2} > {var1}')
else:
    print(' ... ')

 
#--------------------while loop--------------------# 


# while loop
words = ['bir', 'iki', 'üç', 'dört', 'beş']
n = 0
while( n < 5):
    print(words[n])
    n +=1



#--------------------for loop--------------------# 

words2 = ['bir', 'iki', 'üç', 'dört', 'beş']

# words dizisi içerisindeki değer kadar tekrar et
for i in words:
    print(i)

# default olarak sıfır(0) dan başlayıp range içerisindeki veriye kadar tekrar eder(döngü-loop)
# Çıktı : 0 1 2 ..9 (10 tekrar)
# 10 dahil değil
for x in range(10):
    print(x) 


# range içerisindeki değerler arasında tekrar eder. 
# Çıktı : 12 13 14 15  (4 tekrar)
# 16 dahil değil
for x in range(12,16):
    print(x) 


# range içerisindeki değerler arasında, aralık kadar artarak tekrar eder. 
# Çıktı : 0 5 10 15 20  (5 tekrar)
for x in range(0,25,5):
    print(x) 