# 17.04.2022
# Burak GÜN 
# burak.gun@hotmail.com


# id() function returns identity (unique integer) of an object.
# Ancak her farklı nesne için farklı numarak döndürür.

# Aşağıda görüleceği üzere, 5 için hep aynı numara döndürürken, 5.0 için farklı değer döndürür çünkü farklı değerdir

print('id of 5 =',id(5))

a = 5
print('id of a =',id(a))

b = a
print('id of b =',id(b))

c = 5.0
print('id of c =',id(c))

# id of 5 = 140472391630016
# id of a = 140472391630016
# id of b = 140472391630016
# id of c = 140472372786520





#type() method returns class type of the argument(object) passed as parameter.
# isinstance(x, list/tuple/..)
