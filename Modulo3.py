#Actividad N°3
#Funcion que pide datos de usuario y contraseña, crea un diccionario simulando una BD . 
def creacionDeUsuario():
  user = input("ingrese su nuevo usuario:")
  password = input("ingrese sue nueva contraseña:")
  nuevoUsuario = {"Usuario" : user , "Contraseña" : password}
  return nuevoUsuario


#Funcion que muestra la informacion almacenada en la base de datos
def muestraDeInformacion() :
  print (f"la informacion almacenada es: {baseDeDatos}")


#Login de usuario
def ingresoDeUsuario():
  user = input("ingrese su usuario: ")
  password = input("ingrese su contraseña:")
  if user == baseDeDatos["Usuario"] and password==baseDeDatos["Contraseña"] :
          print("Usted a ingresado con exito")
          return
  print("Debe volver a ingresar sus datos")

#invocacion de las funciones
baseDeDatos = creacionDeUsuario()
muestraDeInformacion()
ingresoDeUsuario()