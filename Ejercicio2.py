consumo_usuario_restaurant = float(input("Digite el valor de su consumo en el restaurant: "))
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar?: "))

# Calculo de propina
total_propina = consumo_usuario_restaurant*porcentaje_propina/100 
# Mostrar el total de propina
print(f"Propina a dejar: S/. {total_propina}")