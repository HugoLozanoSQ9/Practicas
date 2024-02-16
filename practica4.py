#Escribir un escript que solicite un número "n" y que calcule el valor de n + nn + nnn y una cantidad m de veces

n = float(input('Hola podrías indicarme por favor tu numero deseado?'))
m = int(input('indica tu número de veces que se va a repetir'))
sumaTotal = 0
for i in range (1,m+1):
    suma=(n**i)
    #print(suma)
    sumaTotal = sumaTotal + suma
print('El total de tu operación es: ', sumaTotal)