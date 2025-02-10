#condicionales
if True:
    print("Hola")
    print("otra linea")

a=5
if a==2:
    print("a es igual a dos")
if a==5:
    print("a es igual a cinco")

n=11
if (n%2==0):
    print("El numero es par")
else:
    print("El numero es impar")

#elif

nota=float(input("Introduce una nota: "))
if nota>=9:
    print("Sobresaliente")
elif nota>=7:
    print("Notable")
elif nota>=6:
    print("Bien")
elif nota>=5:
    print("suficiente")
else:
    print("insuficiente")


c=0
while c<=6:
    c+=1
    print("c vale: ",c)

for i in range(1,11):
    print(f"Tabla del {i}:")
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")

tabla=int(input("Introduce el numero del que quieres saber su tabla de multiplicar: "))

for i in range (1,11):
    print(f"{tabla}*{i}={tabla*i}")

#funciones

def saludo():
    print("Hola como estas")
saludo()

def sumar(a,b):
    return a+b
resultado=sumar(3,4)
print("La suma es: ",resultado)

a=4
a%2==0

def es_par(num):
    return num%2==0
print(es_par(4))

print(es_par(5))