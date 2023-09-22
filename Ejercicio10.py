# Definir la lista original
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Lista de valores a eliminar por posición
posiciones_a_eliminar = [0, 4, 5]

# Eliminar elementos en las posiciones especificadas
elementos_a_eliminar = [lista[posicion] for posicion in posiciones_a_eliminar]

for elemento in elementos_a_eliminar:
    lista.remove(elemento)

# Imprimir la lista resultante
print(lista)
