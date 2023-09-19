# Solicitar al usuario el costo de la comida
consumo_usuario_restaurant = float(input("Digite el valor de su consumo en el restaurant: $"))
# Solicitar al usuario el porcentaje de propina deseado
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))
# Calculo de propina
total_propina = consumo_usuario_restaurant*porcentaje_propina/100 
# Mostrar la cantidad de propina
print(f"Deje ${total_propina:.2f} como propina. \nTotal a pagar: ${consumo_usuario_restaurant + total_propina:.2f}")
