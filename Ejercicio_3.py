
# Autor: Santiago Camargo Molina

def main():
    lista1 = input("Ingrese una serie de elementos separados con espacio: ").split()
    lista2 = input("Ingrese una serie de elementos separados con espacio: ").split()
    n_list = []
    for i in lista1:
        if i not in lista2:
            n_list.append(i)
    if len(n_list)>0:
        print(f"La lista dos, no contiene los elementos: {n_list}, de la lista uno")
    else:
        print("Las dos listas, contienen los mismo elementos")

if __name__=="__main__":
    main()