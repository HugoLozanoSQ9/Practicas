#un programa que salude al usuario, y muestre el año de nacimiento 
print('Hola este programa sirve para solicitar el nombre, el apellido y la edad del usuario ')

name = input('¿Podrías darme tu nombre?' )
last_name = input('Podrías darme tu apellido?')
age = int(input('Podrías ahora darme tu edad?'))
year = 2023
bornIn = str(year - age)
print('Hola', name, last_name, 'tienes', age, 'y naciste en el ', bornIn)

