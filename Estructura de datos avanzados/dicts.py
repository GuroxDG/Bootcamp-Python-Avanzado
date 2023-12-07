'''
Dicts
'''

dict_a = {'name' : 'Camila',
          'last_name' : 'Gomez',
          'age' : 27}

print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

# Los diccionarios no son ordenados
print({'last_name' : 'Gomez', 'name' : 'Camila'}
       == {'name' : 'Camila', 'last_name' : 'Gomez'}) # True

# Los diccionarios solo reciben keys inmutables
# Si repito la key el diccionario toma el último valor
# En los dict comprehensions debe pasarse tanto el key como el valor

squares = {i: i*i for i in range(10) }
print(squares)

