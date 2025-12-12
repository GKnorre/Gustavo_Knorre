class Chamado:
    def __init__(self, id_chamado, titulo, prioridade, status):
        self.id_chamado = id_chamado
        self.titulo = titulo
        self.prioridade = prioridade
        self.status = status


# -------------------- ORDENAR LISTA (necessário para busca binária) --------------------

def ordenar_por_id(lista_chamados):
    n = len(lista_chamados)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista_chamados[j].id_chamado < lista_chamados[menor].id_chamado:
                menor = j
        temp = lista_chamados[i]
        lista_chamados[i] = lista_chamados[menor]
        lista_chamados[menor] = temp


# -------------------- LETRA A: BUSCA BINÁRIA --------------------

def buscar_binaria(lista_chamados, id_busca):
    inicio = 0
    fim = len(lista_chamados) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_chamados[meio].id_chamado == id_busca:
            return True
        elif lista_chamados[meio].id_chamado < id_busca:
            inicio = meio + 1
        else:
            fim = meio - 1

    return False


# -------------------- LETRA B: BUSCA SEQUENCIAL POR PRIORIDADE --------------------

def buscar_por_prioridade(lista_chamados, minimo, maximo):
    resultado = []
    for ch in lista_chamados:
        if ch.prioridade >= minimo and ch.prioridade <= maximo:
            resultado.append(ch)
    return resultado


# -------------------- ENTRADA DOS DADOS --------------------

lista_chamados = []

qtd = int(input("Quantidade de chamados: "))

for i in range(qtd):
    print("Chamado", i + 1)
    id_c = int(input("ID: "))
    titulo = input("Titulo: ")
    prioridade = int(input("Prioridade (1 a 5): "))
    status = input("Status: ")

    c = Chamado(id_c, titulo, prioridade, status)
    lista_chamados.append(c)


# ordenar lista (necessário para busca binária)
ordenar_por_id(lista_chamados)


# -------------------- TESTE LETRA A --------------------

id_procurar = int(input("Digite um ID para buscar: "))

achou = buscar_binaria(lista_chamados, id_procurar)

if achou:
    print("ID encontrado")
else:
    print("ID nao encontrado")


# -------------------- TESTE LETRA B --------------------

minimo = int(input("Prioridade minima: "))
maximo = int(input("Prioridade maxima: "))

lista_filtrada = buscar_por_prioridade(lista_chamados, minimo, maximo)

print("Chamados dentro do intervalo:")
for ch in lista_filtrada:
    print(ch.id_chamado, ch.titulo, ch.prioridade, ch.status)
    
    
    
    
    
    
    
    
    
    
    
    
    
    class Filme:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano


def ordenar_filmes(lista_filmes):
    n = len(lista_filmes)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista_filmes[j].ano < lista_filmes[menor].ano:
                menor = j
        temp = lista_filmes[i]
        lista_filmes[i] = lista_filmes[menor]
        lista_filmes[menor] = temp
    
