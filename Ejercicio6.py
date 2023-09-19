# Solicitar al usuario su edad
edad_del_cliente = int(input("Ingrese su edad: "))
# Mostrar el costo de su entrada
if edad_del_cliente < 4:
    print("Usted puede entrar gratis")
elif edad_del_cliente <= 18:
    print("Usted debe pagar $5 por entrada")
else :
    print("Usted debe pagar $10 por entrada")
