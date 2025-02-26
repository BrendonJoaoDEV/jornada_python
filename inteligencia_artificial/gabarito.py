# Por conta do desmenbramento do arquivo .ipynb em um arquivo .py e um .md
# Foram substituídos os comandos display por print.

# Passo a passo
# Passo 0 - Entender a empresa e o desafio da empresa
# Passo 1 - Importar a base de dados
import pandas as pd

tabela = pd.read_csv("clientes.csv")

print(tabela)

# Score de crédito = Nota de crédito
# Good = Boa
# Standard = OK
# Poor = Ruim

# Passo 2 - Preparar a base de dados para a Inteligência Artificial
print(tabela.info())

# int -> numero inteiro
# float -> numero com casa decimal
# object -> texto

# LabelEncoder
from sklearn.preprocessing import LabelEncoder

# profissao

# cientista - 1
# bombeiro - 2
# engenheiro - 3
# dentista - 4
# artista - 5
codificador_profissao = LabelEncoder()
tabela["profissao"] = codificador_profissao.fit_transform(tabela["profissao"])


# mix_credito
codificador_credito = LabelEncoder()
tabela["mix_credito"] = codificador_credito.fit_transform(tabela["mix_credito"])

# comportamento_pagamento
codificador_pagamento = LabelEncoder()
tabela["comportamento_pagamento"] = codificador_pagamento.fit_transform(tabela["comportamento_pagamento"])

print(tabela.info())

# y -> é a coluna da base de dados que eu quero prever
y = tabela["score_credito"]

# x -> as colunas da base de dados que eu vou usar pra fazer a previsão
x = tabela.drop(columns=["score_credito", "id_cliente"])

# separar em dados de treino e dados de teste
from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Passo 3 - Treinar a Inteligência Artificial -> 
# Criar o modelo: Nota de crédito: Boa, Ok, Ruim

# Arvore de Decisão -> RandomForest
# Nearest Neighbors -> KNN -> Vizinhos Próximos

# importar a IA (Inteligencia Artificial)
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# criar a IA
modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

# treinar a IA
modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

# Passo 4 - Escolher qual o melhor modelo
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

# acurácia
from sklearn.metrics import accuracy_score
print(accuracy_score(y_teste, previsao_arvoredecisao))
print(accuracy_score(y_teste, previsao_knn))

# Passo 5 - Usar o melhor modelo para fazer previsão de novos clientes
# melhor modelo é o modelo_arvoredecisao

# importar os novos clientes para fazer a previsao
tabela_novos_clientes = pd.read_csv("novos_clientes.csv")

# profissao
tabela_novos_clientes["profissao"] = codificador_profissao.transform(
    tabela_novos_clientes["profissao"])


# mix_credito
tabela_novos_clientes["mix_credito"] = codificador_credito.transform(
    tabela_novos_clientes["mix_credito"])

# comportamento_pagamento
tabela_novos_clientes["comportamento_pagamento"] = codificador_pagamento.transform(
    tabela_novos_clientes["comportamento_pagamento"])


print(tabela_novos_clientes)

nova_previsao = modelo_arvoredecisao.predict(tabela_novos_clientes)
print(nova_previsao)
