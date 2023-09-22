def eliminar_duplicados(lista_original):
    # Creamos un conjunto vacío para almacenar elementos únicos
    elementos_no_repetidos = set()
    
    # Creamos una lista para almacenar los elementos únicos en orden
    lista_procesada = []
    
    # Iteramos sobre la lista original
    for elemento in lista_original:
        if elemento not in elementos_no_repetidos:
            elementos_no_repetidos.add(elemento)
            lista_procesada.append(elemento)
    
    return lista_procesada

lista_inicial = [1, 1, 2, 3, 4, 4, 5, 1]

lista_procesada = eliminar_duplicados(lista_inicial)

# Imprimimos la lista procesada
print("Lista procesada:", lista_procesada)
