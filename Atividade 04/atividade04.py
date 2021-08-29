def inicializar_matriz():
    v = int(input("Entre com a quantidade de vertices: "))
    grafo = []
    for i in range(v):
        linha = []
        for j in range(v):
            linha.append(0)
        grafo.append(linha)
    return grafo


def inicializar_lista(grafo):
    lista = []
    for i in grafo:
        vertice = []
        lista.append(vertice)
    return lista


def mostrar_matriz(grafo):
    print("Matriz de adjcências: ")
    for i in grafo:
        print(i)


def mostrar_lista(lista):
    print("Lista de adjacências: ")
    for i, line in enumerate(lista, start=1):
        print(i, "=", line)


def adc_aresta(grafo, l, c):
    if l <= len(grafo) and c <= len(grafo[0]):
        grafo[l-1][c-1] += 1
        if (l != c):
            grafo[c-1][l-1] += 1
    else:
        print("Vertices inválidos :( ")


def converte(grafo, lista):
    lista = inicializar_lista(grafo)
    for i, line in enumerate(grafo):
        for j, value in enumerate(line, start=1):
            if value != 0:
                for k in range(value): lista[i].append(j)
    return lista
    


def calc_grau(grafo, l):
    grau = sum(grafo[l])
    if (grafo[l][l] != 0):
        grau += grafo[l][l]
    return grau


def grau_vetices(grafo):
    for i in range(len(grafo)):
        print("Grau do vertice", i+1, "=", calc_grau(grafo, i))


def maior_grau(grafo):
    maior = 0
    for i in range(len(grafo)):
        aux = calc_grau(grafo, i)
        if (aux > maior):
            maior = aux

    print("Maior grau: ", maior)


def menor_grau(grafo):
    menor = calc_grau(grafo, 0)

    for i in range(len(grafo)):
        aux = calc_grau(grafo, i)
        if (aux < menor):
            menor = aux

    print("Menor grau: ", menor)


# ===========================================================================
grafo = inicializar_matriz()
lista = inicializar_lista(grafo)

while True:
    print("========================================")
    print("Escolha uma opção: ")
    print("1) Mostrar grafo; ")
    print("2) Adicionar aresta; ")
    print("3) Converter para lista de adjacências; ")
    print("Extras: ")
    print("4) Grau de cada vertice; ")
    print("5) Grau mínimo; ")
    print("6) Grau máximo; ")
    print("0) Encerar menu. ")
    opcao = int(input("Opção: "))
    print("========================================")

    if(opcao == 1):
        mostrar_matriz(grafo)
    elif(opcao == 2):
        l = int(input("Informe o primeiro vertice: "))
        c = int(input("Informe o segundo vertice: "))
        adc_aresta(grafo, l, c)
    elif(opcao == 3):
        lista = converte(grafo, lista)
        mostrar_lista(lista)
    elif(opcao == 4):
        grau_vetices(grafo)
    elif(opcao == 5):
        menor_grau(grafo)
    elif(opcao == 6):
        maior_grau(grafo)
    elif(opcao == 0):
        print("Menu encerrado. Adiós!")
        break
    else:
        print('A opção digitada é inválida, tente novamente.')
