def tipo_risada(risada):
    vogais = "aeiou"
    sequencia_vogais = ""

    for caractere in risada.lower():
        if caractere in vogais:
            sequencia_vogais += caractere

    inicio = 0
    fim = len(sequencia_vogais) - 1
    while inicio < fim:
        if sequencia_vogais[inicio] != sequencia_vogais[fim]:
            return False
        inicio += 1
        fim -= 1
    return True


risada = input().strip()
print("sim" if tipo_risada(risada) else "não")









def verificar_compatibilidade(pai, filho):
    # Verifica tamanho mínimo e igualdade
    if len(pai) != len(filho) or len(pai) < 2:
        print("SEQUÊNCIAS DE TAMANHO INVÁLIDO")
        return None

    # Pega a primeira metade das sequências
    metade = len(pai) // 2
    iguais = 0

    # Compara caractere a caractere na mesma posição
    for i in range(metade):
        if pai[i] == filho[i]:
            iguais += 1

    # Calcula percentual de compatibilidade
    compatibilidade = (iguais / metade) * 100

    print(f"{compatibilidade:.2f}%")

    # Retorna True se compatibilidade ≥ 80%
    return compatibilidade >= 80


# Lista de casos de teste
casos = [
    {"pai": "AACCTGGA", "filho": "AAGCTGGT"},
    {"pai": "ACGTACGT", "filho": "ACGAACGA"},
    {"pai": "AGCTA", "filho": "AGGTA"},
    {"pai": "ACGTACGTACGTACG", "filho": "ACGTATGTACGTACG"},
    {"pai": "ACGTACGTACGTACG", "filho": "ACGAATGTACGTACG"},
    {"pai": "AACCTGGA", "filho": "AAGCTG"},
]

# Processa cada dicionário da lista
for caso in casos:
    pai = caso["pai"]
    filho = caso["filho"]

    resultado = verificar_compatibilidade(pai, filho)
    if resultado is True:
        print("POTENCIAL PAI-FILHO")
    elif resultado is False:
        print("NÃO COMPATÍVEL")
    print()  # linha em branco entre os casos
    
    
    
    
    
    
    
    
    
    
# a) Função: calcula o total diário
def total_diario(dia):
    data, manha, noite = dia
    return manha + noite


# b) Função: cria lista com (data, total_dia, diferenca)
def resumo_por_dia(lista_dias):
    resumo = []
    for dia in lista_dias:
        data, manha, noite = dia
        total = total_diario(dia)
        diferenca = manha - noite
        if diferenca < 0:
            diferenca = -diferenca  # valor absoluto sem usar abs()
        resumo.append((data, total, diferenca))
    return resumo


# c) Função: retorna a data com maior total de consumo
def maior_total(lista_resumo):
    maior = 0
    data_maior = ""
    primeiro = True

    for item in lista_resumo:
        data, total, diferenca = item
        if primeiro or total > maior:
            maior = total
            data_maior = data
            primeiro = False

    return data_maior


# --- PROGRAMA PRINCIPAL ---
dias = []

# Leitura da quantidade de dias
n = int(input())

# Leitura dos dados
for i in range(n):
    entrada = input().split()
    data = entrada[0]
    manha = float(entrada[1])
    noite = float(entrada[2])
    dias.append((data, manha, noite))

# Gera o resumo
resumo = resumo_por_dia(dias)

# Mostra o resumo
for item in resumo:
    data, total, diferenca = item
    print(data, total, diferenca)

# Mostra a data com maior consumo
print("Dia de maior consumo:", maior_total(resumo))


