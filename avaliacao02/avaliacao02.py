import random
lista_adj = []          # Lista de adjacencias do grafo inicial
op_arestas = []         # Lista de op_arestas mapeados disponíveis
res_dj = []             # Esqueleto da árvore de baixo custo
qtd_arestas = 0         # Número de arestas da árvore nova
marcados = []           # Lista de arestas que já estão no res_dj
cam_usados = []         # Caminhos usados pelo menos uma vez no res_dj
# ==============================================================================
# A função encontra o caminho disponível de menor custo, remove da lista de op_arestas e o retorna

def encontra_menor():
    pos = 0
    min = op_arestas[0]
    min = min[0]
    for (i, line) in enumerate(op_arestas):
        c = line[0]
        if (c < min):
            min = c
            pos = i
    #print("melhor op_arestas", op_arestas[pos])
    return op_arestas.pop(pos)

# função encarregada de exibir as listas de forma padronizada


def mostrar_lista(lista):
    print("Lista de adjacências: ")
    for i, line in enumerate(lista):
        print(i, "=", line)

# Atualiza os caminhos disponíveis


def update_caminhos(a, custo):
    for (b, c) in lista_adj[a]:
        op_arestas.append((c+custo, a, b))  # custo, saída, chegada


# ==============================================================================
vertices = int(input("Entre com a quantidade de vertices: "))
arestas = int(input("Entre agora com a quantidade de arestas: "))

# Criando as posições para os vertices
lista_adj = [[]*vertices for i in range(vertices)]
# Povoando o grafo
print("\nEntre com os dados conforme o modelo:\nresta1 aresta2 custo")
for j in range(arestas):  # ler as arestas do grafo
    a, b, c = input().split()  # ponto a e b com o custo c
    a = int(a)
    b = int(b)
    c = int(c)
    lista_adj[a].append((b, c))
    if (a != b):
        lista_adj[b].append((a, c))

mostrar_lista(lista_adj)

# Escolhendo a raiz de modo aleartório
raiz = random.randint(0, vertices-1)

# Adicionando os caminhos disponiveis da raiz no op_arestas
update_caminhos(raiz, 0)

# Informando que a raíz já foi usada
marcados.append(raiz)
# Informando que o caminho usado para raiz foi padrão, não partiu de ninguém
cam_usados.append((raiz, raiz))


while qtd_arestas < (vertices-1):
    # Procurando o caminho de menor custo
    (custo, a, b) = encontra_menor()
    # Verificando se o caminho já foi usado alguma vez, para evitar ciclos e repetições
    if (((a, b) and (b, a)) not in cam_usados) and (b not in marcados):
        cam_usados.append((a, b))
        marcados.append(b)
        res_dj.append((custo, a, b))  # custo, saída, chegada
        qtd_arestas += 1

    # Adicionando novos caminhos disponíveis no op_arestas para a proxima escolha
    update_caminhos(b, custo)

print("Raiz: ", raiz)
print("Caminho segundo Dijkstra:\n", res_dj)
