def leerarchivo(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    contenido=[]
    for linea in archivo:
        contenido.append(linea)
        #print(linea, end="")
        listalinea=linea.split()
    archivo.close()
    return contenido

def grabarArchivo(nombreArchivo,palabra):
    archivo = open(nombreArchivo, "a")
    archivo.write(palabra)
    archivo.close()
def main():
    diccionario={}
    archivoEntrada="texto.txt"
    archivoSalida="reporte.txt"
    contenido=leerarchivo(archivoEntrada)
    for palabra in contenido:
        print(palabra)
        listaPalabra=palabra.split()
        for frase in listaPalabra:
            if frase.upper() not in diccionario:
                diccionario[frase.upper()] = 1
            else:
                diccionario[frase.upper()] = diccionario[frase.upper()]+1
    keys=list(diccionario.keys())
    valores=list(diccionario.values())
    for x in range(len(keys)):
        palabra=str(keys[x])+" "+str(valores[x])+"\n"
        grabarArchivo(archivoSalida,palabra)
main()