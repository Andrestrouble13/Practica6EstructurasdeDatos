def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def binario_a_decimal(binario):
    return int(binario, 2)

# Ejemplo de uso:
if __name__ == "__main__":
    opcion = input("¿Convertir (1) Decimal a Binario o (2) Binario a Decimal? ")
    if opcion == '1':
        numero = int(input("Introduce un número decimal: "))
        print("Binario:", decimal_a_binario(numero))
    elif opcion == '2':
        binario = input("Introduce un número binario: ")
        print("Decimal:", binario_a_decimal(binario))
    else:
        print("Opción no válida.")