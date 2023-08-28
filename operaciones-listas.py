import numpy as np
# Solicitamos al usuario que ingrese los valores para dos listas
lista1=(input("ingresa los valores para la lista:"))
lista2=(input("ingresa los valores para la lista:"))

# Convertimos las listas de cadenas de texto a enteros utilizando NumPy
complis=np.array([int(lis) for lis in lista1])
comps=np.array([int(los) for los in lista2])

# Solicitamos al usuario que ingrese una operación aritmética
operacion=input("que operacion quiere hacer:")

# Realizamos la operación deseada en las dos listas
if operacion=="+":
    resul=complis+comps
# podria ponerle mas condiciones para realizar mas operaciones aritmeticas pero lo deje hay

# Imprimimos el resultado de la operación
print(resul)