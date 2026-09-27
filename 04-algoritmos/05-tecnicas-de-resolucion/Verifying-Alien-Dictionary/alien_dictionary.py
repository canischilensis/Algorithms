def alien_sorted(words, order):
    # 1) Inicializamos el diccionario que mapeará cada letra a su posición
    letter_order = {}
    for i in range(len(order)):
        letter = order[i]
        letter_order[letter] = i

    # 2) Función interna para comparar dos palabras
    def compare(w1, w2):
        n = min(len(w1), len(w2))
        for j in range(n):
            if letter_order[w1[j]] < letter_order[w2[j]]:
                print(f"{w1} < {w2} → ✅")
                return True
            if letter_order[w1[j]] > letter_order[w2[j]]:
                print(f"{w1} > {w2} → ❌")
                return False
        # Si llegamos aquí, son iguales hasta la longitud más corta
        resultado = len(w1) <= len(w2)
        signo = "✅" if resultado else "❌"
        print(f"{w1} y {w2} iguales hasta el fin, gana la más corta → {signo}")
        return resultado

    # 3) Recorremos la lista de palabras comparando cada par consecutivo
    for k in range(1, len(words)):
        if not compare(words[k-1], words[k]):
            print("Encontramos un par fuera de orden")
            return False

    return True  # Si nunca falló, todo está bien


# ---- Ejemplo de uso ----
#palabras = ["hola", "holaa", "holb"]
#orden = "hlabcdefgijkmnopqrstuvwxyz"

#print("¿Listado ordenado?", alien_sorted(palabras, orden))
