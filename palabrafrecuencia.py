def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.strip('.,;:"!?').lower()
        if palabra:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def palabra_mas_frecuente(diccionario):
    if not diccionario:
        return None, 0
    palabra = max(diccionario, key=diccionario.get)
    return palabra, diccionario[palabra]

# Ejemplo de uso:
if __name__ == "__main__":
    texto = input("Introduce un texto: ")
    frecuencias = contar_palabras(texto)
    print("Frecuencias:", frecuencias)
    palabra, repeticiones = palabra_mas_frecuente(frecuencias)
    print(f"La palabra más frecuente es '{palabra}' con {repeticiones} repeticiones.")