from collections import Counter

def encontrar_numeros_mais_repetidos(listas, num_listas=3, num_numeros=6):
    # Contar a frequência de cada número em todas as listas
    contagem_total = Counter()
    
    for lista in listas:
        numeros = lista.split('\n')
        numeros = [int(numero) for numero in numeros if numero.strip()]
        contagem_total.update(numeros)
    
    # Encontrar os números mais repetidos
    mais_repetidos = contagem_total.most_common(num_numeros)
    
    # Criar as listas de números mais repetidos, garantindo que sejam diferentes
    resultados = []

    while len(resultados) < num_listas:
        numeros_mais_repetidos = [numero for numero, frequencia in mais_repetidos]
        resultados.append(numeros_mais_repetidos)
        
        # Remover os números mais repetidos já escolhidos
        for numero, _ in mais_repetidos:
            del contagem_total[numero]
        
        mais_repetidos = contagem_total.most_common(num_numeros)

    return resultados

# Lista fornecida com o número 2 na primeira linha
listas_fornecidas = [
    "09\n30\n34\n44\n54\n55\n",
    "01\n02\n10\n32\n34\n59\n",
    "05\n16\n38\n42\n43\n48\n",
    "06\n11\n29\n37\n56\n58\n",
    "08\n27\n28\n32\n48\n56\n",
    "02\n23\n25\n33\n45\n54\n",
    "05\n10\n27\n38\n56\n57\n",
    "14\n26\n36\n39\n50\n53\n",
    "14\n18\n22\n26\n31\n38\n",
    "11\n32\n35\n40\n41\n48\n",
    "05\n14\n32\n40\n53\n54\n",
    "13\n25\n31\n43\n57\n58\n",
    "01\n09\n13\n16\n52\n59\n",
    "09\n10\n35\n44\n55\n58\n",
    "05\n31\n37\n47\n52\n58\n",
    "10\n15\n20\n35\n37\n59\n",
    "09\n19\n22\n24\n50\n60\n"
]

numeros_mais_repetidos = encontrar_numeros_mais_repetidos(listas_fornecidas, num_listas=3, num_numeros=6)

for i, numeros in enumerate(numeros_mais_repetidos, start=1):
    numeros_ordenados = sorted(numeros)
    print(f"Lista {i} - Números mais repetidos:", numeros)