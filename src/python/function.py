################################################################################
#                                 IMPORT                                       #     
################################################################################
import json
################################################################################
#                                 FUNCIONES                                    #     
################################################################################
def imprimirSeparadorHorizontal():
    print('========================================')

def mostrarMenu():
    imprimirSeparadorHorizontal()
    print('''
        1 - Ver listado de series
        2 - Añadir una serie nueva
        3 - Modificar una serie
        4 - Eliminar una serie
        5 - Ficha serie
        6 - Añadir un campo a la serie
        9 - Salir
          ''')
    imprimirSeparadorHorizontal()
    
def abrirFichero(fichero):
    lista= []
    with open (fichero, "r") as f:
        for registro in f:
            lista.append(json.loads(registro))
    return (lista)

def guardarFichero(fichero, lista):
    with open(fichero, "w+") as f:
        for registro in lista:
            f.write(json.dumps(registro))
            f.write("\n")

def pedirValor(mensaje):
    valor = int(input(mensaje))
    return(valor)

def listarSeries(listaSeries, campo, valor):
    listaOrdenada = []
    listaClaves = list(listaSeries[0].keys())
    numeroCampos = len(listaSeries[0].keys())
    print()
    anchuraPrimerCampo = 20
    anchuraRestoCampos = 15
    contador = 0
    for campo in listaClaves:
        if campo != "Sinopsis":
            if contador == 0:
                print("  | " + campo[:anchuraPrimerCampo].upper().center(anchuraPrimerCampo), end=" | ")
            else:
                print(campo[:anchuraRestoCampos].upper().center(anchuraRestoCampos), end=" | ")
            contador += 1
    longitud = anchuraPrimerCampo + anchuraRestoCampos * contador
    print()
    print("-".center(longitud, "-"))
    for registro in listaSeries:
        if registro[campo] == valor or valor == "":
            contador = 0
            registroCompleto = ""
            for clave in listaClaves:
                if clave != "Sinopsis":
                    if contador == 0:
                        registroCompleto += " | "+ registro[clave][:anchuraPrimerCampo].ljust(anchuraPrimerCampo) + " | "
                    elif contador <= numeroCampos:
                        registroCompleto += registro[clave][:anchuraRestoCampos].ljust(anchuraRestoCampos) + " | "
                    contador += 1
            listaOrdenada.append(registroCompleto)
    listaOrdenada.sort()
    numeroSerie = 1
    for registro in listaOrdenada:
        print(str(numeroSerie) + registro)
        numeroSerie += 1

def mostrarValores(lista, campo):
    listaOrdenada = []
    for registro in lista:
        if registro[campo] not in listaOrdenada:
            listaOrdenada.append(registro[campo])
    listaOrdenada.sort()
    numeroSerie = 1
    for registro in listaOrdenada:
        print(str(numeroSerie) + " - " + registro)
        numeroSerie += 1
    return(listaOrdenada)

def buscarRegistro(lista, campo, valor):
    registro = -1
    contador = 0
    for elemento in lista:
        if elemento[campo] == valor:
            registro = contador
        contador += 1
    return (registro)

def addSerie(lista):
    tipos = list(lista[0].keys())
    serie = {}
    longitud = len(tipos)
    contador = 0
    existe = False
    while contador < longitud and existe == False:
        serie[tipos[contador]] = input(f"Introduce un {tipos[contador]}, por favor: ")
        if tipos[contador] == "Titulo":
            registro = buscarRegistro(lista, "Titulo", serie[tipos[contador]])
            if registro != -1:
                print("Esa serie ya la tienes añadida")
                existe = True
        contador += 1
    if existe == False:
        lista.append(serie)
    return (lista)

def editSerie(lista, serieToEdit):
    tipos = list(lista[0].keys())
    longitud = len(tipos)
    contador = 0
    while contador < longitud:
        nuevoElemento = input(f"Inserta el nuevo {tipos[contador]} de la serie (Intro para mantener el valor): ")
        if nuevoElemento != "":
            lista[serieToEdit-1][tipos[contador]] = nuevoElemento
        contador += 1
    return (lista)

def delSerie(lista, campo, serieToDel):
    registro = buscarRegistro(lista, campo, serieToDel)
    del lista[registro]
    return (lista)

def recorrerTipos(lista):
    tipos = list(lista[0].keys())
    contador = 1
    for i in tipos:
        print (str(contador) + " - " + i)
        contador += 1

def fichaSeries(lista, valor):
    registro = buscarRegistro(lista, "Titulo", valor)
    tipos = list(lista[0].keys())
    contador = 1
    for i in tipos:
        print (str(contador) + " - " + (i.upper()) + ": " + lista[registro][i])
        contador += 1

def addCampo(lista, campo, valor):
    longitudLista = len(lista)
    contador = 0
    while contador < longitudLista:
        lista[contador][campo] = valor
        contador += 1
    return (lista)