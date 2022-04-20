# 20.04.2022
# Burak GÜN 
# burak.gun@hotmail.com


# Built-in methods that you can use on lists/arrays.

# Method	    Description
# --------------------------------------------------
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list



from inspect import stack
from tkinter import S


class Stack:

    # A constructor is a method with always has a name init
    # creates the class constructor. yapıcı metodu oluşturdu
    # sınıf oluşturulduğunda boş  bir dizi oluşturdu.
    def __init__(self):
        self.items = []
    #    print('Constructor Created')

    def is_empty(self):
        # return len(self.items) == 0 # aynı deperi döndürür
        return not self.items
    
    # add new value into the stack
    def push(self,item):
        self.items.append(item)
    
    # returns the last value in the stack and removes it
    def pop(self):
        return self.items.pop()

    # returns the last value in the stack
    def peek(self):
        return self.items[-1] # reaches to end of the list

    def size(self):
        return len(self.items)

    # print için geri dönüş belirleme.
    # eğer kullanılmazsa farklı türden değerler döner
    # verinin nasıl dönmesini istediğimi belirtiyoruz
    # __str__ function is called when print() and str() functions is used
    def __str__(self) :
        return str(self.items)

# eğer bu çalıştırılan  dosya ana(main) dosya ise, o zaman bu noktadan sonraki yeri çalıştır.
# örnek olarak bu StackClass.py dosyası farklı projede kullanılsaydı, import edilseydi, ve oradan erişilseydi
# çalıştırılan main dosya bu dosya olmayacağı için, bu satırdan sonraki kodlar çalıştırılmayacak.

if __name__ == "__main__": 

    # call the constructor. (__init__)
    s = Stack()

    print(s)
    print(s.is_empty())
    s.push(5)
    s.push(12)
    s.push(7)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s)
    print(s.size())









# Built-in methods that you can use on lists/arrays.

# Method	    Description
# --------------------------------------------------
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list