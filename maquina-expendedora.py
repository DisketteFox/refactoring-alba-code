nombresProductos=["Agua 💧", "Refresco🥤", "Zumo🍹"]

preciosProductos=[0.50, 0.75, 0.95]
reservaMonedas=[20,20,20,20,20,20]
valoresMonedas=[2,1,0.5,0.20,0.10,0.05]

continuar=True
dinero = 0.0

def menu(nombres, precios, dinero):
    cont=0
    textoMenu=""

    for nombre in nombres:
        textoMenu += f"{cont+1} - {nombre} - {precios[cont]} \n"
        cont +=1
    textoMenu += f"{cont +1} - Introducir dinero \n"
    textoMenu += f"{cont +2} - Salir\n"
    textoMenu += f"Dinero: {dinero}€"

    print(textoMenu)
    opcion=input(">> ")

    return int(opcion)-1
    
def ingresarMoneda(dinero, reservaMonedas, valoresMonedas):
    valoresValidos = [2, 1, 0.50, 0.20, 0.10, 0.5]
    num = 0

    while num != -1:
        print("Introduzca monedas de 2€, 1€, 0.50€, 0.20€, 0.10€ o 0.05€ ")
        print("-1 para salir")
        print(f"Dinero: {dinero}€")
        num = float(input(">> "))
        if num != -1 and num in valoresValidos:
            dinero += num
            for i in range(len(reservaMonedas)):
                if valoresMonedas[i] == num:
                    reservaMonedas[i] += 1

    return float(dinero)

def darCambio(resto, reservaMonedas, valoresMonedas):
    vueltas = 0
    monedasDevueltas = []

    while vueltas<resto:
        for valor in valoresMonedas:
            if valor <= round(resto,2):
                monedasDevueltas.append(valor)
                vueltas+=valor
                resto-=valor
                for i in range(len(reservaMonedas)):
                    if valoresMonedas[i] == valor:
                        reservaMonedas[i] -= 1
    print(f"Tus vueltas son estas: {monedasDevueltas}")

while continuar:
    opcion = menu(nombresProductos, preciosProductos, dinero)
    if opcion > 3 or opcion < 0:
        continuar = False
    elif opcion == 3:
        dinero += ingresarMoneda(dinero, reservaMonedas, valoresMonedas)
    elif dinero >= preciosProductos[opcion]:
        darCambio(dinero-preciosProductos[opcion], reservaMonedas, valoresMonedas)
        print(f"Aquí tienes tu {nombresProductos[opcion]}")
    else:
        print("Dinero insuficiente")

print("Gracias por usar nuestros servicios")
print(reservaMonedas)