import json

# Lê o arquivo JSON com os valores de faturamento diário
with open('valores.json', 'r') as file:
    dados = json.load(file)

# Inicializa as variáveis de mínimo, máximo e soma
minimo = float('inf')
maximo = float('-inf')
soma = 0
dias_uteis = 0

# Itera pelos dados e atualiza as variáveis de mínimo, máximo e soma
for dado in dados:
    if dado['valor'] > 0:
        dias_uteis += 1
        soma += dado['valor']
        if dado['valor'] < minimo:
            minimo = dado['valor']
        if dado['valor'] > maximo:
            maximo = dado['valor']

# Calcula a média mensal considerando somente os dias úteis
media = soma / dias_uteis

# Inicializa a variável de contagem de dias com faturamento acima da média
acima_da_media = 0

# Itera novamente pelos dados e verifica se o valor está acima da média
for dado in dados:
    if dado['valor'] > media:
        acima_da_media += 1

# Imprime os resultados
print('Menor valor de faturamento ocorrido em um dia do mês:', minimo)
print('Maior valor de faturamento ocorrido em um dia do mês:', maximo)
print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:', acima_da_media)
