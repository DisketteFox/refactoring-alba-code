nombresProductos=["Agua 💧", "Refresco🥤", "Zumo🍹"]
preciosProductos=[0.50, 0.75, 0.95]
reservaMonedas=[20,20,20,20,20,20]
valoresMonedas=[2,1,0.5,0.20,0.10,0.05]
continuar=True
def menu(nombres, precios):
    cont=0
    textoMenu=""
    for nombre in nombres:
        textoMenu += f"{cont+1} - {nombre} - {precios[cont]} \n"
        cont +=1
    textoMenu += f"{cont +1} - SALIR"
    print(textoMenu)
def ingresarOpcion():
    opcion=input("Introduzca la opción: ")
    while opcion not in ["1", "2", "3", "4"]:
        opcion = input("Introduzca la opción correcta: ")
    return int(opcion)-1
def ingresarImporte(opcion):
    precio=preciosProductos[opcion]
    importeUsuario=0
    monedasIntroducidas=[]
    while importeUsuario<precio:
        print(f"Le queda {round(precio-importeUsuario, 2)} por ingresar")
        moneda=ingresarMoneda()
        importeUsuario+=moneda
        monedasIntroducidas.append(moneda)
    if importeUsuario >precio:
        resto=importeUsuario-precio
        darCambio(resto)
    entregarProducto(nombresProductos[opcion])
    sumarMonedas(monedasIntroducidas)
def sumarMonedas(monedas):
    for moneda in monedas:
        reservaMonedas[valoresMonedas.index(moneda)]+=1

def devolverMonedas(monedas):
    for moneda in monedas:
        reservaMonedas[valoresMonedas.index(moneda)] -= 1
def entregarProducto(producto):
    print(f"Aquí tiene su {producto}")
def ingresarMoneda():
    valoresValidos=[]
    for valor in valoresMonedas:
        valoresValidos.append(valor)
    valorIntroducido=float(input("Introduzca monedas de 2€, 1€, 0.50 cents, 0.20 cents, 0.10 cents o 0.05 cents: "))
    while valorIntroducido not in valoresValidos:
        valorIntroducido=float(input("Introduzca una moneda válida: "))
    return float(valorIntroducido)
def darCambio(resto):
    vueltas=0
    monedasDevueltas=[]
    while vueltas<resto:
        for valor in valoresMonedas:
            if valor<=round(resto,2):
                monedasDevueltas.append(valor)
                vueltas+=valor
                resto-=valor
    devolverMonedas(monedasDevueltas)
    print(f"Tus vueltas son estas: {monedasDevueltas}")
while continuar:
    menu(nombresProductos, preciosProductos)
    opcion=ingresarOpcion()
    if opcion>=len(nombresProductos):
        print("Gracias por usar nuestros servicios")
        continuar=False
    else:
         ingresarImporte(opcion)