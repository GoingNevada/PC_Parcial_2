
# Autor: Santiago Camargo Molina

def main():
    lista1 = input("Ingrese una serie de elementos separados con espacio: ").split() # ingreso de cadena 1
    lista2 = input("Ingrese una serie de elementos separados con espacio: ").split() # ingreso de cadena 2
    n_list = [] # lista donde se almacenaran los elementos de 1 que no estan en 2
    for i in lista1:    # iteramos dentro de la lista 1
        if i not in lista2: # si el elemento no esta en la lista dos, entonces se agrega a la lista vacia
            n_list.append(i)
    if len(n_list)>0:   # si el tamaño final de la lista es >0, entonces se imprimen los elementos encontrados
        print(f"La lista dos, no contiene los elementos: {n_list}, de la lista uno")
    else:
        print("Las dos listas, contienen los mismo elementos")

if __name__=="__main__":
    main()