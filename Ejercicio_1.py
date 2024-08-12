
# Autor: Santiago Camargo Molina

def main():
    lista = input("Ingrese una serie de elementos para la lista, separados por espacio: ").split()
    print(lista)
    for i in lista:
        if lista.count(i)>1:
            print(f"La lista contiene {lista.count(i)} veces el elemento '{i}'")
            return None
    print("La lista no contiene elementos repetidos")
    

if __name__=="__main__":
    main()