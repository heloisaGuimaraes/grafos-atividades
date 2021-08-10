def inicializar_grafo():
    v = int(input("Entre com a quantidade de vertices: "))
    grafo = []

    for i in range(v):
        linha = []
        for j in range(v):
            linha.append(0)
        grafo.append(linha)

    print("Grafo inicializado:")
    mostrar_grafo(grafo)
    return grafo


def mostrar_grafo(grafo):
    for i in grafo:
        print(i)


def adc_aresta(grafo, l, c):
    grafo[l-1][c-1] += 1
    grafo[c-1][l-1] += 1


def grau_vetices(grafo):
    for i in range(len(grafo)):
        print("Grau do vertice", i+1, "=", sum(grafo[i]))


def maior_grau(grafo):
    l = len(grafo)
    maior = sum(grafo[0])

    for i in range(l):
        aux = sum(grafo[i])
        if (aux > maior):
            maior = aux

    print("Maior grau: ", maior)


def menor_grau(grafo):
    l = len(grafo)
    menor = sum(grafo[0])

    for i in range(l):
        aux = sum(grafo[i])
        if (aux < menor):
            menor = aux

    print("Menor grau: ", menor)

#===========================================================================
grafo = inicializar_grafo()

while True:
    print("========================================")
    print("Escolha uma opção: ")
    print("1) Mostrar grafo; ")
    print("2) Adicionar aresta; ")
    print("3) Grau de cada vertice; ")
    print("4) Grau mínimo; ")
    print("5) Grau máximo; ")
    print("0) Encerar menu. ")
    opcao = int(input("Opção: "))
    print("========================================")
    
    if(opcao == 1):
        print("Grafo em seu estado atual:")
        mostrar_grafo(grafo)

    elif(opcao == 2):
        l = int(input("Informe o primeiro vertice: "))
        c = int(input("Informe o segundo vertice: "))
        adc_aresta(grafo, l, c)
    elif(opcao == 3):
        grau_vetices(grafo)
    elif(opcao == 4):
        menor_grau(grafo)
    elif(opcao == 5):
        maior_grau(grafo)
    elif(opcao == 0):
        print("Menu encerrado. Adiós!")
        break
    else:
        print('A opcao digitada é inválida, tente novamente.')
        
