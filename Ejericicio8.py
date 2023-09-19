# Solicitar al usuario una hora en formato de 24 horas
hora_comidas = input("Ingrese una hora en formato hh:mm: ")

# Dividir la hora en horas y minutos
hora, minutos = map(int, hora_comidas.split(":"))

# Verificar si es hora de desayunar, almorzar o cenar
if 7 <= hora < 8:
    print("Es hora de desayunar.")
elif 12 <= hora < 13:
    print("Es hora de almorzar.")
elif 18 <= hora < 19:
    print("Es hora de cenar.")
