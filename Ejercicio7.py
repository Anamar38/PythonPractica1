#Ingreso de números
primer_numero = float(input("Ingrese el primer número: "))
segundo_numero = float(input("Ingrese el segundo número: "))
# Mostrar opciones
print("1. Suma de números")
print("2. Resta de números")
print("3. Multiplicación de números")
#Elegir opción
opcion_elegida = int(input("Elija una opción: "))
# Realizar operación
if opcion_elegida == 1:
    suma_numeros = primer_numero + segundo_numero
    print(f"La suma de los números ingresados es: {suma_numeros:.2f}")
elif opcion_elegida == 2:
    resta_numeros = primer_numero - segundo_numero
    print(f"La resta de los números ingresados es: {resta_numeros:.2f}")
elif opcion_elegida == 3:
    multiplicacion_numeros = primer_numero * segundo_numero
    print(f"La multiplicación de los números ingresados es: {multiplicacion_numeros:.2f}")
else :
    print("Opción invalida")
