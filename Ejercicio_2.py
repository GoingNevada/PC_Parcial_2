
# Autor: Santiago Camargo Molina

def main():
    lista = input("Ingrese una serie de cadenas de caracteres separadas por espacio: ").split() # ingreso de las cadenas de caracteres
    vocales = ['a','e','i','o','u'] # lista que contiene las vocales
    print(lista)    # se imprime la lista
    for i in lista: # iteramos dentro de la lista
        count = 0   # contador de veces que se ha encontrado una vocal
        for j in vocales:   # iterador para vocales
            if j in i:  # si la vocal esta en la cadena, se suma 1 al contador
                count +=1
        if count > 1:    # si el contador termina siendo mayor a 1, entonces se envia mensaje
            print(f"La cadena '{i}' contiene mas de una vocal")
            return None
    print("No existe ninguna cadena dentro de la lista, con mas de una vocal")
    

if __name__=="__main__":
    main()