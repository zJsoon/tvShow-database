################################################################################
#                             IMPORT FUNCTIONS                                 #     
################################################################################
from function import mostrarMenu
from function import abrirFichero
from function import listarSeries
from function import addSerie
from function import guardarFichero
from function import pedirValor
from function import editSerie
from function import mostrarValores
from function import delSerie
from function import recorrerTipos
from function import fichaSeries
from function import addCampo
################################################################################
#                                 PRINCIPAL                                    #     
################################################################################
fichero = "src\databases.txt"
listaSeries = abrirFichero(fichero)
continuar = True
while continuar == True:
    mostrarMenu()
    opcionEscogida = int(input("Escoge una opción del menú: "))
    if opcionEscogida == 1: ###################################### LISTAR SERIES ######################################
        listarSeries(listaSeries, "Titulo", "")
    elif opcionEscogida == 2: ###################################### AÑADIR SERIES ######################################
        listaSeries = addSerie(listaSeries)
        guardarFichero(fichero, listaSeries)
    elif opcionEscogida == 3: ###################################### EDITAR SERIES ######################################
        listarSeries(listaSeries, "Titulo", "")
        serieToEdit = pedirValor("¿Qué serie quieres editar?: ")
        lista = editSerie(listaSeries, serieToEdit)
        guardarFichero(fichero, lista)
    elif opcionEscogida == 4: ###################################### ELIMINAR SERIES ######################################
        valores = mostrarValores(listaSeries, "Titulo")
        serieToDel = pedirValor("¿Qué serie quieres eliminar?: ")
        lista = delSerie(listaSeries, "Titulo", valores[serieToDel-1])
        guardarFichero(fichero, lista)
    elif opcionEscogida == 5: ###################################### FICHA DE SERIES ######################################
        tipos = list(listaSeries[0].keys())
        valoresMostrados = mostrarValores(listaSeries, "Titulo")
        valor = pedirValor(f"¿Por qué Titulo quieres fichar?: ")
        fichaSeries(listaSeries, valoresMostrados[valor-1])
    elif opcionEscogida == 6: ###################################### AÑADIR UN CAMPO ######################################
        campo = input(f"¿Qué campo quieres añadir?: ")
        valor = input(f"¿Qué {campo} quieres añadir?: ")
        lista = addCampo(listaSeries, campo, valor)
        guardarFichero(fichero, lista)
    elif opcionEscogida == 9: ###################################### SALIR ######################################
        continuar = False
        print("Ya has terminado, que tengas un buen día")
    else:
        print("Escoge una opción válida")
