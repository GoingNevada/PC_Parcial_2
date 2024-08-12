
# Autor: Santiago Camargo Molina

def is_int(num):  # FUNCION PARA LA COMPROBACION DE CONVERSION DE UN NUMERO A ENTERO
    try:        # UTILIZAMOS UN TRY PARA INTENTAR REALIZAR LA CONVERSION
        int(num)  # EN CASO DE EXITO, LA FUNCION RETORNARA UN VALOR 'TRUE'
        return True
    except ValueError:     # EN CASO CONTRARIO, RETORNARA UN VALOR 'FALSE'
        return False
    
def is_intarray(list): # FUNCION PARA LA COMPROBACION DE QUE UN ELEMENTO DENTRO DE LA LISTA SEA ENTERO
    for i in list:  # UTILIZAMOS UN CICLO FOR PARA ITERAR EN CADA ELEMENTO
        if is_int(i) != True:   # UTILIZAMOS LA FUNCION IS_INT PARA COMPROBAR QUE SEA CONVERTIBLE A ENTERO
            return False    # SI ENCUENTRA UN CASO QUE NO SEA CONVERTIBLE, RETORNA FALSE
    return True # RETORNA TRUE SI NO ENCUENTRA ALGUN ELEMENTO DISTINTO A ENTERO


def median(lista): # FUNCION PARA CALCULAR LA MEDIANA DE UNA LISTA
    lista.sort()    # UTILIZAMOS EL METODO SORT PARA ORDENAR DE MENOR A MAYOR LA LISTA
    print(lista)
    if (len(lista) % 2) == 0:   # PREGUNTAMOS SI EL TAMAÑO ES PAR
        ind = round(len(lista)/2)   # OBTENEMOS EL INDICE DE LOS 2 NUMEROS CENTRALES
        return (lista[ind-1] + lista[ind])/2    # RETORNAMOS LA MEDIANA CALCULADA
    else:
        ind = round((len(lista)+1)/2)-1     # OBTENEMOS EL INDICE DEL NUMERO CENTRAL
        return lista[ind]   # RETORNAMOS LA MEDIANA CALCULADA

def main():
    # INGRESO DE PRIMERA SECUENCIA DE NUMEROS
    v = input("Ingrese una serie de numeros enteros, separados con 1 espacio: ").split()
    if not(v):  # SI NO EXISTE EL ARREGLO
        print("No se ingreso ninguna serie de numeros")
        return None
    elif is_intarray(v) == False:   # SI EXISTE ALGUN ELEMENTO NO ENTERO
        print("La serie contiene elementos que no son numeros")
        return None
    else:
        v = [int(i) for i in v ]  # CONVERTIMOS LOS ELEMENTOS DE LA LISTA EN NUMEROS ENTEROS
    
    print("La mediana de la lista es: ", median(v))

if __name__ == '__main__':
    main()