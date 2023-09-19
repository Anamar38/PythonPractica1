# Solicitar al usuario la cantidad de shows musicales vistos
shows_vistos = int(input("Ingrese la cantidad de shows musicales que ha visto en el último año: "))
# Comprobar si ha visto más de 3 shows
ha_visto_mas_de_3 = shows_vistos > 3
# Mostrar el valor booleano en pantalla
print(f"¿Ha visto más de 3 shows? {ha_visto_mas_de_3}")
