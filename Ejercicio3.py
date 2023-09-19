# Solicitar al usuario el número de payasos vendidos
payasos_vendidos = int(input("Ingrese la cantidad de payasos vendidos: "))
# Solicitar al usuario el número de muñecas vendidas
muñecas_vendidas = int(input("Ingrese la cantidad de muñecas vendidas: "))
# Calculo del peso
peso_total_jueguetes = (payasos_vendidos*112)+(muñecas_vendidas*75)
# Mostrar la cantidad de jueguetes 
print(f"En el último pedido se vendieron {payasos_vendidos} payasos y {muñecas_vendidas} muñecas.")
print(f"El peso total del paquete a enviar será de {peso_total_jueguetes} g.")