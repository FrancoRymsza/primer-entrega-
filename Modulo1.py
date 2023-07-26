# ACTIVIDAD N°1 "AÑO BISIESTO"

# Funcion que solicita el año
def solicitar_anio():
  while True:
    anio_ingresado = input("ingrese un año:")
    if anio_ingresado.isnumeric() == True:
      return anio_ingresado
    else :
      print ("Debe ingresar un año:")


# Funcion que ejecuta el valor retornado y devuelve el resultado.
def confirmacion_anio_bisiesto():
  anio = solicitar_anio()
  anio = int(anio)
  if (anio % 4 == 0) and (anio % 100 != 0):
      print (f"El año {anio} es bisiesto")
  elif (anio % 400 == 0):
      print(f"El año {anio} es bisiesto")
  else :
      print (f"El año {anio} no es bisiesto")

# Invocacion de la funcion
confirmacion_anio_bisiesto()