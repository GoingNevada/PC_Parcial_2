
# Autor: Santiago Camargo Molina

def main():
    lista = input("Ingrese una serie de elementos para la lista, separados por espacio: ").split() # Ingreso de datos separados para genera lista
    print(lista)    # se imprime la lista
    for i in lista: # iteramos dentro de los elementos de la lista
        if lista.count(i)>1:    # si el elemento, aparece mas de 1 vez
            print(f"La lista contiene {lista.count(i)} veces el elemento '{i}'")    # se imprime la cantidad y elemento encontrado
            return None
    print("La lista no contiene elementos repetidos")
    

if __name__=="__main__":
    main()