nombre = str (input("Por favor introduce tu nombre ") )
print (nombre.isalpha() )

aPaterno= str (input ("Por favor introduce apellido paterno ")) 
print (aPaterno.isalpha())

aMaterno = str (input ("Por favor introduce apellido materno "))
print (aMaterno.isalpha())
 
peso = float (input ("Por favor introduce tu peso ")) 

estatura = float (input ("Por favor introduce tu estatura "))
indice = peso / estatura ** 2
print (f"Su indice de masa corporal es de: {indice}")
