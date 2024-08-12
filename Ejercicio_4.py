
# Autor: Santiago Camargo Molina

def is_float(num):  # FUNCION PARA LA COMPROBACION DE CONVERSION DE UN NUMERO A REAL
    try:        # UTILIZAMOS UN TRY PARA INTENTAR REALIZAR LA CONVERSION
        float(num)  # EN CASO DE EXITO, LA FUNCION RETORNARA UN VALOR 'TRUE'
        return True
    except ValueError:     # EN CASO CONTRARIO, RETORNARA UN VALOR 'FALSE'
        return False
    
def is_floatarray(list): # FUNCION PARA LA COMPROBACION DE QUE UN ELEMENTO DENTRO DE LA LISTA SEA REAL
    for i in list:  # UTILIZAMOS UN CICLO FOR PARA ITERAR EN CADA ELEMENTO
        if is_float(i) != True:   # UTILIZAMOS LA FUNCION IS_FLOAT PARA COMPROBAR QUE SEA CONVERTIBLE A REAL
            return False    # SI ENCUENTRA UN CASO QUE NO SEA CONVERTIBLE, RETORNA FALSE
        else:
            pass
    return True # RETORNA TRUE SI NO ENCUENTRA ALGUN ELEMENTO DISTINTO A FLOAT

def mean(list): # FUNCION PARA CALCULAR EL PROMEDIO DE UNA LISTA
    sum = 0 # INICIALIZAMOS LA VARIABLE SUMA EN 0
    for i in list:  # ITERAMOS CON UN FOR DENTRO DE LA LISTA
        sum += i    # SUMAMOS CADA TERMINO
    return sum/len(list)    # RETORNAMOS LA SUMA DIVIDA LA CANTIDAD DE DATOS


def main():
    # INGRESO DE PRIMERA SECUENCIA DE NUMEROS
    v = input("Ingrese una serie de numeros, separados con 1 espacio: ").split()
    if not(v):  # SI NO EXISTE EL ARREGLO
        print("No se ingreso ninguna serie de numeros")
        return None
    elif is_floatarray(v) == False:   # SI EXISTE ALGUN ELEMENTO NO ENTERO
        print("La serie contiene elementos que no son numeros")
        return None
    else:
        v = [float(i) for i in v ]  # CONVERTIMOS LOS ELEMENTOS DE LA LISTA EN NUMEROS REALES

    print("El promedio ponderado de la lista es: ",mean(v))


if __name__ == '__main__':
    main()