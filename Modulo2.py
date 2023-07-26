#Actividad N°2
# ejercicio 1

def area_rectangulo (base,altura):  #Funcion que pide como parametro, base y altura
  return base * altura              # return de la funcion

base = int(input("ingrese la base del rectangulo:"))     # input solicitando los datos
altura = int(input("ingrese la altura del rectangulo:"))

print (f"el area del rectangulo es {area_rectangulo(base,altura)}")



#Actividad N°2
## Ejercicio 2

def area_circulo(radio):          #Funcion que calcula el area de un circulo
  return (radio**2) * 3.14159

radio = 5                         # valor del radio

print (f"el area del circulo es {area_circulo(radio)}")


#Actividad N°2
# Ejercicio 3

def relacion(a,b):   # funcion que dependiendo la relacion entre a y b, retorna un valor distinto
  if a > b:
    return 1
  elif a < b:
    return -1
  else:
    return 0

a = int(input("ingrese el primer numero:"))     #input para agregarle argumentos a la funcion
b = int(input("ingrese el segundo numero:"))

print(f"el resultado de la funcion es {relacion(a,b)}")



#Actividad N°2
# Ejercicio 4

def intermedio(a,b):    #Funcion que encuentra el intermedio entre dos numeros.
  return (a + b) / 2

a = int(input("ingrese el numero 'a':"))   # input para agregarle argumentos a la funcion
b = int(input("ingrese el numero 'b':"))

print (f"el intermedio de 'a' y 'b' es: {intermedio(a,b)}")


#Actividad N°2
# Ejercicio 5

def recortar(a,b,c):
  if a < b :
    return b
  elif a > c :
    return c
  else :
    return a

a = int(input("ingrese numero 'a':"))
b = int(input("ingrese numero 'b':"))
c = int(input("ingrese numero 'c':"))

print(recortar(a,b,c))

#Actividad N°2
# EJERCICIO 6

#Declarando la variable lista_principal
lista_principal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
list1 = [] # Declarando listas vacias
list2 = []
def separar(lista_principal):    #Funcion que toma una lista como argumento y devuelve dos listas
  for n in lista_principal:      #Una lista con numero pares ordenados
    if n % 2 == 0 :              #Y otra con numero impares ordenados
      list1.append(n)

    elif n % 2 != 0 :
      list2.append(n)

  print (list1 , list2)


separar(lista_principal)