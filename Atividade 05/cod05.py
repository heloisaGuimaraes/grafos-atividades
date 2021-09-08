import random
lista_adj = []          # Lista de adjacencias do grafo inicial
caminho = []            # Lista de caminhos mapeados disponíveis para a árvore de custo minimo
arv_ger_min = []        # Esqueleto da árvore de custo minimo
qtd_arestas = 0         # Número de arestas da árvore nova
custo_total = 0         # Váriável para contabilizar o custo
marcados = []           # Lista de vertices que já foram para a nova árvore

#==============================================================================
# A função encontra o caminho de menor custo, remove da lista de caminhos e o retorna
def encontra_menor():
    pos = 0
    min = caminho[0]
    min = min[0]
    for (i, line) in enumerate(caminho):
        c = line [0]
        if (c < min):
           min = c
           pos = i
    return caminho.pop(pos)        

# função encarregada de exibir as listas de forma padronizada
def mostrar_lista(lista):
    print("Lista de adjacências: ")
    for i, line in enumerate(lista, start=1):
        print(i, "=", line)

#==============================================================================
vertices = int(input("Entre com a quantidade de vertices: ")) 
arestas = int(input("Entre agora com a quantidade de aretas: "))

# Criando as posições para os vertices
lista_adj = [[]*vertices for i in range(vertices)]
# Povoando o grafo
print("\nEntre com os dados conforme o modelo:\nresta1 aresta2 custo")
for j in range(arestas): # ler as arestas do grafo
    a, b, c = input().split()  #ponto a e b com o custo c
    a = int(a)
    b = int(b)
    c = int(c)
    lista_adj[a].append((b,c))
    if (a!=b):
        lista_adj[b].append((a,c))
    
mostrar_lista(lista_adj)

# Escolhendo a raiz de modo aleartório
raiz = random.randint(0, vertices-1)

# Adicionando os caminhos disponiveis
for (x,c) in lista_adj[raiz]:
    caminho.append((c, raiz, x))
    
# Informando que a raíz já está no novo grafo
marcados.append(raiz)

while qtd_arestas < (vertices-1):
    #Procurando os melhores caminhos
    while True:
        (custo, a, b) = encontra_menor() 
        if b not in marcados:
            break
   
    #Atualizando os paramentros de controle
    marcados.append(b)
    custo_total += custo
    arv_ger_min.append((a, b))
    qtd_arestas +=1
    
    #Adicionando novos caminhos disponíveis para a proxima escolha
    for (x, c) in lista_adj[b]:
        if x not in marcados:
            caminho.append((c, b, x))

print("Raiz: ", raiz)
print("Custo total: ", custo_total)
print("Nova árvore de custo minimo:\n", arv_ger_min)