def recursiva(numero):
    if numero==0:
        return 0
    else:
        return numero%10 +recursiva(numero//10)

def main():

    numero=int(input("Número: "))
    print("La suma de los digitos es: ",recursiva(numero))
main()