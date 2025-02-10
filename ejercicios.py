#control de flujo
'''
print("Introduce los dos numeros que quieras sumar/restar/multiplicar")
numero_uno=float(input("Introduce el primer numero: "))
numero_dos=float(input("Introduce el segundo numero: "))

print("Introduce la operacion que deseas realizar con estos dos numeros")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
opcion_menu=int(input("Introduce la opcion que desees: "))

if opcion_menu<1:
    print("Numero no valido")
elif opcion_menu==1:
    resultado=(numero_uno+numero_dos)
    print(f"{numero_uno} mas {numero_dos}")
    print(f"El resultado es: {resultado}")
elif opcion_menu==2:
    resultado=(numero_uno-numero_dos)
    print(f"{numero_uno} menos {numero_dos}")
    print(f"El resultado es: {resultado}")
elif opcion_menu==3:
    resultado=(numero_uno*numero_dos)
    print(f"{numero_uno} multiplicado por {numero_dos}")
    print(f"El resultado es: {resultado}")
else:
    print("Numero no valido")
'''

'''
print("Introduce un numero impar, de lo contrario el programa se reiniciará y se le pedira de nuevo introducir un numero impar")

es_impar=False

while es_impar==False:
    numero=int(input("Introduce un numero impar: "))
    if numero%2==0:
        es_impar=False
    else:
        es_impar=True
'''

'''
print("Programa que suma todos los números enteros pares desde el 0 hasta el 100")

suma=sum(range(0,101,2))
print(f"El resultado es: {suma}")
'''


'''
print("Programa que pide al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética")

cantidad_numeros=int(input("Introduce la cantidad de numeros que desees: "))

suma=0

for i in range(cantidad_numeros):
    numero = float(input(f"Introduce el número {i+1}: "))
    suma=numero+suma

media= suma/cantidad_numeros

print(f"La media es: {media}")
'''

'''
print("Introduce un numero entero del 0 al 9, si se introduce un numero no valido el programa se reiniciara y volvera a pedir el numero. Se comprobara que este numero este en la lista de numeros validos y se notificara")

es_del_uno_al_nueve=False
numeros_validos=[0,1,2,3,4,5,6,7,8,9]

while es_del_uno_al_nueve==False:
    numero=float(input("Introduce un numero entero del 1 al 9: "))
    if numero>9 or numero<0:
        print("El numero no es valido")
    elif numero in numeros_validos:
        es_del_uno_al_nueve=True
        print("El numero es valido")
    else:
        es_del_uno_al_nueve=False
        print("El numero no es valido")
'''


'''
numeros_del_0_al_10=(list(range(0,11)))
print(numeros_del_0_al_10)

numeros_del_menos_10_al_0=(list(range(-10,1)))
print(numeros_del_menos_10_al_0)

numeros_pares_del_0_al_20=(list(range(0,21,2)))
print(numeros_pares_del_0_al_20)

numeros_impares_del_menos_20_al_0=(list(range(-19,0,2)))
print(numeros_impares_del_menos_20_al_0)

numeros_multiplos_de_5_del_0_al_50=(list(range(0,51,5)))
print(numeros_multiplos_de_5_del_0_al_50)
'''

'''
lista1=[1,1,1,2,3,4,4,5,5]
lista2=[6,8,5,6,7,9,1]
lista3=list(set(lista1)&set(lista2))
print(lista3)
'''

#operadores

'''
print("Programa que pide dos numeros y dice si es cierto lo siguiente:")

print("1.Si los dos números son iguales")
print("2.Si los dos números son diferentes")
print("3.Si el primero es mayor que el segundo")
print("4.Si el segundo es mayor o igual que el primero")

numero_uno=float(input("Introduce el primer numero: "))
numero_dos=float(input("Introduce el segundo: "))

resultado_uno= (numero_uno==numero_dos)
print(f"El resultado 1 es: {resultado_uno}") 

resultado_dos= (numero_uno!=numero_dos)
print(f"El resultado 2 es: {resultado_dos}")

resultado_tres= (numero_uno>numero_dos)
print(f"El resultado 3 es: {resultado_tres}")

resultado_cuatro= (numero_dos>=numero_uno)
print(f"El resultado 4 es: {resultado_cuatro}")
'''



"""
print("Programa que te dice si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10")

texto=input("Introduce una frase: ")

comprobacion=len(texto)>=3 and len(texto)<10

print(f"Resultado: {comprobacion}")
"""


""" 
numero_magico= 12345679
numero_usuario=int(input("Introduce un numero del 1 al 9: "))

numero_usuario*=9
numero_magico*=numero_usuario

print(numero_magico)
 """


#funciones

""" 
def area_rectangulo(x, y):
    return x*y

x=15
y=10

resultado=area_rectangulo(x, y)

print(f"El area del rectangulo es: {resultado}")
 """

""" 
import math

def area_circulo(radio):
    return math.pi * (radio * radio)

radio = 5
area = area_circulo(radio)
print(f"El área del círculo es: {area}")
 """



""" 
def relacion(numero_1, numero_2):
    if numero_1>numero_2:
        return 1
    elif numero_1<numero_2:
        return -1
    else:
        return 0

print(f"Resultado de 5 y 10: {relacion(5,10)}")
print(f"Resultado de 10 y 5: {relacion(10,5)}")
print(f"Resultado de 5 y 5: {relacion(5,5)}")
"""



""" 
def intermedio(numero_1,numero_2):
    return (numero_1+numero_2)/2

numero_1=(-12)
numero_2=24
media=intermedio(numero_1,numero_2)

print(f"Numero intermedio: {media}") 
"""




""" 
def recortar(numero,limite_inferior,limite_superior):
    if numero<limite_inferior:
        return limite_inferior
    elif numero>limite_superior:
        return limite_superior
    else:
        return numero


numero=15
limite_inferior=0
limite_superior=10

resultado=recortar(numero,limite_inferior,limite_superior)

print(f"Resultado: {resultado}")
"""


numeros = [-12, 84, 13, 20, -33, 101, 9]
pares=[]
impares=[]
numeros.sort()

def separar(lista):
    for x in range(len(lista)):
        if lista[x]%2==0:
            pares.append(lista[x])
        else:
            impares.append(lista[x])
    return pares,impares

pares, impares= separar(numeros)

print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")