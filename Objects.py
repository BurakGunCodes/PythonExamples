# 14.04.2022
# Burak GÜN 
# burak.gun@hotmail.com

## In Python EVERYTHING is an OBJECT

# Class is Definition
# Object is Instance of a Class
# Nesne, class tan oluşturulan bir imaj gibi düşünebilir.

#Expression : 
#Statement : line of code


#nesnenin değişkenine yapılan referanslarda 'self' kullanılır.
#Buraya istediğin harfi yada kelimeyi yazabilirsin
# Örnek quack(self) veya quack(istedigin_kelimeyi_yaz)
class Duck: # class

    sound = 'böyle seslensin'
    yürü = 'böyle yürüsün'

    def quack(self): # metod 1, 
        print('quack')

    def walk(istedigin_kelimeyi_yaz): # metod 2
        print('walk')  

    def quack2(self): #metod 3
        print(self.sound) # kendi nesnesine referans verdi

    def walk2 (kelime): #metod 4
        print(kelime.yürü) # argüman ismi değişik olarak örnek verdim. argüman yerine istediğin şeyi yazabilirsin


def main():
    donald = Duck() # donald burada nesne'dir. nesne oluşturuldu.
    donald.quack() # nokta(.) dereference operatörü
    donald.walk()
    donald.walk2()


main()
