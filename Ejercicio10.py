# Definir la lista original
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Eliminar elementos en las posiciones 0, 4 y 5
lista.remove(lista[0]) 
lista.remove(lista[4])
lista.remove(lista[5])

# Imprimir la lista resultante
print(lista)
# Definir la lista original
mi_lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Lista de valores a eliminar por posición
posiciones_a_eliminar = [0, 4, 5]

# Eliminar elementos en las posiciones especificadas
elementos_a_eliminar = [mi_lista[posicion] for posicion in posiciones_a_eliminar]

for elemento in elementos_a_eliminar:
    mi_lista.remove(elemento)

# Imprimir la lista resultante
print(mi_lista)
