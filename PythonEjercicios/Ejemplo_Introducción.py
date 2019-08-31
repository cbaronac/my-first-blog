def ingresarInfo(nombre,apellido,edad):
	persona = [nombre,apellido,edad]
	print("Información de la persona: ")
	print(persona)


nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=int(input("Ingrese su edad: "))
ingresarInfo(nombre,apellido,edad)