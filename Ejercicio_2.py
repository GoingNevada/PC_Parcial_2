
# Autor: Santiago Camargo Molina

def main():
    lista = input("Ingrese una serie de cadenas de caracteres separadas por espacio: ").split()
    vocales = ['a','e','i','o','u']
    print(lista)
    for i in lista:
        count = 0
        for j in vocales:
            if j in i:
                count +=1
        if count > 1:    
            print(f"La cadena '{i}' contiene mas de una vocal")
            return None
    print("No existe ninguna cadena dentro de la lista, con mas de una vocal")
    

if __name__=="__main__":
    main()