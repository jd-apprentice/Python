while True:
    print("----------------------------------------------------")
    print("Bienvenido a la Calculadora de Ganancia-Perdida")
    
    Cantidad = input("Por favor ingrese la cantidad de unidades: ")
    Cantidad1 = float(Cantidad)
    Compra = input("Por favor ingrese el valor de compra del Producto: ")
    Compra1 = float(Compra)
    Venta = input("Por favor ingrese el valor de venta del Producto: ")
    Venta1 = float(Venta)

    Ganancia = ((Venta1 - Compra1)*100) / Compra1
    Perdida = ((Compra1 - Venta1)* 100) / Compra1
    Perdida1 = (Compra1 * Cantidad1) - (Venta1 * Cantidad1)
    Ganancia1 = ((Cantidad1 / Compra1) * Venta1) - Cantidad1

    if Compra1 > Venta1:
        print("Su Calculo dio una Perdida de: -" +"{:.2f}".format(Perdida)+"%")
        print("Perdio un Total de: -"+str(Perdida1))
    else:
        print("Su Porcentaje de Ganancia es: " + "{:.2f}".format(Ganancia)+"%") 
        print("Gano un Total de: "+ "{:.2f}".format(Ganancia1))
    Respuesta = input("Desea hacer otro Calculo? S/N: ")
    if Respuesta == "N":
        break